{
    'name': "Módulo que agrega un archivo imagen al proyecto",
    'version': '1.0',
    'depends': ['project'],
    'author': "X8BIT SA DE CV",
    'category': 'Recursos Humanos',
    'description': """
    Módulo que agrega un archivo imagen al proyecto
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/project_project_image.xml',
    ],
    'installable': True,
    'auto_install': False,
}