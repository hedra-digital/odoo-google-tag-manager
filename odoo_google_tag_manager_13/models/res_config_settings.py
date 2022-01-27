from odoo import api, fields, models, _


class HdResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    @api.depends("website_id")
    def hd_has_google_tag_manager(self):
        self.hd_has_google_tag_manager = bool(self.hd_google_tag_manager_key)

    def hd_inverse_has_google_tag_manager(self):
        if not self.hd_has_google_tag_manager:
            self.hd_google_tag_manager_key = False

    hd_has_google_tag_manager = fields.Boolean(
        "Google Tag Manager",
        compute=hd_has_google_tag_manager,
        inverse=hd_inverse_has_google_tag_manager,
    )
    hd_google_tag_manager_key = fields.Char(
        "Google Tag Manager Key",
        help="Container ID",
        related="website_id.hd_google_tag_manager_key",
        readonly=False,
    )
