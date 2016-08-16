from openerp import models, fields

class FleteVehiculo(models.Model):
    _name = 'x8.flete.vehicle'

    name = fields.Char(string="Numero de placas", size = 8)
    chofer = fields.Char(string="Nombre del chofer")
    num_econ = fields.Integer(string="Numero economico")
    description = fields.Text(string="Descripcion del vehiculo")
    capacidad = fields.Float(string="Capacidad de carga en m3", required=True)
    proyect_id = fields.Many2one("project.project", string="Proyecto")