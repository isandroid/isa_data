# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MadrasahKbm(models.Model):
    _name = 'isa_data.madrasah_kbm'
    _description = 'Kegiatan Belajar Mengajar Madrasah'

    tanggal = fields.Date(string='Tanggal', required=True)
    name = fields.Char(string='Materi yang Diajarkan', required=True)
    pelajaran = fields.Char(related='kurikulum.pelajaran', string='Pelajaran', store=True)
    kurikulum = fields.Many2one('isa_data.madrasah_kurikulum', string='Kurikulum', required=True, store=True)
    kurikulum_detil = fields.Char(related='kurikulum.detil', string='Kurikulum Detil', store=True)
    keterangan = fields.Text(string='Keterangan')
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
