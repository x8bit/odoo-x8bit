from openerp import models, fields

class AccountAgedTrialBalanceX8(models.Model):
	_name = 'account.aged.trial.balance'
    _inherit = 'account.aged.trial.balance'

    #limite_inferior = fields.Float(string="Limite inferior", required=True)
    #limite_superior = fields.Float(string="Limite superior", required=True)
    #cuota_fija = fields.Float(string="Cuota fija", required=True)
    #porcentaje_sobre_excedente = fields.Float(string="Porcentaje sobre el excedente", required=True)