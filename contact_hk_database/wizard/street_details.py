# -*- coding: utf-8 -*-


from odoo import fields, models,_
from odoo.exceptions import UserError, ValidationError


class ReturnStreet(models.TransientModel):
    _name = 'return.street'

    return_ids = fields.One2many('return.line', 'line_id', string="Return Order")

    def ret_street(self):
        active_ids = self.env['res.partner'].browse(self._context.get("active_ids"))
        response = self.return_ids.filtered(lambda x:x.is_selected == True)
        if len(response) > 1:
            raise ValidationError(_("Plese select only one recond"))
        elif len(response) !=1:
            raise ValidationError(_("Please select a recond"))
        else:
            active_ids.street = response.location
            active_ids.street2 = response.street_ids
            active_ids.city = response.town
            # active_ids.country_id = response.country

        # country_id = self.env['res.country'].search([('code', '=', response.country.get('country_code'))])
        # print(country_id)
    # def write(self,values):
    #     res=super(ReturnStreet, self).write(values)
    #     print("hello")
    #     if values.get('country_code', False):
    #         country_id = self.env['res.country'].search([('code', '=', values.get('country_code'))])
    #         print(country_id)
    #     return res
            # vals['country_id'] = country_id and country_id.id


class ReturnLine(models.TransientModel):
    _name = 'return.line'

    line_id = fields.Many2one('return.street', string="return Line")
    location = fields.Char(string="Street")
    town = fields.Char(string="City")
    street_ids = fields.Char(string="Street2")
    country = fields.Char(string="Country")
    is_selected = fields.Boolean(default=False)


