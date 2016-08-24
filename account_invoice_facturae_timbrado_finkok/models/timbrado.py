# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class account_invoice(models.Model):
	_inherit = 'account.invoice'

	def timbrar(self, xml_base64):
		raise UserError("Hola mundo")