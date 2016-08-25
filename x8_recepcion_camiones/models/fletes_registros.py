from openerp import models, fields, api, _

class FleteRegistro(models.Model):
	_name = 'x8.flete.registro'

	@api.onchange('material_id')
	def _onchange_material(self):
		if self.material_id:
			self.project_id = self.material_id.project_id

	@api.model
	def create(self, vals):
		if vals.get('name', 'New') == 'New':
			vals['name'] = self.env['ir.sequence'].next_by_code('x8.flete.registro') or 'New'

		result = super(FleteRegistro, self).create(vals)
		return result

	name = fields.Char(string='Receipt Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
	vehicle_id = fields.Many2one('x8.flete.vehicle', string="Camion", required=True)
	material_id = fields.Many2one('x8.flete.material', string="Material", required=True)
	folio = fields.Char(string="Folio", required=True)
	description = fields.Text(string="Notas")
	zona_id = fields.Many2one('x8.flete.zona', string="Zona", required=True)
	project_id = fields.Many2one("project.project", string="Proyecto", readonly=True)