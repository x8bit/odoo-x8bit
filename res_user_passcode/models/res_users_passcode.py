from openerp import models, fields, api
# import logging

class res_users_passcode(models.Model):
	#_name = 'hr.employee'
	_inherit = 'res.users'

	#fields
	passcode = fields.Integer(string="Codigo",size=4)