# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Base Module',
    'summary': 'Base Module used by CLVsol Solutions.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': ['base'],
    'data': [
        'security/base_security.xml',
        'security/ir.model.access.csv',
        'views/global_settings_view.xml',
        'views/referenceable_model_view.xml',
        'views/default_value_view.xml',
        'views/abstract_log_view.xml',
        'views/abstract_tag_view.xml',
        'views/abstract_category_view.xml',
        'views/abstract_marker_view.xml',
        'views/abstract_format_view.xml',
        'views/global_settings_filestore_view.xml',
        # 'views/abstract_h_category_view.xml',
        'views/base_menu_view.xml',
        'views/global_settings_menu_view.xml',
        'views/referenciable_model_menu_view.xml',
        'views/default_value_menu_view.xml',
        'views/mfmng_menu_view.xml',
        'views/health_menu_view.xml',
        'views/community_menu_view.xml',
        # 'views/aux_menu_view.xml',
        # 'views/processing_menu_view.xml',
        # 'views/export_menu_view.xml',
        # 'views/report_menu_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
