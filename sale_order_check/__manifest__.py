# -*- coding: utf-8 -*-
{
    'name': "Sale Order Check",
    'summary': """Check order by phone no., mobile no., membership no., Customer name """,
    'description': """Filter the order by phone no., mobile no., membership no., Customer name.""",
    'author': "SGG",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order.xml',
        'views/sale_filter.xml',
    ],
}