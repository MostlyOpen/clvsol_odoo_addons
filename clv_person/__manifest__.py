# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Person',
    'summary': 'Person Module used by CLVsol Solutions.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
        'clv_partner_entity',
        'clv_global_tag',
        'clv_address',
        'clv_family',
        'clv_employee',
    ],
    'data': [
        'security/person_security.xml',
        'security/ir.model.access.csv',
        'views/person_view.xml',
        'views/person_category_view.xml',
        'views/person_marker_view.xml',
        'views/person_tag_view.xml',
        'views/res_partner_view.xml',
        'views/global_tag_view.xml',
        'views/address_name_view.xml',
        'views/address_view.xml',
        'views/family_view.xml',
        'views/global_settings_view.xml',
        'views/phase_view.xml',
        'views/person_reg_state_view.xml',
        'views/person_state_view.xml',
        'views/employee_view.xml',
        'views/random_view.xml',
        'views/set_element_view.xml',
        'views/person_age_range_view.xml',
        'wizard/person_mass_edit_view.xml',
        'wizard/person_contact_information_updt_view.xml',
        'wizard/person_associate_to_family_view.xml',
        'wizard/person_address_mass_edit_view.xml',
        'views/person_menu_view.xml',
        "data/person_compute_age_reference_cron.xml",
        "data/person_update_age_range_id_cron.xml",
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
