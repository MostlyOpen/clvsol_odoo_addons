# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentTypeItemSetUp(models.TransientModel):
    _description = 'Document Type Items Setup'
    _name = 'clv.document.type.items_setup'

    def _default_document_type_ids(self):
        return self._context.get('active_ids')
    document_type_ids = fields.Many2many(
        comodel_name='clv.document.type',
        relation='clv_document_type_items_setup_rel',
        string='Document Types',
        default=_default_document_type_ids
    )

    def do_document_type_items_setup(self):
        self.ensure_one()

        return True
