# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools import config
# import xml.etree.cElementTree as ET
from lxml import etree as ET
import xml.dom.minidom as minidom
from openerp.exceptions import UserError
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

		try:
			pay_method_id = invoice.pay_method_id.code
			cta_pago = invoice.acc_payment.acc_number[-4:]
		except TypeError:
			raise UserError("Error en método de pago o cuenta de pago")

		root.set("metodoDePago", pay_method_id)
		root.set("LugarExpedicion", invoice.company_id.city)
		root.set("NumCtaPago", cta_pago)

		root.set("condicionesDePago", invoice.payment_term_id.name)
		root.set("subTotal", unicode(invoice.amount_untaxed))
		root.set("total", unicode(invoice.amount_total))

		emisor = ET.SubElement(root, '{%s}Emisor' % namespaces['cfdi'])
		
		try:
			emisor.set("rfc", invoice.company_id.vat[2:])
			emisor.set("nombre", invoice.company_id.name)
		except TypeError:
			raise UserError("RFC no asignado en la compañía que esta facturando")

		emisor_df = ET.SubElement(emisor, '{%s}DomicilioFiscal' % namespaces['cfdi'])
		try:
			emisor_df.set("calle", invoice.company_id.street) 
			emisor_df.set("noExterior", invoice.company_id.l10n_mx_street3) 
			emisor_df.set("noInterior", invoice.company_id.l10n_mx_street4) 
			emisor_df.set("colonia", invoice.company_id.street2) 
			emisor_df.set("municipio", invoice.company_id.city) 
			emisor_df.set("estado", invoice.company_id.state_id.name) 
			emisor_df.set("pais", invoice.company_id.country_id.name) 
			emisor_df.set("codigoPostal", invoice.company_id.zip)
		except TypeError:
			raise UserError("Error en el domicilio de la compañía que esta facturando")

		emisor_rf = ET.SubElement(emisor, '{%s}RegimenFiscal' % namespaces['cfdi'])
		try:
			emisor_rf.set("Regimen", invoice.company_id.partner_id.regimen_fiscal_id.name)
		except:
			raise UserError("Error en el régimen de la compañía que esta facturando")

		receptor = ET.SubElement(root, '{%s}Receptor' % namespaces['cfdi'])
		try:
			receptor.set("rfc", invoice.partner_id.vat[2:])
			receptor.set("nombre", invoice.partner_id.name)
		except TypeError:
			raise UserError("RFC no asignado en la compañía a la que esta facturando")

		receptor_d = ET.SubElement(receptor, '{%s}Domicilio' % namespaces['cfdi'])
		try:
			receptor_d.set("calle", invoice.partner_id.street) 
			receptor_d.set("noExterior", invoice.partner_id.l10n_mx_street3)
			if invoice.partner_id.l10n_mx_street4:
				receptor_d.set("noInterior", invoice.partner_id.l10n_mx_street4)
			receptor_d.set("colonia", invoice.partner_id.street2) 
			receptor_d.set("municipio", invoice.partner_id.city) 
			receptor_d.set("estado", invoice.partner_id.state_id.name) 
			receptor_d.set("pais", invoice.partner_id.country_id.name) 
			receptor_d.set("codigoPostal", invoice.partner_id.zip)
		except TypeError:
			raise UserError("Error en el domicilio de la compañía a la que esta facturando")
		
		conceptos = ET.SubElement(root, '{%s}Conceptos' % namespaces['cfdi'])

		for invoice_line in invoice.invoice_line_ids:
			concepto = ET.SubElement(conceptos, '{%s}Concepto' % namespaces['cfdi'])
			
			concepto.set("cantidad", "{:.2f}".format(invoice_line.quantity))
			concepto.set("descripcion", invoice_line.name)
			concepto.set("importe", "{:.2f}".format(invoice_line.price_subtotal))
			concepto.set("noIdentificacion", str(invoice_line.product_id.id))
			concepto.set("unidad", invoice_line.uom_id.name)
			concepto.set("valorUnitario", "{:.2f}".format(invoice_line.price_unit))

		# invoice.

		# <cfdi:Conceptos>
		# 	<cfdi:Concepto cantidad="1.00" descripcion="CONSULTORÍA EN DISEÑO INTERFACES DE USUARIO. PLATAFORMA DE ANALÍTICA PREDICTIVA. PROYECTO PEI 223207." importe="21551.72" noIdentificacion="02" unidad="UNIDAD" valorUnitario="21551.72"/>
		# 	<cfdi:Concepto cantidad="1.00" descripcion="CONSULTORÍA EN IMPLEMENTACIÓN DE PROFIT" importe="20000.00" noIdentificacion="21" unidad="SERVICIO" valorUnitario="20000.00"/>
		# </cfdi:Conceptos>

		impuestos = ET.SubElement(root, '{%s}Impuestos' % namespaces['cfdi'])



		xml_str = ET.tostring(root)
		xml = minidom.parseString(xml_str.encode("utf-8"))
		_logger.info(xml.toprettyxml())
		raise UserError(xml.toprettyxml())
