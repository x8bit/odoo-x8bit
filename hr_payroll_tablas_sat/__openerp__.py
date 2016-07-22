{
    'name': "Modulo de tablas para el calculo de impuestos",
    'version': '1.0',
    'depends': ['hr_payroll'],
    'author': "X8BIT SA DE CV",
    'website': 'www.x8bit.com',
    'category': 'Accounting',
    'description': """
    Tablas para el calculo de impuestos sobre nómina
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/tax_isr.xml',
        'views/subsidios.xml',
        'views/settings.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo.xml',
    ],
}