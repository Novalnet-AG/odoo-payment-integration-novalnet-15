# Part of Odoo. See LICENSE file for full copyright and licensing details.

from werkzeug import urls

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import float_compare

from odoo.addons.payment import utils as payment_utils


class PaymentLinkWizard(models.TransientModel):
    _inherit = 'payment.link.wizard'
    _description = "Novalnet generate Payment Link"

    available_novalnet_payment_method_ids = fields.Many2many('novalnet.payment.method', string='Novalnet payment methods')

    hide_novalnet_payment_methods = fields.Boolean(default=True)

    @api.onchange('payment_acquirer_selection')
    def _on_change_payment_acquirer_selection(self):

        if self.payment_acquirer_selection  and self.payment_acquirer_selection!='all' and self.env['payment.acquirer'].sudo().search([('id','=',self.payment_acquirer_selection)]).provider == 'novalnet':
            self.hide_novalnet_payment_methods = False
        else:
            self.hide_novalnet_payment_methods = True


    @api.onchange('available_novalnet_payment_method_ids')
    def _on_change_available_novalnet_payment_method_ids(self):
        self._generate_link()


    def _generate_link(self):
        for payment_link in self:
            if  self.payment_acquirer_selection  and self.payment_acquirer_selection!='all'  and self.env['payment.acquirer'].sudo().search([('id','=',self.payment_acquirer_selection)]).provider == 'novalnet':
                related_document = self.env[payment_link.res_model].browse(payment_link.res_id)
                base_url = related_document.get_base_url()  # Don't generate links for the wrong website
                # payment_methods= ', '.join(str(payment_link.available_novalnet_payment_method_ids._origin.mapped('id')))
                payment_methods= ','.join(str(npm._origin.id) for npm in payment_link.available_novalnet_payment_method_ids)
                payment_link.link = f'{base_url}/payment/pay' \
                       f'?reference={urls.url_quote(payment_link.description)}' \
                       f'&amount={payment_link.amount}' \
                       f'&currency_id={payment_link.currency_id.id}' \
                       f'&partner_id={payment_link.partner_id.id}' \
                       f'&company_id={payment_link.company_id.id}' \
                       f'&invoice_id={payment_link.res_id}' \
                       f'{"&acquirer_id=" + str(payment_link.payment_acquirer_selection) if payment_link.payment_acquirer_selection != "all" else "" }' \
                       f'&access_token={payment_link.access_token}' \
                       f'&payment_types={payment_methods}'
            else:
                super(PaymentLinkWizard, payment_link)._generate_link()
