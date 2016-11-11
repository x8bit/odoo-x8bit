# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import UserError
import requests
import base64
from lxml import etree as ET

import logging
_logger = logging.getLogger(__name__)

class account_invoice(models.Model):
	_inherit = 'account.invoice'

	def timbrar(self, xml_base64):
		xml_str = base64.b64decode(xml_base64)
		url = 'https://staging.diverza.com/stamp/complete'
		headers = {"x-auth-token": "ABCD1234"}
		r = requests.post(url, headers=headers, data=xml_str)
		if r.status_code == requests.codes.ok:
			_logger.info("r.text")
			_logger.info(r.text)
			#xml,UUID,fecha,sello,certificado

			return r.text.encode("utf-8"),"UUID","fec_emision","sello_sat","certificado"
		else:
			raise UserError("Error al timbrar con diverza")