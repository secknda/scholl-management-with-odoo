# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import string


class Students(models.Model):
    _name = "tp.master.student"
    _description = "Liste des étudiants"



    name = fields.Char(string="Nom et Prénoms", compute='_compute_name', store="True")
    file_number = fields.Char(string='Numéro de dossier', required=True, copy=False, readonly=True,index=True, default=lambda self: _('New'))
    firstname = fields.Char(string="Prénoms", required=True)
    lastname = fields.Char(string="Nom de famille", required=True)
    birthday = fields.Date(string="Date de Naissance") 
    place_birth = fields.Char(string="Lieu de Naissance", required=False)
    gender = fields.Selection([
        ('male', 'Masculin'),
        ('female', 'Féminin'),
    ], required=True, string="Sexe")
    program_id = fields.Many2one('tp.master.program', string="Programmes", required=True)
    faculty_id = fields.Many2one('tp.master.faculty', string="Filières", domain="[('program_id', '=', program_id)]", required=True)
    image = fields.Binary(string="Photo")
    email = fields.Char(string='Email', required=False)
    phone = fields.Char(string='Téléphone', required=False)
    birth_act = fields.Binary(string="Extrait de Naissance", attachment=True)
    id_card = fields.Binary(string="Carte d'identité nationale")
    passport = fields.Binary(string="Passeport")
    nationality_certificate = fields.Binary(string="Certificat de nationalité")
    gradebook_ids = fields.Many2many('ir.attachment', 'attachement_1', 'attachment_id', string="Bulletins de notes")
    diploma_certificate_ids = fields.Many2many('ir.attachment', 'attachement_2', 'attachment_id', string="Diplômes et Attestations")
    state = fields.Selection([('new', 'Nouveau'), ('registered', 'Préinscrit'),('valid', 'Validé'),('inscribe', 'Inscrire dans une classe'),('rejected', 'Rejeté')], 
        default='new', string="Statut", tracking=True)
    reason_rejection = fields.Text('Motif du rejet')
    classroom_id = fields.Many2one('tp.master.classroom', string="Salle", required=False)


    def action_new(self):
        self.state = 'new'

    def action_registered(self):
        self.state = 'registered'

    def action_valid(self):
        self.state = 'valid'

    def action_inscribe(self):
        self.state = 'inscribe'
        
    def action_rejected(self):
        self.state = 'rejected'

    @api.depends('firstname','lastname')
    def _compute_name(self):
        self.name = (self.firstname or '')+' '+(self.lastname or '')

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('tp.master.student') or '/'
        vals['file_number'] = seq
        return super(Students, self).create(vals)

    @api.constrains('reason_rejection','state')
    def action_reason_rejection(self):
        if not self.reason_rejection and self.state == 'rejected':
            raise ValidationError(_("Veuillez Remplir le Motif du rejet"))
