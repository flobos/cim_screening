# -*- coding: utf-8 -*-
{
    'name': "Mediges",

    'summary': """
        Screening""",

    'description': """
        Screening Cim
    """,

    'author': "Fernando Lobos",
    'website': "http://www.cimtalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Mediges',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale'],

    # always loaded
    'data': [
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}