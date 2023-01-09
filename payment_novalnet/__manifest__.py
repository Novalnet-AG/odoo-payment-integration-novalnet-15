{
    'name': 'Payment Provider: Novalnet',
    'version': '3.1.0',
    'category': 'Accounting/Payment Providers',
    'summary': "A payment service provider covering several payment.",
    'author': 'Novalnet',
    'website': 'https://www.novalnet.de',
    'depends': ['sale','payment'],
    'data': [
        'views/payment_novalnet_templates.xml',
        'views/payment_provider_views.xml',
        'views/novalnet_payment_method.xml',
        'views/callback_notification.xml',
        'security/ir.model.access.csv',
        'data/mail_template_data.xml',
        'data/payment_provider_data.xml',
        'wizards/payment_link_wizard_views.xml',
    ],
    'application': True,
    'uninstall_hook': 'uninstall_hook',
    'assets': {
        'web.assets_frontend': [
            'payment_novalnet/static/src/js/payment_form.js',
        ],
    },
    'license': 'LGPL-3'
}
