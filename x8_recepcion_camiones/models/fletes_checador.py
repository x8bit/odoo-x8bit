from openerp import models, fields, api

class ResUsers(models.Model):
	_inherit = 'res.users'

	checar_en_project_id = fields.Many2one("project.project", string="Proyecto en el que checa")

class ProyectoChecador(models.Model):
	_inherit = 'project.project'

	#fields
	checadores = fields.One2many("res.users", "checar_en_project_id", string="Checadores del proyecto")