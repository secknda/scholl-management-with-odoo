# -*- coding: utf-8 -*-
{
    'name':
    'TP odoo Master 2022 ISI',
    'version':
    '14.0.2.1.0',
    'summary':
    'TP Odoo M2 ISI',
    'sequence':
    1,
    'description':
    """Ce module a été réalisé lors du TP cours Odoo14 pour gérer un établissement """,
    'category':
    'TP',
    'author':
    'Youssoupha LAM',
    'maintainer':
    'Youssoupha LAM',
    'website':
    'https://www.groupeisi.com',
    'license':
    'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/add_student_to_classroom.xml',
        'views/student.xml',
        'views/program.xml',
        'views/faculty.xml',
        'views/teacher.xml',
        'views/grade.xml',
        'views/speciality.xml',
        'views/classroom.xml',
        'views/sequence.xml',
        'menu/menu.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': [''],
    'installable':
    True,
    'application':
    True,
    'auto_install':
    False,
}
