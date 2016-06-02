from openerp import models, fields

class SubsidioNomina(models.Model):
    _name = 'hr.tables.subsidio.line'

    limite_inferior = fields.Float(string="Limite inferior", required=True)
    limite_superior = fields.Float(string="Limite superior", required=True)
    subsidio = fields.Float(string="Subsidio", required=True)