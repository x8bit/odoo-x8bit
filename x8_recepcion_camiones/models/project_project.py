from openerp import models, fields

class ProjectProject(models.Model):
	_inherit = 'project.project'

	zonas = fields.One2many("x8.flete.zona", "project_id", string="Zonas del proyecto")