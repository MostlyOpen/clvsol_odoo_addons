# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Employee',
    'summary': 'Employee Module used by CLVsol Solutions.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'hr',
        'clv_base',
        'clv_global_tag',
        'clv_phase',
        'clv_set',
    ],
    'data': [
        'security/employee_security.xml',
        'security/ir.model.access.csv',
        'views/hr_employee_view.xml',
        'views/hr_job_view.xml',
        'views/global_tag_view.xml',
        'views/phase_view.xml',
        'views/set_element_view.xml',
        'wizard/hr_employee_mass_edit_view.xml',
        'wizard/hr_employee_user_groups_updt_view.xml',
        'wizard/hr_employee_associate_to_set_view.xml',
        'data/set_element.xml',
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
