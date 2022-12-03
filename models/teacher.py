# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Teachers(models.Model):
    _name = "tp.master.teacher"
    _description = "Liste des Profs"

    name = fields.Char(string='Nom et Prénoms', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True, copy=False)
    gender = fields.Selection([('male', 'Masculin'),('female', 'Féminin'),], required=False, default='male', tracking=True, string="Sexe")
    marital_status = fields.Selection([('single', 'Célibataire'),('married', 'Marié'),], required=False, default='single', tracking=True, string="Situation Matrimoniale")
    image = fields.Binary(string="Photo")
    speciality_ids = fields.Many2many('tp.master.speciality', string="Spécialités", required=False)
    grade_id = fields.Many2one('tp.master.grade', string="Grade", required=False)


    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_("Veuillez saisir un age différent de 0 .. !"))











