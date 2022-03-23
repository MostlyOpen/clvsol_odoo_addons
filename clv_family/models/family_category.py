# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class FamilyCategory(models.Model):
    _description = 'Family Category'
    _name = 'clv.family.category'
    _inherit = 'clv.abstract.category'

    code = fields.Char(string='Category Code', required=False)

    family_ids = fields.Many2many(
        comodel_name='clv.family',
        relation='clv_family_category_rel',
        column1='category_id',
        column2='family_id',
        string='Families'
    )


class Family(models.Model):
    _inherit = "clv.family"

    category_ids = fields.Many2many(
        comodel_name='clv.family.category',
        relation='clv_family_category_rel',
        column1='family_id',
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
