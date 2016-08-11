from openerp import models, fields, api
# import logging

class stock_picking_vehicle(models.Model):
	#_name = 'hr.employee'
	_inherit = 'stock.picking'

	#fields
	vehicle = fields.Many2one('fleet.vehicle', string='Vehiculo', help="Vehiculo asignado")