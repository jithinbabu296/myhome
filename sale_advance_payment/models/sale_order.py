# -*- coding: utf-8 -*-

from odoo import models, fields, api





class SaleOrder(models.Model):
    _inherit = "sale.order"

# class SaleAdvancePaymentInv(models.TransientModel):
#       _inherit = "sale.advance.payment.inv"
    # def action_advance_payment(self):
    #     if self.order_line.product_id.route_ids.name == 'Dropship':
    #   def create_invoices(self):
    #       res=super(SaleAdvancePaymentInv, self).create_invoices()
    #       if self.product_id.route_ids.name == 'Dropship':
    #           self.state = 'sale'
    #       return res



