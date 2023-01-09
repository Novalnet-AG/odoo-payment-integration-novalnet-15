# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Novalnet account payment link',
    'summary': 'Novalnet account payment link in mail template',
    'version': '1.0.0',
    'category': 'Accounting/Accounting',
    'depends': ['account'],
    'data': [
        'data/mail_template_data.xml',
        'views/account_move_views.xml'
    ],
    'demo': [],
    'application': True,
    'license': 'LGPL-3',
}
