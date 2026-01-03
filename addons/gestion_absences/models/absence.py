from odoo import models, fields

class Absence(models.Model):
    _name = 'gestion.absence'
    _description = 'Absence'

    etudiant_id = fields.Many2one(
        'gestion.etudiant',
        string="Étudiant",
        required=True
    )
    date_absence = fields.Date(string="Date", required=True)
    justifie = fields.Boolean(string="Justifiée", default=False)
