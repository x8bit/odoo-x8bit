from openerp import models, fields

class TaxISR(models.Model):
    _name = 'hr.tables.isr.line'

    limite_inferior = fields.Float(string="Limite inferior", required=True)
    limite_superior = fields.Float(string="Limite superior", required=True)
    cuota_fija = fields.Float(string="Cuota fija", required=True)
    porcentaje_sobre_excedente = fields.Float(string="Porcentaje sobre el excedente", required=True)