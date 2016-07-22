{
    'name': "Módulo que agregua un checkbox de urgente a un gasto para poder diferenciarlo de los demás",
    'version': '1.0',
    'depends': ['hr_expense'],
    'author': "X8BIT SA DE CV",
    'website': 'www.x8bit.com',
    'category': 'Recursos Humanos',
    'description': """
    Módulo que agregua un checkbox de urgente a un gasto para poder diferenciarlo de los demás
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/hr_expense_priority.xml',
    ],
    'installable': True,
    'auto_install': False,
}