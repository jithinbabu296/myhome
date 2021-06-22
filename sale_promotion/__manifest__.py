# -*- coding: utf-8 -*-


{
    'name': "Sale Promotion",
    'version': '14.0.1.0.1',
    'summary': """Create Promotion Offers For Sales""",
    'description': """This Module Allows to Set  Promotion Offers On Products And Product Categories.""",
    'author': "SGG",
    'category': 'Sales',
    'depends': ['sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/promotion_product.xml',
        'views/sale_promotion_rule.xml',
        'views/sale_order.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}


