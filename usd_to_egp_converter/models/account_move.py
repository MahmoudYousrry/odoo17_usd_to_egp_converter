from odoo import models, fields, api
from odoo.exceptions import UserError
from .currency_api import get_usd_to_egp_rate

class AccountMove(models.Model):
    _inherit = 'account.move'

    egp_total = fields.Float(string="Total in EGP", compute="_compute_egp_total", store=False)

    @api.depends('amount_total')
    def _compute_egp_total(self):
        rate = get_usd_to_egp_rate()
        if rate is None:
            raise UserError("Unable to fetch exchange rate from API.")
        for move in self:
            move.egp_total = move.amount_total * rate
