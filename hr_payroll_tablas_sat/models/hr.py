# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Odoo, Open Source Management Solution
#
#    Author: Andrius Laukavičius. Copyright: JSC NOD Baltic
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################
from openerp import models, api
import logging
_logger = logging.getLogger(__name__)

class hr_employee(models.Model):
	_inherit = 'hr.employee'

	@api.model
	def getISPT(self, contract):
		#_logger.info("----------> getISPT")
		ispt_table = self.env['hr.tables.isr.line']
		subsidio_table = self.env['hr.tables.subsidio.line']
		sueldo_mes = contract.wage * 30

		r = ispt_table.search([('limite_inferior', '<=', sueldo_mes), ('limite_superior', '>=', sueldo_mes)])[0]
		s = subsidio_table.search([('limite_inferior', '<=', sueldo_mes), ('limite_superior', '>=', sueldo_mes)])[0]

		impuesto_mes = (((sueldo_mes - r.limite_inferior) * r.porcentaje_sobre_excedente / 100) + r.cuota_fija) - s.subsidio
		if impuesto_mes < 0:
			impuesto_mes = 0 

		if contract.schedule_pay == "bi-weekly":
			return impuesto_mes / 2
		elif contract.schedule_pay == "monthly":
			return impuesto_mes
		elif contract.schedule_pay == "weekly":
			return impuesto_mes / 4
		else:
			return impuesto_mes

	@api.model
	def getIMSS(self, contract):
		company = self.env.user.company_id
		dias = 15 # traer cuantos dias tiene el mes de la nomina que se esta generando y dividir entre 2
		a1 = (contract.wage - (company.salario_minimo * 3)) * 0.00400 * dias
		a2 = contract.wage * 0.00375 * dias
		a3 = contract.wage * 0.00250 * dias
		a4 = contract.wage * 0.00625 * dias
		a5 = contract.wage * 0.01125 * dias # este se paga bimestralmente
		return a1 + a2 + a3 + a4 + a5


