# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AddressCategory(models.Model):
    _inherit = 'clv.address.category'

    address_history_ids = fields.Many2many(
        comodel_name='clv.address.history',
        relation='clv_address_history_category_rel',
        column1='category_id',
        column2='address_history_id',
        string='Addresses (History)'
    )


class AddressHistory(models.Model):
    _inherit = "clv.address.history"

    category_ids = fields.Many2many(
        comodel_name='clv.address.category',
        relation='clv_address_history_category_rel',
        column1='address_history_id',
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
