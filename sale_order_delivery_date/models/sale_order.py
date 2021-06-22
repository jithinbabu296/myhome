# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.constrains('date_order', 'commitment_date')
    def _compute_display_time(self):
        for rec in self:
            if rec.date_order and rec.commitment_date:
                today = (rec.commitment_date - rec.date_order).days
                dates = abs(today)
                if dates >= 14:
                    raise ValidationError(_('Delivery date should be with in 2 weeks from the day they creating the SO'))
