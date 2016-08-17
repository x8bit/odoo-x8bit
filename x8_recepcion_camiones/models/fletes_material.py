from openerp import models, fields, api

class FleteMaterial(models.Model):
	_name = 'x8.flete.material'

	@api.onchange('product_id')
	def _onchange_product(self):
		if self.product_id:
			self.precio = self.product_id.standard_price or 0.00

	@api.onchange('project_id')
	def _onchange_product(self):
		if self.project_id:
			self.zonas = []

	name = fields.Char(string="Nombre del material", required=True)
	product_id = fields.Many2one("product.template", string="Producto", required=True, domain=[('type', '=', 'product')])
	banco = fields.Char(string="Banco", required=True)
	distancia = fields.Integer(string="Distancia", required=True)
	precio = fields.Integer(string="Precio", required=True)
	precio_flete = fields.Integer(string="Costo flete", required=True)
	proveedor = fields.Many2one("res.partner", string="Proveedor")
	project_id = fields.Many2one("project.project", string="Proyecto", required=True)
	zonas = fields.Many2many("x8.flete.zona","zona_project_rel", "project_id", string="Zonas en las que esta disponible")

