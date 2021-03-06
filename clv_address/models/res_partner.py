# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[
        ('clv.address', 'Address'),
    ])

    address_ids = fields.One2many(
        string='Related Addresses',
        comodel_name='clv.address',
        compute='_compute_address_ids_and_count',
    )
    count_addresses = fields.Integer(
        compute='_compute_address_ids_and_count',
    )

    def _get_clv_entity(self):
        self.ensure_one()
        if self.type and self.type[:3] == 'clv':
            return self.env[self.type].search([
                ('partner_id', '=', self.id),
            ])

    def _compute_address_ids_and_count(self):
        for record in self:
            try:
                addresses = self.env['clv.address'].search([
                    ('partner_id', 'child_of', record.id),
                ])
                record.count_addresses = len(addresses)
                record.address_ids = [(6, 0, addresses.ids)]
            except TypeError:
                record.count_addresses = False
                record.address_ids = False
