from openerp import models, fields, api
from openerp.tools import config
# import xml.etree.cElementTree as ET
from lxml import etree as ET
import xml.dom.minidom as minidom
# from subprocess import check_output
# import base64, os

import logging
_logger = logging.getLogger(__name__)

class account_invoice(models.Model):
	_inherit = 'account.invoice'

	@api.model
	def genFacturae(self, cr):
		invoice = self.browse(cr)

		namespaces =  {
			'cfdi' : "http://www.sat.gob.mx/cfd/3",
			'xsi' : "http://www.w3.org/2001/XMLSchema-instance",
		}

		root = ET.Element('{%s}Comprobante' % namespaces['cfdi'], nsmap=namespaces)
		root.set("{%s}schemaLocation" % namespaces['xsi'], "http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd")
		root.set("version", "3.2")
		arr = invoice.number.split("-")
		root.set("serie", arr[0])
		root.set("folio", arr[1])
		root.set("formaDePago", "PAGO EN UNA SOLA EXHIBICION")
		root.set("Moneda", "PESO MXN")
		#root.set("Moneda", "DOLAR USD")
		root.set("tipoDeComprobante", "ingreso")

		pay_method_id = invoice.pay_method_id.code
		cta_pago = invoice.acc_payment.acc_number[-4:]

		root.set("metodoDePago", pay_method_id)
		root.set("LugarExpedicion", invoice.company_id.city)
		root.set("NumCtaPago", cta_pago)

		root.set("condicionesDePago", invoice.payment_term_id.name)
		root.set("subTotal", unicode(invoice.amount_untaxed))
		root.set("total", unicode(invoice.amount_total))

		emisor = ET.SubElement(root, '{%s}Emisor' % namespaces['cfdi'])
		receptor = ET.SubElement(root, '{%s}Receptor' % namespaces['cfdi'])
		conceptos = ET.SubElement(root, '{%s}Conceptos' % namespaces['cfdi'])
		impuestos = ET.SubElement(root, '{%s}Impuestos' % namespaces['cfdi'])



		xml_str = ET.tostring(root)
		xml = minidom.parseString(xml_str.encode("utf-8"))
		_logger.info(xml.toprettyxml())
