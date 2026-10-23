from odoo import models, fields


class Prueba(models.Model):
    _name = 'hola_mundo.prueba'
    _description = 'Modelo de prueba Hola Mundo'

    name = fields.Char(string='Nombre', required=True)
    quantitat = fields.Integer(string='Cantidad', default=1)
    descripcio = fields.Text(string='Descripción')
    preu = fields.Float(string='Precio', required=True)
    actiu = fields.Boolean(string='Activo', default=True)
    data = fields.Date(string='Fecha', default=fields.Date.context_today)
    data_hora = fields.Datetime(string='Fecha y hora')
    contingut = fields.Html(string='Contenido')
    fitxer = fields.Binary(string='Fichero')
    imatge = fields.Image(string='Imagen', max_width=512, max_height=512)
    estat = fields.Selection(
        [('esborrany', 'Borrador'), ('confirmat', 'Confirmado'), ('fet', 'Hecho')],
        string='Estado', default='esborrany')
