# -*- coding: utf-8 -*-
{
    'name': "Delivery Slip Enhancement",
    'summary': """modify some fields on the Delivery slip""",
    'description': """modify the fields on the delivery slip so they are a bit more informational to the 
                    pickers/delivery people.""",
    'author': "SGG",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base', 'sale', 'purchase', 'account', 'stock'],
    'data': [
        'report/report_deliveryslip.xml'
    ],
}
