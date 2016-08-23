{
    'name': "Módulo que agrega cantidades a tarea",
    'version': '1.0',
    'depends': ['project'],
    'author': "X8BIT SA DE CV",
    'category': 'Recursos Humanos',
    'description': """
    Módulo que agrega cantidades a tarea
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/project_task_cant.xml',
    ],
    'installable': True,
    'auto_install': False,
}