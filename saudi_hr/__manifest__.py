# -*- coding: utf-8 -*-
{
    'name': "Telenoc HCM",

    'summary': """
        human capital management system""",

    'description': """
        Human capital management system that can manage Employee salary,
        Employee Documents and Employee Training ,Appraisal ,And Resignation process
        and also cover all employee related Detail.
    """,

    'author': "Telenoc",
    'website': "http://www.telenoc.org",

   
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_payroll_account',
                'hr_gamification',
                'hr_employee_updation',
                'hr_recruitment',
                'hr_attendance',
                'hr_holidays',
                'hr_payroll',
                'hr_expense',
                'hr_leave_request_aliasing',
                'hr_timesheet',
                'oh_appraisal',
                'oh_employee_creation_from_user',
                'hr_multi_company',
                'ohrms_loan_accounting',
                'ohrms_salary_advance',
                'mail',
                ],
    'data': [
        'security/hr_insurance_security.xml',
        'security/hr_reminder_security.xml',
        'security/reward_security.xml',
        'security/ir.model.access.csv',
        'views/menu_arrangement_view.xml',
        'views/template_view.xml',
        'views/hr_announcement_view.xml',
        'views/template_view.xml',
        'views/gosi_view.xml',
        'views/sequence.xml',
        'views/hcm.xml',
        # 'views/reminder_template.xml',
        'views/hr_reminder_view.xml',
        'views/employee_document_view.xml',
        'views/employee_insurance_view.xml',
        'views/policy_management.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'application':True
}
