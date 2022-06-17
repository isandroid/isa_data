# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MadrasahNilai(models.Model):
    _name = 'isa_data.madrasah_nilai'
    _description = 'Nilai Madrasah'

    murid_nama = fields.Many2one('isa_data.madrasah_murid', string='Nama Murid', required=True)
    pelajaran = fields.Many2one('isa_data.madrasah_pelajaran', string='Pelajaran', required=True)
    nilai = fields.Integer(string='Nilai', required=True)
    nilai_jenis = fields.Selection([
    	('harian', 'Nilai Harian'),
    	('ujian', 'Nilai Ujian'),
    	], string='Jenis Nilai', required=True)

#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
