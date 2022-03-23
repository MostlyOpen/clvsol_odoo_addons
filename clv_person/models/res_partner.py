# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[
        ('clv.person', 'Person'),
    ])

    person_ids = fields.One2many(
        string='Related Persons',
        comodel_name='clv.person',
        compute='_compute_person_ids_and_count',
    )
    count_persons = fields.Integer(
        compute='_compute_person_ids_and_count',
    )

    def _get_clv_entity(self):
        self.ensure_one()
        if self.type and self.type[:3] == 'clv':
            return self.env[self.type].search([
                ('partner_id', '=', self.id),
            ])

    def _compute_person_ids_and_count(self):
        for record in self:
            try:
                persons = self.env['clv.person'].search([
                    ('partner_id', 'child_of', record.id),
                ])
                record.count_persons = len(persons)
                record.person_ids = [(6, 0, persons.ids)]
            except TypeError:
                record.count_persons = False
                record.person_ids = False
