
from openerp import models, fields, api
# import logging

class project_task_percentage(models.Model):
	#_name = 'hr.employee'
	_inherit = 'project.task'
	@api.onchange('c_planificada','c_realizada')
	def _onchange_porcentaje(self):
		if self.c_planificada and self.c_realizada:
			self.porcentaje = self.c_realizada/float(self.c_planificada)*100

	#fields
	porcentaje = fields.Integer(string="Porcentaje de avance",readonly=True)