# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Website(models.Model):
    _inherit = 'website'

    hd_has_google_tag_manager = fields.Boolean("Google Tag Manager")
    hd_google_tag_manager_key = fields.Char("Google Tag Manager Key", help='GTM Container ID')
