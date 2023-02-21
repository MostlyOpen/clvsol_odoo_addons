# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Patient (Aux)',
    'summary': 'Patient (Aux) Module used by CLVsol Solutions.',
    'version': '15.0.6.1',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
        'clv_partner_entity',
        'clv_global_tag',
        'clv_patient',
    ],
    'data': [
        'security/patient_aux_security.xml',
        'security/ir.model.access.csv',
        'views/patient_aux_view.xml',
        'views/patient_aux_marker_view.xml',
        'views/patient_aux_category_view.xml',
        'views/res_partner_view.xml',
        'views/global_tag_view.xml',
        'views/address_name_view.xml',
        'views/patient_view.xml',
        'views/phase_view.xml',
        'views/patient_aux_reg_state_view.xml',
        'views/patient_aux_state_view.xml',
        'views/patient_aux_age_range_view.xml',
        'wizard/patient_aux_mass_edit_view.xml',
        'wizard/patient_associate_to_patient_aux_view.xml',
        'views/patient_aux_menu_view.xml',
        'data/default_value.xml',
        "data/patient_aux_compute_age_reference_cron.xml",
        "data/patient_aux_update_age_range_id_cron.xml",
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
