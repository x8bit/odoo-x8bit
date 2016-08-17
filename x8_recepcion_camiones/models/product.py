from openerp import models, fields
from openerp.tools.translate import _

class product_template(models.Model):
    _inherit = 'product.template'

    def _get_product_template_type(self, cr, uid, context=None):
        res = super(product_template, self)._get_product_template_type(cr, uid, context=context)
        if 'product' not in [item[0] for item in res]:
            res.append(('product', _('Stockable Product')))
        return res