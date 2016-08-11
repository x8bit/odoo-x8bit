{
    'name': "Módulo que agregua un combo de vehiculo al modulo stock.picking",
    'version': '1.0',
    'depends': ['stock'],
    'author': "X8BIT SA DE CV",
    'category': 'Recursos Humanos',
    'description': """
    Módulo que agregua un combo de vehiculo al modulo stock.picking
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_vehicle.xml',
    ],
    'installable': True,
    'auto_install': False,
}