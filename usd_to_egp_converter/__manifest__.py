{
    'name': 'USD to EGP Converter',
    'summary': 'Convert USD totals to EGP using live API in Sale Orders and Invoices',
    'author': 'Mahmoud Yousry',
    'category': 'Sales',
    'depends': ['sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
}
