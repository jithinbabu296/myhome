# -*- coding: utf-8 -*-
import requests
import json
from json import dump
from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_select(self):
        if self.street:
            value= self.street
            headers = {'Content-type': 'application/json', 'Accept': 'application/json', }
            response = requests.get("https://www.als.ogcio.gov.hk/lookup?", headers=headers, params={'q': value})
            if response.status_code == 200:
                result = response.json()
                data = result['SuggestedAddress']
                unique_stuff = {each['Address']['PremisesAddress']['EngPremisesAddress']['EngStreet']['StreetName']: each
                                   for each in data}.values()
                line = []
                print(len(unique_stuff))
                for address in unique_stuff:
                    name = address['Address']['PremisesAddress']['EngPremisesAddress']['EngStreet']
                    second_street = address['Address']['PremisesAddress']['ChiPremisesAddress']['ChiStreet']
                    city = address['Address']['PremisesAddress']['EngPremisesAddress']['EngDistrict']
                    # nation = address['Address']['PremisesAddress']['EngPremisesAddress']
                    location = name.get('StreetName')
                    street2 = second_street.get('StreetName')
                    town = city.get('DcDistrict')
                    # country = nation.get('Region')
                    line.append((0, 0, {
                            'location': location,
                            'street_ids': street2,
                            'town': town,
                             # 'country':country
                           }))
                    print(line)
                return {'name': 'Return Order',
                        'type': 'ir.actions.act_window',
                        'res_model': 'return.street',
                        'view_mode': 'form',
                        'target': 'new',
                        'context': {'default_return_ids': line}
                             }
        else:
            raise ValidationError(_("Plese fill the street field"))


