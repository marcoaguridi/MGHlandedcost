{
    'name': 'Extended Landed Cost',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Extends stock landed cost with new unitary cost calculation',
    'description': """
This module extends the functionality of stock landed cost by adding a new tab 
for calculating new unitary costs based on the landed cost lines.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['stock_landed_costs'],
    'data': [
        'views/stock_landed_cost_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
