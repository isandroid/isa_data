# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HomeopatiRemedi(models.Model):
    _name = 'isa_data.homeopati_remedi'
    _description = 'Data Remedi Homeopati'

    remedi = fields.Char(string='Remedi', required=True)
    potensi = fields.Char(string='Potensi')
    tautan = fields.Char(string='Tautan')

    def name_get(self):
        return self.mapped(lambda it: (it.id, f"{it.remedi} - {it.potensi}"))