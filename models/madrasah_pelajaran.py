# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MadrasahPelajaran(models.Model):
    _name = 'isa_data.madrasah_pelajaran'
    _description = 'Pelajaran Madrasah'

    name = fields.Char(string='Pelajaran', required=True)
    keterangan = fields.Text(string='Keterangan')
    
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
