# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    type = fields.Selection(selection_add=[
        ('clv.address_aux', 'Address (Aux)'),
    ])
    address_aux_ids = fields.One2many(
        string='Related Addresses (Aux)',
        comodel_name='clv.address_aux',
        compute='_compute_address_aux_ids_and_count',
    )
    count_addresses_aux = fields.Integer(
        compute='_compute_address_aux_ids_and_count',
    )

    def _get_clv_entity(self):
        self.ensure_one()
        if self.type and self.type[:3] == 'clv':
            return self.env[self.type].search([
                ('partner_id', '=', self.id),
            ])

    def _compute_address_aux_ids_and_count(self):
        for record in self:
            try:
                address_auxs = self.env['clv.address_aux'].search([
                    ('partner_id', 'child_of', record.id),
                ])
                record.count_addresses_aux = len(address_auxs)
                record.address_aux_ids = [(6, 0, address_auxs.ids)]
            except TypeError:
                record.count_addresses_aux = False
                record.address_aux_ids = False
