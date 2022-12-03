# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Specialities(models.Model):
    _name = "tp.master.speciality"
    _description = "Liste des spécialités"



    name = fields.Char(string="Nom", required=True)
    code = fields.Char(string="Code", required=True)
    teacher_ids = fields.Many2many('tp.master.teacher', string="Professeurs", required=False)
    faculty_ids = fields.Many2many('tp.master.faculty', string="Filières", required=False)
    