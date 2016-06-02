{
    'name': "Extender reportes de balance de saldos",
    'version': '1.0',
    'depends': ['account'],
    'author': "Juan Carlos del Valle",
    'category': 'Accounting',
    'description': """
    Nuevos reportes
    """,
    # data files always loaded at installation
    'data': [
        'views/account_report_aged_partner_balance_x8.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
}