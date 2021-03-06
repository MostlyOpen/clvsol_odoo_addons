# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DocumentItemsUpdateFromSurvey(models.TransientModel):
    _description = 'Document Items Update from Survey'
    _name = 'clv.document.items_updt_from_survey'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_items_updt_from_survey_rel',
        string='Documents',
        default=_default_document_ids
    )

    def do_document_items_updt_from_survey(self):
        self.ensure_one()

        for document in self.document_ids:

            _logger.info(u'%s %s %s', '>>>>>', document.code, document.document_type_id.name)

            if document.survey_user_input_id.id is not False:

                for item in document.item_ids:

                    _logger.info(u'%s %s', '>>>>>>>>>>', item.code)

                    if item.code is not False:

                        item.value = document.survey_user_input_id.get_value(item.code)

        return True
