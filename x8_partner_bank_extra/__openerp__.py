{
    'name': "X8bit - Módulo de información extra para cuentas bancarias de contactos",
    'version': '1.0',
    'author': "X8BIT SA DE CV",
    'website': 'www.x8bit.com',
    'category': 'Specific Industry Applications',
    'application': True,
    'description': """
    X8bit - Módulo de información extra para cuentas bancarias de contactos

        - Sobreescribe el campo de número de cuenta bancaria con el de la clabe si este no existe
    """,
    'data': [
        'security/ir.model.access.csv',
    ],
    'depends': [
        'base',
    ]
}