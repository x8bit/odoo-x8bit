from openerp import models, fields, api
# import logging

class project_project_percentage(models.Model):
	#_name = 'hr.employee'
	_inherit = 'project.project'

	#fields
	porcentaje = fields.integer(string="Porcentaje de avance")