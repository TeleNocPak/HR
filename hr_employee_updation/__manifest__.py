# -*- coding: utf-8 -*-

{
    'name': 'HRMS Employee Info',
    'version': '12.0.2.0.0',
    'summary': """Adding Advanced Fields In Employee Master""",
    'description': 'This module helps you to add more information in employee records.',
    'category': 'Generic Modules/Human Resources',
    'author': 'Telenoc',
    'website': "https://www.teleoc.org",
    'depends': ['base', 'hr', 'mail', 'hr_gamification'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_view.xml',
        'views/hr_notification.xml',
    ],
    'demo': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
