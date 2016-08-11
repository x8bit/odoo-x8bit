from openerp import models, fields, api
# import logging

class project_task_percentage(models.Model):
	#_name = 'hr.employee'
	_inherit = 'project.task'

	#fields
	porcentaje = fields.Integer(string="Porcentaje de avance")