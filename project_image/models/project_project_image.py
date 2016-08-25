from openerp import models, fields, api
# import logging

class project_project_image(models.Model):
	#_name = 'hr.employee'
	_inherit = 'project.project'

	#fields
	imagen = fields.Binary(string="Imagen del mapa", attachment=True)