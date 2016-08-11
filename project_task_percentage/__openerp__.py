{
    'name': "Módulo que agregua un porcentaje de avance de la tarea",
    'version': '1.0',
    'depends': ['project'],
    'author': "X8BIT SA DE CV",
    'category': 'Recursos Humanos',
    'description': """
    Módulo que agregua un porcentaje de avance de la tarea
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/project_task_percentage.xml',
    ],
    'installable': True,
    'auto_install': False,
}