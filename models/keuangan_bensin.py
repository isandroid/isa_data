# -*- coding: utf-8 -*-

from odoo import models, fields, api

class KeuanganBensin(models.Model):
    _name = 'isa_data.keuangan_bensin'
    _description = 'Harga Bensin'

    name = fields.Char(string='Jenis Bensin', required=True)
    harga = fields.Float(string='Harga Bensin', required=True)