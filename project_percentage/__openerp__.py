{
    'name': "Módulo que agrega un porcentaje de avance del proyecto",
    'version': '1.0',
    'depends': ['project'],
    'author': "X8BIT SA DE CV",
    'category': 'Recursos Humanos',
    'description': """
    Módulo que agrega un porcentaje de avance del proyecto
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/project_project_percentage.xml',
    ],
    'installable': True,
    'auto_install': False,
}