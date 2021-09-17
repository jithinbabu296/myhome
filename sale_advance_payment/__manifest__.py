# -*- coding: utf-8 -*-
{
    'name' : 'Sale Advance Payment',
    'version' : '14.1.0',
    'summary': 'Sale & Advanced Payments',
    'description': """
    'author':"SGG-jithin"
Dropshipping in Sale
====================
Create a advanced payment feature in sale before confirm the sale order
    """,
    'depends' : ['base', 'purchase', 'sale', 'account'],
    'data': [
        'views/sale_order.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
