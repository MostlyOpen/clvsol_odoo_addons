# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Phase(models.Model):
    _inherit = 'clv.phase'

    lab_test_type_ids = fields.One2many(
        comodel_name='clv.lab_test.type',
        inverse_name='phase_id',
        string='Lab Test Types',
        readonly=True
    )
    count_lab_test_types = fields.Integer(
        string='Lab Test Types (count)',
        compute='_compute_lab_test_type_ids_and_count',
    )

    def _compute_lab_test_type_ids_and_count(self):
        for record in self:

            search_domain = [
                ('phase_id', '=', record.id),
            ]

            lab_test_types = self.env['clv.lab_test.type'].search(search_domain)

            record.count_lab_test_types = len(lab_test_types)
            record.lab_test_type_ids = [(6, 0, lab_test_types.ids)]

    lab_test_request_ids = fields.Integer(
        string='Lab Test Requests',
        default=False,
        readonly=True
    )
    count_lab_test_requests = fields.Integer(
        string='Lab Test Requests (count)',
        default=False,
        readonly=True
    )

    lab_test_result_ids = fields.One2many(
        comodel_name='clv.lab_test.result',
        inverse_name='phase_id',
        string='Lab Test Results',
        readonly=True
    )
    count_lab_test_results = fields.Integer(
        string='Lab Test Results (count)',
        compute='_compute_lab_test_result_ids_and_count',
    )

    def _compute_lab_test_result_ids_and_count(self):
        for record in self:

            search_domain = [
                ('phase_id', '=', record.id),
            ]

            lab_test_results = self.env['clv.lab_test.result'].search(search_domain)

            record.count_lab_test_results = len(lab_test_results)
            record.lab_test_result_ids = [(6, 0, lab_test_results.ids)]

    lab_test_report_ids = fields.Integer(
        string='Lab Test Reports',
        default=False,
        readonly=True
    )
    count_lab_test_reports = fields.Integer(
        string='Lab Test Reports (count)',
        default=False,
        readonly=True
    )


class LabTestType(models.Model):
    _inherit = 'clv.lab_test.type'

    phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Phase',
        ondelete='restrict'
    )


class LabTestResult(models.Model):
    _inherit = 'clv.lab_test.result'

    phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Phase',
        ondelete='restrict'
    )


class LabTestCriterion(models.Model):
    _inherit = 'clv.lab_test.criterion'

    lab_test_type_phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Lab Test Type Phase',
        related='lab_test_type_id.phase_id',
        store=True
    )
    lab_test_result_phase_id = fields.Many2one(
        comodel_name='clv.phase',
        string='Lab Test Result Phase',
        related='lab_test_result_id.phase_id',
        store=True
    )

    # lab_test_report_phase_id = fields.Integer(
    #     string='Lab Test Report Phase',
    #     default=False,
    #     readonly=True
    # )
