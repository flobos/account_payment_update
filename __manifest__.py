# -*- coding: utf-8 -*-
{
    'name': "account_payment_update",

    'summary': """
        Modifica el form account payment para ingresar mas informacion del pago""",

    'description': """
        Modifica el form account payment para ingresar mas informacion del pago
    """,

    'author': "Fimar",
    'website': "http://www.fimarcorp.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale','stock', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/account_payment_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}