# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ModuleName(models.TransientModel):
    _name = 'tp.master.add_student'
    _description = 'Transient model add student classroom'

    student_id = fields.Many2one('tp.master.student',
                                 'Etudiant',
                                 required=True)
    classroom_id = fields.Many2one('tp.master.classroom',
                                   'Classe',
                                   required=True)

    def action_add_student_classroom(self):
        print("Button on")
