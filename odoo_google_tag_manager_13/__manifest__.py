# -*- coding: utf-8 -*-

{
    'name': "Google Tag Manager Odoo (V13)",
    'summary': 'Google Tag Manager - Odoo integration',
    'description': 'Includes Google Tag Manager in the website metadata',
    'author': "Hedra",
    'website': "www.hedra.com.br",
    'category': 'Integration',
    'version': '13.1.0.0',
    # 'license': 'LGPL-3',
    'depends': ['base', 'website', 'website_sale', 'account'],

    'data': [
        'views/website_view.xml',
        'views/res_config_settings_view.xml',
        'views/website_template.xml',
    ],

}
