# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import ValidationError



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.constrains('route_ids')
    def selection_routes(self):
        for rec in self:
            if len(rec.route_ids) > 1:
                 raise ValidationError(_('Only you can select one route'))
