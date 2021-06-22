{
    'name': 'POS Promotion',
    'category': 'Point of Sale',
    'summary' : "Point of Sale Promotion",
    'description': """
User needs to create the promotion according to promotion, rules will be apply in POS.
""",
    'author': "Sigb",
    'depends': ['web', 'point_of_sale','sale_management'],
    'version': '1.0',
    'data': [
        'views/pos_promotion_view.xml',
        'views/promotion_template.xml',
        # 'views/product_brand_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'test': [],
    'qweb': ['static/src/xml/pos_promotion.xml'],
    'installable': True,
    'auto_install': False,
}