# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AbstractCodePool(models.AbstractModel):
    _description = 'Abstract CodePool'
    _name = 'clv.abstract.code_pool'
    _rec_name = 'code'
    _order = 'code'

    code = fields.Char(string='Code', required=False)

    pool_instance_id = fields.Many2one(
        comodel_name='clv.pool.instance',
        string='Pool Instance',
        ondelete='restrict'
    )

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('code_uniq',
         'UNIQUE (code)',
         'Error! The Code must be unique!'),
    ]
