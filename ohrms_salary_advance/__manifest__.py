# -*- coding: utf-8 -*-

{
    'name': 'HRMS Advance Salary',
    'version': '12.0.1.0.1',
    'summary': 'Advance Salary In HR',
    'description': """
        Helps you to manage Advance Salary Request of your company's staff.
        """,
    'category': 'Generic Modules/Human Resources',
    'author': "Telenoc",
    'website': "https://www.telenoc.org",
    'depends': [
        'hr_payroll', 'hr', 'account', 'hr_contract', 'ohrms_loan',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/salary_structure.xml',
        'views/salary_advance.xml',
    ],
    'demo': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

