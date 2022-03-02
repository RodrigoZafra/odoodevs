# -*- coding: utf-8 -*-

from odoo import models, fields, api


class infame(models.Model):
    _name = 'infame.infame'
    _description = 'infame.infame'

    title = fields.Char()
    date = fields.Date()
    score = fields.Float()
    distributor = fields.Char()
    publisher = fields.Char()
    favs = fields.Boolean(compute="_value_favs", store=True)

    #Este computo depende de la variable score
    @api.depends('score')
    def _value_favs(self):
        for record in self:
            if record.score>=75:
                record.favs = True
            else:
                record.favs = False