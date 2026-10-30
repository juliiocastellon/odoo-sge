from odoo import models, fields


class Pavello(models.Model):
    _name = 'basquet.pavello'
    _description = 'Pavelló'

    name = fields.Char(string='Nom', required=True)
    ciutat = fields.Char(string='Ciutat')


class Equip(models.Model):
    _name = 'basquet.equip'
    _description = 'Equip'

    name = fields.Char(string='Nom', required=True)
    ciutat = fields.Char(string='Ciutat')
    jugador_ids = fields.One2many(
        'basquet.jugador', 'equip_id', string='Jugadors')
    estadi_id = fields.Many2one(
        'basquet.pavello', string='Estadi',
        domain="[('ciutat', '=', ciutat)]")
    equips_agermanats_ids = fields.Many2many(
        'basquet.equip',
        relation='basquet_equip_agermanats_rel',
        column1='equip_id', column2='agermanat_id',
        string='Equips agermanats')
    equips_rivals_ids = fields.Many2many(
        'basquet.equip',
        relation='basquet_equip_rivals_rel',
        column1='equip_id', column2='rival_id',
        string='Rivals històrics')


class Jugador(models.Model):
    _name = 'basquet.jugador'
    _description = 'Jugador'

    name = fields.Char(string='Nom', required=True)
    equip_id = fields.Many2one(
        'basquet.equip', string='Equip',
        domain=[('estadi_id', '!=', False)])
    estadi_nom = fields.Char(
        string='Estadi', related='equip_id.estadi_id.name')
    es_capita = fields.Boolean(string='És capità')
