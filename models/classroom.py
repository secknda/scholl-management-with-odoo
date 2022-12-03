# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Programs(models.Model):
	_name = "tp.master.classroom"
	_description = "Liste des salles de classe"



	name = fields.Char(string="Nom de la salle", required=True)
	code = fields.Char(string="Numéro de la salle", required=True)
	faculty_id = fields.Many2one('tp.master.faculty', string="Filières", required=True)
	student_ids = fields.One2many('tp.master.student', 'classroom_id', 'Liste des étudiants')
	nbre_student = fields.Char(string="Nombre Etudiant")
	#nbre_student = fields.Char(string="Nombre Etudiant", compute='_compute_nbre_student')


	_sql_constraints = [
        ('code_uniq',
         'unique(code)', 'Le numéro de la salle est unique!')]
	





	