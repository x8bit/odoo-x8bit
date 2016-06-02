{
    'name': "Agregar campos a contrato",
    'version': '1.0',
    'depends': ['hr'],
    'author': "Juan Carlos del Valle",
    'category': 'Contracts',
    'description': """
    Agrega campos a contrato para calculo de nominas
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
}