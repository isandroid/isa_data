# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MadrasahKurikulum(models.Model):
    _name = 'isa_data.madrasah_kurikulum'
    _description = 'Kurikulum Madrasah'

    pelajaran = fields.Many2one('isa_data.madrasah_pelajaran', string='Mata Pelajaran', required=True)
    nama = fields.Char(string='Kurikulum', required=True)
    detil = fields.Char(string='Kurikulum Detil', required=True)
    keterangan = fields.Text(string='Keterangan')

    def name_get(self):
        return self.mapped(lambda it: (it.id, f"{it.nama} - {it.detil}"))