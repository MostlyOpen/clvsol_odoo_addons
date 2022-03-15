# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Document',
    'summary': 'Document Module used by CLVsol Solutions.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
        'clv_global_tag',
    ],
    'data': [
        'security/document_security.xml',
        'security/ir.model.access.csv',
        'views/document_view.xml',
        'views/document_type_view.xml',
        'views/document_type_parameter_view.xml',
        'views/document_category_view.xml',
        'views/document_marker_view.xml',
        'views/global_tag_view.xml',
        'views/document_item_view.xml',
        'views/referenceable_model_view.xml',
        'views/phase_view.xml',
        'views/document_reg_state_view.xml',
        'views/document_state_view.xml',
        'wizard/document_mass_edit_view.xml',
        'wizard/document_items_refresh_view.xml',
        'wizard/document_type_mass_edit_view.xml',
        'wizard/document_type_duplicate_view.xml',
        'wizard/document_type_items_setup_view.xml',
        'wizard/document_items_ok_setup_view.xml',
        'views/document_menu_view.xml',
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
