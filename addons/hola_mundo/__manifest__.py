{
    'name': "Hola Mundo",
    'summary': "Mi primer módulo de Odoo 19",
    'description': """Módulo de prueba con todos los tipos de campo básicos.""",
    'author': "alumne14",
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}
