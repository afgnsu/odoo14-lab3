# -*- coding: utf-8 -*-
{
    'name': "Lab3(多對多)",

    'summary': "多對多(Many2many)練習",

    'description': "介吾測試",

    'author': "蘇介吾",
    'website': "http://afgn.cc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/lab3_movie.xml',
        'views/lab3_tag.xml',
        'views/lab3_menu.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': ['demo/demo.xml'],
}
