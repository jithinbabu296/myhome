# -*- coding: utf-8 -*-
{
    'name': "Contact HK database",
    'summary': """Create custom hk database in contact""",
    'author': "SGG",
    'category': 'Uncategorized',
    'version': '14.0.1.2',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'wizard/street_details.xml'
    ],
}