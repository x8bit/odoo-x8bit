from openerp import models, fields, api

class FleteVehiculo(models.Model):
    _name = 'x8.flete.registro'

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('x8.flete.registro') or 'New'

    name = fields.Char(string='Receipt Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    vehicle_id = fields.Many2one('x8.flete.vehicle', string="Camión", required=True)
    material_id = fields.Many2one('x8.flete.material', string="Material", required=True)
	folio = fields.Char(string="Folio", required=True)
    description = fields.Text(string="Notas")
