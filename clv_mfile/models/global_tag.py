# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class GlobalTag(models.Model):
    _inherit = 'clv.global_tag'

    mfile_ids = fields.Many2many(
        comodel_name='clv.mfile',
        relation='clv_mfile_global_tag_rel',
        column1='global_tag_id',
        column2='mfile_id',
        string='Media Files'
    )


class MediaFile(models.Model):
    _inherit = 'clv.mfile'

    global_tag_ids = fields.Many2many(
        comodel_name='clv.global_tag',
        relation='clv_mfile_global_tag_rel',
        column1='mfile_id',
        column2='global_tag_id',
        string='Global Tags'
    )
    global_tag_names = fields.Char(
        string='Global Tag Names',
        compute='_compute_global_tag_names',
        store=True
    )
    global_tag_names_suport = fields.Char(
        string='Global Tag Names Suport',
        compute='_compute_global_tag_names_suport',
        store=False
    )

    @api.depends('global_tag_ids')
    def _compute_global_tag_names(self):
        for r in self:
            r.global_tag_names = r.global_tag_names_suport

    def _compute_global_tag_names_suport(self):
        for r in self:
            global_tag_names = False
            for global_tag in r.global_tag_ids:
                if global_tag_names is False:
                    global_tag_names = global_tag.name
                else:
                    global_tag_names = global_tag_names + ', ' + global_tag.name
            r.global_tag_names_suport = global_tag_names
            if r.global_tag_names != global_tag_names:
                record = self.env['clv.mfile'].search([('id', '=', r.id)])
                record.write({'global_tag_ids': r.global_tag_ids})
