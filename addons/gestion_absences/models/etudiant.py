from odoo import models, fields

class Etudiant(models.Model):
    _name = 'gestion.etudiant'
    _description = 'Etudiant'

    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom")
    cne = fields.Char(string="CNE")
    filiere = fields.Char(string="Filière")
