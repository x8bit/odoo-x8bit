{
    'name': "Modulo de conexión con toggl",
    'version': '1.0',
    'depends': ['hr'],
    'author': "X8BIT SA DE CV",
    'category': 'Timesheet',
    'description': """
    Conexión con toggl
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/hr_timesheet_toggl_employee.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo.xml',
    ],
}