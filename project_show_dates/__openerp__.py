{
    'name': "Módulo que hace visibles las fechas de inicio y fin de los proyectos",
    'version': '1.0',
    'depends': ['project'],
    'author': "X8BIT SA DE CV",
    'category': 'Project',
    'description': """
    Módulo que hace visibles las fechas de inicio y fin de los proyectos
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/project_show_dates.xml',
    ],
    'installable': True,
    'auto_install': False,
}