# -*- coding: utf-8 -*-
from odoo import models,fields,api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount = fields.Selection([
            ('yes', 'yes'),
            ('no', 'no')],string="Discount")
    remarks = fields.Text()
    product_no = fields.Char(string='Product Number')
    model_no = fields.Char(string='Model Number')
    price_time = fields.Datetime('Change Time')
    product_spec = fields.Text('Product Specification')




