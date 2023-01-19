# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LabTestReport(models.Model):
    _description = 'Lab Test Report'
    _name = "clv.lab_test.report"


class LabTestType(models.Model):
    _inherit = 'clv.lab_test.type'

    lab_test_report_ids = fields.Integer(
        string='Lab Test Reports',
        default=False,
        readonly=True
    )


class LabTestRequest(models.Model):
    _inherit = 'clv.lab_test.request'

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
    count_lab_test_reports_2 = fields.Integer(
        string='Lab Test Reports 2 (count)',
        default=False,
        readonly=True
    )


class LabTestResult(models.Model):
    _inherit = 'clv.lab_test.result'

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
    count_lab_test_reports_2 = fields.Integer(
        string='Lab Test Reports 2 (count)',
        default=False,
        readonly=True
    )
