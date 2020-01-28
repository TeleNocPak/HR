
{
    'name': 'HRMS Branch Transfer',
    'version': '12.0.1.0.0',
    'summary': 'Employee transfer between branches',
    'category': 'Generic Modules/Human Resources',
    'author': 'Telenoc',
    'company': 'Telenoc IT services and solution',
    'website': 'https://www.telenoc.org',
    'depends': ['base',
                'hr_employee_updation'
                ],
    'data': [
        'views/employee_transfer.xml',
        'security/ir.model.access.csv',
        'security/branch_security.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
