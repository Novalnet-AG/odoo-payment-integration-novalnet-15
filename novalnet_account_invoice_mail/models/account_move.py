from werkzeug import urls
from odoo.http import request
from odoo import _, fields, models, service
from odoo.exceptions import UserError, ValidationError
from odoo.tools import format_amount

from odoo.addons.payment import utils as payment_utils



class PaymentTransaction(models.Model):
    _inherit = 'account.move'

    is_payment_link_in_invoice = fields.Boolean(string='Is payment Link included in invoice',default=True)

    def _get_access_token(self):
        self.ensure_one()
        return payment_utils.generate_access_token(
            self.partner_id.id, self.amount_total, self.currency_id.id
        )

    def _generate_payment_link(self):
        for inv in self:
            base_url = inv.get_base_url()  # Don't generate links for the wrong website
            url_params = {
                'reference': urls.url_quote(inv.name),
                'amount': self.amount_total,
                'access_token': self._get_access_token(),
                'invoice_id': self.id,
                'partner_id': self.partner_id.id,
                'currency_id': self.currency_id.id,
            }
            return f'{base_url}/payment/pay?{urls.url_encode(url_params)}'
