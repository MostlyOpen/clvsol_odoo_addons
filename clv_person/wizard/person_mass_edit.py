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

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PersonMassEdit(models.TransientModel):
    _description = 'Person Mass Edit'
    _name = 'clv.person.mass_edit'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_mass_edit_rel',
        string='Persons',
        default=_default_person_ids
    )

    reg_state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('done', 'Done'),
         ('canceled', 'Canceled')
         ], string='Register State', default=False, readonly=False, required=False
    )
    reg_state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='Register State:', default=False, readonly=False, required=False
    )

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('waiting', 'Waiting'),
         ('selected', 'Selected'),
         ('unselected', 'Unselected'),
         ('unavailable', 'Unavailable'),
         ('unknown', 'Unknown')
         ], string='State', default=False, readonly=False, required=False
    )
    state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='State:', default=False, readonly=False, required=False
    )

    global_tag_ids = fields.Many2many(
        comodel_name='clv.global_tag',
        relation='clv_person_mass_edit_global_tag_rel',
        column1='person_id',
        column2='global_tag_id',
        string='Global Tags'
    )
    global_tag_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Global Tags:', default=False, readonly=False, required=False
    )

    category_ids = fields.Many2many(
        comodel_name='clv.person.category',
        relation='clv_person_mass_edit_category_rel',
        column1='person_id',
        column2='category_id',
        string='Categories'
    )
    category_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Categories:', default=False, readonly=False, required=False
    )

    marker_ids = fields.Many2many(
        comodel_name='clv.person.marker',
        relation='clv_person_mass_edit_marker_rel',
        column1='person_id',
        column2='marker_id',
        string='Markers'
    )
    marker_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Markers:', default=False, readonly=False, required=False
    )

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsible Empĺoyee'
    )
    employee_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Responsible Empĺoyee:', default=False, readonly=False, required=False
    )
    get_employee_id = fields.Boolean(
        string='Get Responsible Empĺoyee'
    )

    random_field = fields.Char(
        string='Random ID', default=False,
        help='Use "/" to get an automatic new Random ID.'
    )
    random_field_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Random ID:', default=False, readonly=False, required=False
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

    tag_ids = fields.Many2many(
        comodel_name='clv.person.tag',
        relation='clv_person_mass_edit_tag_rel',
        column1='person_id',
        column2='tag_id',
        string='Person Tag'
    )
    tag_ids_selection = fields.Selection(
        [('add', 'Add'),
         ('remove_m2m', 'Remove'),
         ('set', 'Set'),
         ], string='Person Tag:', default=False, readonly=False, required=False
    )

    partner_entity_code_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Partner Entity Code:', default=False, readonly=False, required=False
    )

    person_ref_age_refresh = fields.Boolean(
        string='Person Reference Age Refresh'
    )

    active_log = fields.Boolean(
        string='Active Log'
    )
    active_log_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Active Log:', default=False, readonly=False, required=False
    )

    @api.model
    def default_get(self, field_names):

        defaults = super().default_get(field_names)

        return defaults

    def do_person_mass_edit(self):
        self.ensure_one()

        for person in self.person_ids:

            _logger.info(u'%s %s', '>>>>>', person.name)

            if self.reg_state_selection == 'set':
                person.reg_state = self.reg_state
            if self.reg_state_selection == 'remove':
                person.reg_state = False

            if self.state_selection == 'set':
                person.state = self.state
            if self.state_selection == 'remove':
                person.state = False

            if self.global_tag_ids_selection == 'add':
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((4, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.global_tag_ids = m2m_list
            if self.global_tag_ids_selection == 'remove_m2m':
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((3, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.global_tag_ids = m2m_list
            if self.global_tag_ids_selection == 'set':
                m2m_list = []
                for global_tag_id in person.global_tag_ids:
                    m2m_list.append((3, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.global_tag_ids = m2m_list
                m2m_list = []
                for global_tag_id in self.global_tag_ids:
                    m2m_list.append((4, global_tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.global_tag_ids = m2m_list

            if self.category_ids_selection == 'add':
                m2m_list = []
                for category_id in self.category_ids:
                    m2m_list.append((4, category_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.category_ids = m2m_list
            if self.category_ids_selection == 'remove_m2m':
                m2m_list = []
                for category_id in self.category_ids:
                    m2m_list.append((3, category_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.category_ids = m2m_list
            if self.category_ids_selection == 'set':
                m2m_list = []
                for category_id in person.category_ids:
                    m2m_list.append((3, category_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.category_ids = m2m_list
                m2m_list = []
                for category_id in self.category_ids:
                    m2m_list.append((4, category_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.category_ids = m2m_list

            if self.marker_ids_selection == 'add':
                m2m_list = []
                for marker_id in self.marker_ids:
                    m2m_list.append((4, marker_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.marker_ids = m2m_list
            if self.marker_ids_selection == 'remove_m2m':
                m2m_list = []
                for marker_id in self.marker_ids:
                    m2m_list.append((3, marker_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.marker_ids = m2m_list
            if self.marker_ids_selection == 'set':
                m2m_list = []
                for marker_id in person.marker_ids:
                    m2m_list.append((3, marker_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.marker_ids = m2m_list
                m2m_list = []
                for marker_id in self.marker_ids:
                    m2m_list.append((4, marker_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.marker_ids = m2m_list

            if self.employee_id_selection == 'set':
                person.employee_id = self.employee_id
            if self.employee_id_selection == 'remove':
                person.employee_id = False

            if self.get_employee_id:
                if person.ref_address_id.employee_id.id is not False:
                    person.employee_id = person.ref_address_id.employee_id.id

            if self.random_field_selection == 'set':
                person.random_field = self.random_field
            if self.random_field_selection == 'remove':
                person.random_field = False

            if self.phase_id_selection == 'set':
                person.phase_id = self.phase_id
            if self.phase_id_selection == 'remove':
                person.phase_id = False

            if self.tag_ids_selection == 'add':
                m2m_list = []
                for tag_id in self.tag_ids:
                    m2m_list.append((4, tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.tag_ids = m2m_list
            if self.tag_ids_selection == 'remove_m2m':
                m2m_list = []
                for tag_id in self.tag_ids:
                    m2m_list.append((3, tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.tag_ids = m2m_list
            if self.tag_ids_selection == 'set':
                m2m_list = []
                for tag_id in person.tag_ids:
                    m2m_list.append((3, tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.tag_ids = m2m_list
                m2m_list = []
                for tag_id in self.tag_ids:
                    m2m_list.append((4, tag_id.id))
                _logger.info(u'%s %s', '>>>>>>>>>>', m2m_list)
                person.tag_ids = m2m_list

            if self.partner_entity_code_selection == 'set':
                if person.entity_code != person.code:
                    vals = {}
                    vals['entity_code'] = person.code
                    person.write(vals)
            if self.partner_entity_code_selection == 'remove':
                if person.entity_code is not False:
                    vals = {}
                    vals['entity_code'] = False
                    person.write(vals)

            if self.person_ref_age_refresh:
                person._compute_age_reference()
                person._compute_age_range_id()

            if self.active_log_selection == 'set':
                person.active_log = self.active_log
            if self.active_log_selection == 'remove':
                person.active_log = False

        return True
