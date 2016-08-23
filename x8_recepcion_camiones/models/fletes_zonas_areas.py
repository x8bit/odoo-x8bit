from openerp import models, fields, api

class FleteZonasAreas(models.Model):
	_name = 'x8.flete.zona.areas'

	
	
	name = fields.Char(string='Area', required=True)
	zona_id = fields.Many2one("x8.flete.zona", string="Zona", required=True)
	description = fields.Text(string='Description')