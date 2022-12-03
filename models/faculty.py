# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import *


class Faculties(models.Model):
    _name = "tp.master.faculty"
    _description = "Liste des filières"



    name = fields.Char(string="Nom", required=True)
    code = fields.Char(string="Code", required=True)
    nbre_student = fields.Char(string="Nombre d'étudiant", compute='_compute_nbre_student')
    student_ids = fields.One2many('tp.master.student', 'faculty_id', 'Liste des étudiants')
    program_id = fields.Many2one('tp.master.program', string="Programmes")
    speciality_ids = fields.Many2many('tp.master.speciality', string="Spécialité", required=False)

   


    def _compute_nbre_student(self):
        self.nbre_student = len(self.student_ids)
