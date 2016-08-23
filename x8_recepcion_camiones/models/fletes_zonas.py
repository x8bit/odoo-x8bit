from openerp import models, fields, api

class FleteZonas(models.Model):
	_name = 'x8.flete.zona'

	
	
	name = fields.Char(string='Zona', required=True)
	project_id = fields.Many2one("project.project", string="Proyecto", required=True)
	checadores = fields.Many2many("res.users", "checador_zone_rel", "checar_en_zone_id", string="Checadores del proyecto")
	description = fields.Text(string='Description')