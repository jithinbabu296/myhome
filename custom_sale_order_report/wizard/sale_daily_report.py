# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleDailyReportWizard(models.TransientModel):
    _name = 'sale.daily.report.wizard'
    _description = ' Sale Details Report'

    start_date = fields.Datetime(required=True, default=fields.Datetime.now())
    end_date = fields.Datetime(required=True, default=fields.Datetime.now)


    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            self.end_date = self.start_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    def generate_report(self):
        data = {'date_start': self.start_date, 'date_stop': self.end_date}
        return self.env.ref('custom_sale_order_report.sale_details_report_id').report_action(self, data=data)


