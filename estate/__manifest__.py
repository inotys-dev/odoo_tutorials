{
    'name': 'REAL ESTATE',
    'version': '1.0',
    'category': 'Inotys',
    'sequence': 15,
    'summary': 'On va tester des trucs',
    'description': "Test",
    'author': "Michael B.",
    
    'depends': [
        'base'
    ],
    'data': [  
        'security/ir.model.access.csv',   
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False
}