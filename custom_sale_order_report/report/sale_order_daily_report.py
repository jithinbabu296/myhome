from datetime import timedelta
import pytz
from odoo import api, models,fields, _
from odoo.osv.expression import AND


class ReportDailySalesOrder(models.AbstractModel):
    _name = 'report.custom_sale_order_report.report_sale_order_daily'
    _description = 'Daily Sale Order Report'


    @api.model
    def get_sale_details(self, date_start=False, date_stop=False):
        """
        :param date_start: The dateTime to start, default today 00:00:00.
        :type date_start: str.
        # :param date_stop: The dateTime to stop, default date_start + 23:59:59.
        # :type date_stop: str.
      """
        amount=0
        order=0
        domain = [('state', 'in', ['sale','cancel'])]
        cancel =  [('state', 'in', ['cancel'])]
        if date_start:
            date_start = fields.Datetime.from_string(date_start)
        else:
            # start by default today 00:00:00
            user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
            today = user_tz.localize(fields.Datetime.from_string(fields.Date.context_today(self)))
            date_start = today.astimezone(pytz.timezone('UTC'))

        if date_stop:
            date_stop = fields.Datetime.from_string(date_stop)
            # avoid a date_stop smaller than date_start
            if (date_stop < date_start):
                date_stop = date_start + timedelta(days=1, seconds=-1)
        else:
            # stop by default today 23:59:59
            date_stop = date_start + timedelta(days=1, seconds=-1)

        domain = AND([domain,
            [('date_order', '>=', fields.Datetime.to_string(date_start)),
            ('date_order', '<=', fields.Datetime.to_string(date_stop))]
        ])

        cancel = AND([cancel,
                      [('date_order', '>=', fields.Datetime.to_string(date_start)),
                       ('date_order', '<=', fields.Datetime.to_string(date_stop))]
                      ])

        order_cancel = self.env['sale.order'].search(cancel)
        cancel_from = self.env['sale.order'].search(cancel, order='id asc', limit=1)
        cancel_to = self.env['sale.order'].search(cancel, order='id desc', limit=1)

        orders = self.env['sale.order'].search(domain)
        order_from=self.env['sale.order'].search(domain,order='id asc',limit=1)
        order_to=self.env['sale.order'].search(domain,order='id desc',limit=1)


        orders_qty=len(orders)
        for order in orders:
            # print(order.order_line.product_uom)
            amount += order.amount_total
        total_amount = round(amount,2)

        total_qty=0
        payment=0
        refund_amount=0
        total_payment=0
        balance=0
        overall_amount=0
        for rec in orders.invoice_ids:
            balance= balance + rec.amount_residual
            payment=payment + rec.amount_total
            if rec.move_type == 'out_refund':
                total_qty += len(rec)
                refund_amount += rec.amount_total
            else:
                overall_amount += rec.amount_total
        refund_qty = total_qty
        refund_total = round(refund_amount,2)
        outstanding_balance = round(balance,2)
        main_total = round(overall_amount,2)
        total_payment += round(total_payment + payment + outstanding_balance,2)

        cancel_qty=0
        cancel_amount=0
        for cancel in order_cancel:
                cancel_qty += len(cancel)
                cancel_amount += cancel.amount_total
        cancel_order_qty=cancel_qty
        cancel_order_amount=round(cancel_amount,2)
        total = round(cancel_order_amount + refund_total + total_amount,2)

        outstand_qty=0
        for outstand in orders.invoice_ids:
            for out in outstand.invoice_line_ids:
                if outstand.amount_residual != 0:
                    outstand_qty += out.quantity
        out_qty=format(outstand_qty,'.2f')

        return {
            "qty":orders_qty,
            'docs': order,
            'docer':orders,
            'order_from':order_from,
            'order_to':order_to,
            'total_amount':total_amount,
            'refund_qty':refund_qty,
            'cancel_order_qty':cancel_order_qty,
            'refund_total':refund_total,
            'cancel_order_amount':cancel_order_amount,
            'total':total,
            'total_payment':total_payment,
            'cancel_from':cancel_from,
            'cancel_to':cancel_to,
            'outstanding_balance':outstanding_balance,
            'main_total':main_total,
            'out_qty':out_qty
        }

    @api.model
    def _get_report_values(self, docids, data=None):
        data = dict(data or {})
        data.update(self.get_sale_details(data['date_start'], data['date_stop'],))
        return data

