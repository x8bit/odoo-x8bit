{
    'name': "Modulo que agrega boton de registro de tiempo en tareas de proyectos",
    'version': '1.0',
    'depends': ['project', 'web'],
    'author': "Juan Carlos del Valle",
    'category': 'Project',
    'description': """
    Modulo que agrega boton de registro de tiempo en tareas de proyectos
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/project_task_track_button.xml',
    ],
    # data files containing optionally loaded demonstration data
    'qweb': [
        'static/src/xml/show_tracking.xml',
    ],
    'installable': True,
    'auto_install': False,
}