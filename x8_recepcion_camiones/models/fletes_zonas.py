from openerp import models, fields, api

class FleteZonas(models.Model):
	_name = 'x8.flete.zona'

	@api.model
	def create(self, vals):
		if vals.get('name', 'New') == 'New':
			vals['name'] = self.env['ir.sequence'].next_by_code('x8.flete.zona') or 'New'

		result = super(FleteZonas, self).create(vals)
		return result

	name = fields.Char(string='Zona', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
	project_id = fields.Many2one("project.project", string="Proyecto", required=True)
	checadores = fields.One2many("res.users", "checar_en_zone_id", string="Checadores del proyecto")
	description = fields.Text(string='Description')