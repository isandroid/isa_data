# -*- coding: utf-8 -*-

from odoo import models, fields, api

class JemaatKelompok(models.Model):
    _name = 'isa_data.jemaat_kelompok'
    _description = 'Data Kelompok Jemaat'

    name = fields.Char(string='Kelompok', required=True)
    jemaat = fields.Many2one('isa_data.jemaat', string='Jemaat', required=True)
