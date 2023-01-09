# Part of Odoo. See LICENSE file for full copyright and licensing details.

import urllib.parse
import werkzeug
import logging

from odoo import _, http
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.fields import Command
from odoo.http import request

from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment.controllers import portal
_logger = logging.getLogger(__name__)

class NovalnetPaymentPortal(portal.PaymentPortal):

    def _get_custom_rendering_context_values(self, **kwargs):
        """ Return a dict of additional rendering context values.

        :param dict kwargs: Optional data. This parameter is not used here
        :return: The dict of additional rendering context values
        :rtype: dict
        """

        rendering_context_values = super()._get_custom_rendering_context_values(**kwargs)

        if 'payment_types' in kwargs and kwargs['payment_types']:
            novalnet_payment_types = kwargs['payment_types'].split(',')
            rendering_context_values['novalnet_payment_types']= novalnet_payment_types
        return rendering_context_values
