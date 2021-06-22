# -*- coding: utf-8 -*-

{
    'name': 'Product Brand in Inventory',
    'version': '14.0.1.0.0',
    'category': 'Warehouse',
    'summary': 'Product Brand in Inventory',
    # 'images': ['static/description/banner.png'],
    'depends': ['stock'],
    'data': [
        'views/brand_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,

}
