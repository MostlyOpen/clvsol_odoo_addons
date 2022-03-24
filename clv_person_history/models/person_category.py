# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PersonCategory(models.Model):
    _inherit = 'clv.person.category'

    person_history_ids = fields.Many2many(
        comodel_name='clv.person.history',
        relation='clv_person_history_category_rel',
        column1='category_id',
        column2='person_history_id',
        string='Persons (History)'
    )


class PersonHistory(models.Model):
    _inherit = "clv.person.history"

    category_ids = fields.Many2many(
        comodel_name='clv.person.category',
        relation='clv_person_history_category_rel',
        column1='person_history_id',
        column2='category_id',
        string='Categories'
    )
    category_names = fields.Char(
        string='Category Names',
        compute='_compute_category_names',
        store=True
    )

    @api.depends('category_ids')
    def _compute_category_names(self):
        for r in self:
            category_names = False
            for category in r.category_ids:
                if category_names is False:
                    category_names = category.name
                else:
                    category_names = category_names + ', ' + category.name
            r.category_names = category_names
