# -*- coding: utf-8 -*-

{
    'name': 'HRMS Multi-Company',
    'version': '12.0.1.0.0',
    'summary': """Enables Multi-Company""",
    'description': 'This module enables multi company features',
    'category': 'Generic Modules/Human Resources',
    'author': 'Telenoc',
    'website': "https://www.telenoc.org",
    'depends': ['base', 'hr_contract', 'hr_payroll', 'hr_expense', 'hr_attendance', 'hr_employee_transfer'],
    'data': [
        'views/hr_company_view.xml',
        'views/multi_company_view.xml',
    ],
    'demo': [],

    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
