# -*- coding: utf-8 -*-
{
    'name': "Custom Sale Order Report",
    'summary': """Create custom sale order report""",
    'author': "SGG",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base', 'sale','purchase','stock'],
    'data': [
        'security/ir.model.access.csv',
        'report/sale_order_daily_report.xml',
        'report/sale_order_template.xml',
        'report/sale_order.xml',
        'wizard/sale_daily_order_report.xml',
    ],
}