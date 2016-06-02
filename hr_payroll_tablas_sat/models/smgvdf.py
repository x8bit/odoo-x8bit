from openerp import models, fields, api

class res_company(models.Model):
	_inherit = 'res.company'

	salario_minimo = fields.Float()
	prima_riesgo = fields.Float()

class SalarioMinimo(models.TransientModel):
	_inherit = 'res.config.settings'
	_name = 'smgvdf.config.settings'

	salario_minimo = fields.Char()
	prima_riesgo = fields.Char()

	@api.model
	def get_default_company_values(self, fields):
		"""
		Method argument "fields" is a list of names
		of all available fields.
		"""
		company = self.env.user.company_id
		return {
			'salario_minimo': company.salario_minimo,
			'prima_riesgo': company.prima_riesgo
		}

	@api.one
	def set_company_values(self):
		company = self.env.user.company_id
		company.salario_minimo = self.salario_minimo
		company.prima_riesgo = self.prima_riesgo