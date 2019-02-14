# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ecosoft Website',
    'category': 'Theme/Creative',
    'description': """
Odoo Web Editor widget.
==========================

""",
    'version': '1.0',
    'author': 'Saran Lim.',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        # 'data/data_submenu.xml',
        'views/templates.xml',
        'views/theme_customize_view.xml',
        # 'views/our_approach_page.xml',
    ],
}
