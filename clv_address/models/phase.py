# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Phase(models.Model):
    _inherit = 'clv.phase'

    address_ids = fields.One2many(
        comodel_name='clv.address',
        inverse_name='phase_id',
        string='Addresses',
        readonly=True
    )
    count_addresses = fields.Integer(
        string='Addresses (count)',
        compute='_compute_address_ids_and_count',
    )

    def _compute_address_ids_and_count(self):
        for record in self:

            search_domain = [
                ('phase_id', '=', record.id),
            ]

            addresses = self.env['clv.address'].search(search_domain)

            record.count_addresses = len(addresses)
            record.address_ids = [(6, 0, addresses.ids)]


class Address(models.Model):
    _inherit = 'clv.address'

    phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Phase',
        ondelete='restrict'
    )
