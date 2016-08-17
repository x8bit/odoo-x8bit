{
    'name': "Modulo de recepción de camiones",
    'version': '1.0',
    'depends': ['project'],
    'author': "X8BIT SA DE CV",
    'website': 'www.x8bit.com',
    'category': 'Logistics',
    'description': """
    Modulo para recibir camiones
    """,
    # data files always loaded at installation
    'data': [
        'sequence.xml'
        'security/x8_security.xml',
        'security/ir.model.access.csv',
        'views/recepcion_view.xml',
        'views/fletes_vehicle.xml',
        'views/fletes_material.xml',
        'views/fletes_checador.xml',
    ],
}