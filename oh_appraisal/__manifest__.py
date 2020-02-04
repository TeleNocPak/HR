# -*- coding: utf-8 -*-


{
    'name': "Open HRMS Employee Appraisal",
    'version': '12.0.1.1.2',
    'summary': """Roll out appraisal plans and get the best of your workforce""",
    'description': """Roll out appraisal plans and get the best of your workforce""",
    'category': 'Generic Modules/Human Resources',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.openhrms.com",
    'depends': ['base', 'hr', 'survey'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_appraisal_security.xml',
        'views/hr_appraisal_survey_views.xml',
        'views/hr_appraisal_form_view.xml',
        'data/hr_appraisal_stages.xml'
    ],
    'images': ["static/description/icon.png"],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}
