{
    'name': "Modulo para capturar codigo para App",
    'version': '1.0',
    'depends': [],
    'author': "Lizbeth Contreras",
    'category': 'Timesheet',
    'description': """
    Codigo para App
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_passcode.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo.xml',
    ],
}