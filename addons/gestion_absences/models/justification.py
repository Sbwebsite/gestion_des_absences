from odoo import models, fields

class Justification(models.Model):
    _name = 'gestion.justification'
    _description = 'Justification'

    absence_id = fields.Many2one(
        'gestion.absence',
        string="Absence",
        required=True
    )
    motif = fields.Text(string="Motif")
    date_justification = fields.Date(string="Date de justification")
