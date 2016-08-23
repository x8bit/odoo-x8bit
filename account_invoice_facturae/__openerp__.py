{
    'name': "Modulo que agrega la facturación electrónica a los invoices de odoo",
    'version': '1.0',
    'depends': [
        'document',
        'company_facturae_certs',
        'l10n_mx_payment_method',
        'l10n_mx_partner_address'
    ],
    'author': "X8BIT SA DE CV",
    'website': 'www.x8bit.com',
    'category': 'Accounting',
    'description': """
    Modulo que agrega la facturación electrónica a los invoices de odoo
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/invoice_facturae.xml',
    ],
}