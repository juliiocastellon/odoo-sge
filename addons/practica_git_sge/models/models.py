from odoo import models, fields


class ModeloPractica(models.Model):
    _name = 'practica_git_sge.practica'
    _description = 'Modelo de prueba para la práctica de Git'

    name = fields.Char(string="Nombre de prueba", required=True)
