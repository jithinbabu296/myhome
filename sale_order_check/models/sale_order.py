# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    phone_no = fields.Char("phone_no")
    mobile_no = fields.Char("mobile_no")
    # phone_no = fields.Many2one('res.partner')


    @api.onchange('partner_id')
    def _set_phone_no(self):
        for rec in self:
            if rec.partner_id:
                rec.phone_no = rec.partner_id.phone

    @api.onchange('partner_id')
    def _set_mobile_no(self):
        for rec in self:
            if rec.partner_id:
                rec.mobile_no = rec.partner_id.mobile