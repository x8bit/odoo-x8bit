from openerp import models, fields

class FleteVehiculo(models.Model):
    _name = 'x8.flete.vehicle'

    name = fields.Char(string="Numero de placas", size = 8, required=True)
    chofer = fields.Char(string="Nombre del chofer", required=True)
    num_econ = fields.Integer(string="Numero economico", required=True)
    description = fields.Text(string="Descripcion del vehiculo")
    capacidad = fields.Float(string="Capacidad de carga en m3", required=True)
    project_id = fields.Many2one("project.project", string="Proyecto", required=True)