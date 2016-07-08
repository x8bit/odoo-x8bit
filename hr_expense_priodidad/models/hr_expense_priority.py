from openerp import models, fields, api
# import logging

class hr_expense_priority(models.Model):
	#_name = 'hr.employee'
	_inherit = 'hr.expense'

	#fields
	urgente = fields.Boolean(string="Urgente")