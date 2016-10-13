# -*- encoding:utf-8 -*-

from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class x8_cuenta(models.Model):
	_inherit = 'res.partner.bank'
	
	@api.onchange('clabe')
	def _onchange_customer(self):
		if self.clabe:
			_logger.info(len(self.clabe))
			if len(self.clabe) == 19 and not self.acc_number:
				self.acc_number = self.clabe