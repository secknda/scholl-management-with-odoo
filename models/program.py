# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Programs(models.Model):
	_name = "tp.master.program"
	_description = "Liste des programmes"



	name = fields.Char(string="Nom du programme", required=True)
	code = fields.Char(string="Code", required=True)
	faculty_ids = fields.One2many('tp.master.faculty', 'program_id', 'Liste des filières')
	student_ids = fields.One2many('tp.master.student', 'program_id', 'Liste des étudiants')
	nbre_student = fields.Char(string="Nombre Etudiant", compute='_compute_nbre_student')
	nbre_faculty = fields.Char(string="Nombre de filières", compute='_compute_nbre_faculty')
	



	def _compute_nbre_faculty(self):
		self.nbre_faculty = len(self.faculty_ids)

	
	def _compute_nbre_student(self):
		self.nbre_student = self.env['tp.master.student'].search_count([('program_id','=',self.id)])


	