# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LabTestResult(models.Model):
    _inherit = 'clv.lab_test.report'

    state = fields.Selection(
        [('new', 'New'),
         ('available', 'Available'),
         ('approved', 'Approved'),
         ('discarded', 'Discarded')
         ], string='Report State', readonly=True,
    )

    def action_new(self):
        pass

    def action_available(self):
        pass

    def action_approve(self):
        pass

    def action_discard(self):
        pass
