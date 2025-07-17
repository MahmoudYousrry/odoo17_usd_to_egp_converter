from odoo import models, fields, api
from odoo.exceptions import UserError
from .currency_api import get_usd_to_egp_rate

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    egp_total = fields.Float(string="Total in EGP", compute="_compute_egp_total", store=False)

    @api.depends('amount_total')
    def _compute_egp_total(self):
        rate = get_usd_to_egp_rate()
        if rate is None:
            raise UserError("Unable to fetch exchange rate from API.")
        for order in self:
            order.egp_total = order.amount_total * rate
