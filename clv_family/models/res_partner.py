# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[
        ('clv.family', 'Family'),
    ])

    family_ids = fields.One2many(
        string='Related Families',
        comodel_name='clv.family',
        compute='_compute_family_ids_and_count',
    )
    count_families = fields.Integer(
        compute='_compute_family_ids_and_count',
    )

    def _get_clv_entity(self):
        self.ensure_one()
        if self.type and self.type[:3] == 'clv':
            return self.env[self.type].search([
                ('partner_id', '=', self.id),
            ])

    def _compute_family_ids_and_count(self):
        for record in self:
            try:
                families = self.env['clv.family'].search([
                    ('partner_id', 'child_of', record.id),
                ])
                record.count_families = len(families)
                record.family_ids = [(6, 0, families.ids)]
            except TypeError:
                record.count_families = False
                record.family_ids = False
