# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# import logging

# from odoo import api, fields, models
from odoo import models

# _logger = logging.getLogger(__name__)


class LabTestReportMassEdit(models.TransientModel):
    _description = 'Lab Test Report Mass Edit'
    _name = 'clv.lab_test.report.mass_edit'

    # def _default_lab_test_report_ids(self):
    #     return self._context.get('active_ids')
    # lab_test_report_ids = fields.Many2many(
    #     comodel_name='clv.lab_test.report',
    #     relation='clv_lab_test_report_mass_edit_rel',
    #     string='Lab Test Reports',
    #     default=_default_lab_test_report_ids
    # )

    # date_report = fields.Date(string='Date of the Report', default=False, readonly=False, required=False)
    # date_report_selection = fields.Selection(
    #     [('set', 'Set'),
    #      ('remove', 'Remove'),
    #      ], string='Date of the Report:', default=False, readonly=False, required=False
    # )

    # phase_id = fields.Many2one(
    #     comodel_name='clv.phase',
    #     string='Phase'
    # )
    # phase_id_selection = fields.Selection(
    #     [('set', 'Set'),
    #      ('remove', 'Remove'),
    #      ], string='Phase:', default=False, readonly=False, required=False
    # )

    # @api.model
    # def referenceable_models(self):
    #     return [(ref.model, ref.name) for ref in self.env['clv.referenceable.model'].search([
    #         ('base_model', '=', 'clv.lab_test.report'),
    #     ])]

    # ref_id = fields.Reference(
    #     selection='referenceable_models',
    #     string='Refers to')
    # ref_id_selection = fields.Selection(
    #     [('set', 'Set'),
    #      ('remove', 'Remove'),
    #      ], string='Refers to:', default=False, readonly=False, required=False
    # )

    # def do_lab_test_report_mass_edit(self):
    #     self.ensure_one()

    #     for lab_test_report in self.lab_test_report_ids:

    #         _logger.info(u'%s %s', '>>>>>', lab_test_report.code)

    #         if self.date_report_selection == 'set':
    #             lab_test_report.date_report = self.date_report
    #         if self.date_report_selection == 'remove':
    #             lab_test_report.date_report = False

    #         if self.phase_id_selection == 'set':
    #             lab_test_report.phase_id = self.phase_id
    #         if self.phase_id_selection == 'remove':
    #             lab_test_report.phase_id = False

    #         if self.ref_id_selection == 'set':
    #             lab_test_report.ref_id = self.ref_id
    #         if self.ref_id_selection == 'remove':
    #             lab_test_report.ref_id = False

    #     return True
