# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class FamilyContactInformationUpdate(models.TransientModel):
    _description = 'Family Contact Information Update'
    _name = 'clv.family.contact_information_updt'

    def _default_family_ids(self):
        return self._context.get('active_ids')
    family_ids = fields.Many2many(
        comodel_name='clv.family',
        relation='clv_family_contact_information_updt_rel',
        string='Families',
        default=_default_family_ids
    )

    updt_phone = fields.Boolean(string='Update Phone', default=False)
    updt_mobile = fields.Boolean(string='Update Mobile', default=False)
    updt_email = fields.Boolean(string='Update Email', default=False)

    def do_family_contact_information_updt(self):
        self.ensure_one()

        family_count = 0
        for family in self.family_ids:

            family_count += 1

            _logger.info(u'%s %s %s', '>>>>>', family_count, family.name)

            if family.ref_address_id is not False:

                values = {}

                values['street_name'] = family.ref_address_id.street_name
                values['street2'] = family.ref_address_id.street2
                values['country_id'] = family.ref_address_id.country_id.id
                values['state_id'] = family.ref_address_id.state_id.id
                values['city'] = family.ref_address_id.city
                values['zip'] = family.ref_address_id.zip
                if self.updt_phone:
                    values['phone'] = family.ref_address_id.phone
                if self.updt_mobile:
                    values['mobile'] = family.ref_address_id.mobile
                if self.updt_email:
                    values['email'] = family.ref_address_id.email

                _logger.info(u'%s %s %s', '>>>>>>>>>>', 'values:', values)

                family.write(values)

        return True
