# -*- coding: utf-8 -*-
from odoo import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """ This method will find Customer names,address,mobile_no according to its
        phone"""
        if name and not self.env.context.get('import_file'):
            args = args if args else []
            args.extend(['|', ['name', 'ilike', name],
                         '|', ['mobile', 'ilike', name],
                         ['function', 'ilike', name]])
            name = ''
        return super(ResPartner, self).name_search(
            name=name, args=args, operator=operator, limit=limit)
