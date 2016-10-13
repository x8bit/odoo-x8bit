{
    'name': "X8bit - Módulo de información extra para contactos",
    'version': '1.0',
    'author': "X8BIT SA DE CV",
    'website': 'www.x8bit.com',
    'category': 'Specific Industry Applications',
    'application': True,
    'description': """
    X8bit - Módulo de información extra para contactos

        - Agrega campo de nombre comercial al contacto
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/contacto.xml',
    ],
    'depends': [
        'base',
        'account'
    ]
}