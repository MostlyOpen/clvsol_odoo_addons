# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LabTestReport(models.Model):
    _inherit = 'clv.lab_test.report'

    reg_state = fields.Selection(
        [('draft', 'Draft'),
         ('revised', 'Revised'),
         ('done', 'Done'),
         ('cancelled', 'Cancelled')
         ], string='Register State', readonly=True
    )

    def action_draft(self):
        pass

    def action_revised(self):
        pass

    def action_done(self):
        pass

    def action_cancel(self):
        pass
