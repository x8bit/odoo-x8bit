# -*- encoding:utf-8 -*-

from openerp import models, fields, api
class x8_contacto(models.Model):
	_inherit = 'res.partner'

	@api.onchange('rfc')
	def _onchange_rfc(self):
		if self.rfc:
			self.vat = "MX%s" % (self.rfc or '')
		else:
			self.vat = ''

	rfc = fields.Char(string="RFC", default="")
	nombre_comercial = fields.Char(string="Nombre comercial")