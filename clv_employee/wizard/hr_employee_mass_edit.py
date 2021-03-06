# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

'''
Reference: http://help.odoo.com/question/18704/hide-menu-for-existing-group/

There are actually0-6 numbers for representing each job for a many2many/ one2many field

    (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
    (1, ID, { values }) -- update the linked record with id = ID (write values on it)
    (2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the
               object completely, and the link to it as well)
    (3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two
               objects but does not delete the target object itself)
    (4, ID) -- link to existing record with id = ID (adds a relationship)
    (5) -- unlink all (like using (3,ID) for all linked records)
    (6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
'''

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class EmployeeMassEdit(models.TransientModel):
    _description = 'Employee Mass Edit'
    _name = 'hr.employee.mass_edit'

    def _default_employee_ids(self):
        return self._context.get('active_ids')
    employee_ids = fields.Many2many(
        comodel_name='hr.employee',
        relation='hr_employee_mass_edit_rel',
        string='Employees',
        default=_default_employee_ids
    )

    job_id = fields.Many2one(
        comodel_name='hr.job',
        string='Job'
    )
    job_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Job:', default=False, readonly=False, required=False
    )

    department_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department'
    )
    department_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Department:', default=False, readonly=False, required=False
    )

    global_tag_ids = fields.Many2many(
        comodel_name='clv.global_tag',
        relation='hr_employee_mass_edit_global_tag_rel',
        column1='employee_id',
        column2='global_tag_id',
        string='Global Tags'
    )
    global_tag_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Global Tags:', default=False, readonly=False, required=False
    )

    phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Phase'
    )
    phase_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Phase:', default=False, readonly=False, required=False
    )

    active_log = fields.Boolean(
        string='Active Log'
    )
    active_log_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Active Log:', default=False, readonly=False, required=False
    )

    def do_employee_mass_edit(self):
        self.ensure_one()

        for employee in self.employee_ids:

            _logger.info(u'%s %s', '>>>>>', employee.name)

            if self.job_id_selection == 'set':
                employee.job_id = self.job_id.id
            if self.job_id_selection == 'remove':
                employee.job_id = False

            if self.department_id_selection == 'set':
                employee.department_id = self.department_id.id
            if self.department_id_selection == 'remove':
                employee.department_id = False

            if self.global_tag_ids_selection == 'add':
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((4, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                employee.global_tag_ids = m2m_list
            if self.global_tag_ids_selection == 'remove_m2m':
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((3, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                employee.global_tag_ids = m2m_list
            if self.global_tag_ids_selection == 'set':
                m2m_list = []
                for global_tag_id in employee.global_tag_ids:
                    m2m_list.append((3, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                employee.global_tag_ids = m2m_list
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((4, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                employee.global_tag_ids = m2m_list

            if self.phase_id_selection == 'set':
                employee.phase_id = self.phase_id
            if self.phase_id_selection == 'remove':
                employee.phase_id = False

            if self.active_log_selection == 'set':
                employee.active_log = self.active_log
            if self.active_log_selection == 'remove':
                employee.active_log = False

        return True
