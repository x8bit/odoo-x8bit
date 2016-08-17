from openerp import models, fields

class ResUsers(models.Model):
	_inherit = 'res.users'

	checar_en_zone_id = fields.Many2one("x8.flete.zona", string="Zona en la que checa")