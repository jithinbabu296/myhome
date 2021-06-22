# -*- coding: utf-8 -*-


from odoo import models,fields,api


class ProductBrand(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('brand.product',string='Brand Name')
    brand_code = fields.Char(string="Brand Code",related='brand_id.brand_code')


class BrandProduct(models.Model):
    _name = 'brand.product'


    name= fields.Char(String="Name")
    brand_image = fields.Binary()
    brand_code = fields.Char(string='Brand Code')
    member_ids = fields.One2many('product.template', 'brand_id')
    product_count = fields.Char(String='Product Count', compute='get_count_products', store=True)

    @api.depends('member_ids')
    def get_count_products(self):
        self.product_count = len(self.member_ids)


class BrandReportStock(models.Model):
    _inherit = 'stock.quant'

    brand_id  = fields.Many2one(related='product_id.brand_id',
        string='Brand', store=True, readonly=True)


