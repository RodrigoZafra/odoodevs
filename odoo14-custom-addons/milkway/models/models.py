# -*- coding: utf-8 -*-

from odoo import models, fields, api


class milkway(models.Model):
    _name = 'milkway.milkway'
    _description = 'milkway.milkway'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    planet_status = fields.Text() 
    mass = fields.Float()
    radius = fields.Text()
    orbital_period = fields.Float()
    angular_distance = fields.Text()
    discovered = fields.Integer()
    molecules = fields.Text()
    star_name = fields.Text()
    star_distance = fields.Float() 
    star_age = fields.Float()
    
 
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
