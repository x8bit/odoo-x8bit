from openerp import models, fields, api
# import logging

class project_task_cant(models.Model):
	#_name = 'hr.employee'
	_inherit = 'project.task'

	#fields
	c_planificada = fields.Integer(string="Cantidad planificada")
	c_realizada = fields.Integer(string="Cantidad realizada")
	u_medida = fields.Many2one('product.uom',string="Unidad de medida",domain=[('category_id', '=', 'Volumen')])