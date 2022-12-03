# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Grades(models.Model):
    _name = "tp.master.grade"
    _description = "Liste des grades"



    name = fields.Char(string="Nom du grade", required=True)
    code = fields.Char(string="Code", required=True)
    