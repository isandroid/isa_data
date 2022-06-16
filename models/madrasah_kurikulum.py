# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MadrasahKurikulum(models.Model):
    _name = 'isa_data.madrasah_kurikulum'
    _description = 'Kurikulum Madrasah'

    pelajaran = fields.Char(string='Mata Pelajaran', required=True)
    name = fields.Char(string='Kurikulum', required=True)
    detil = fields.Char(string='Kurikulum Detil', required=True)
    keterangan = fields.Text(string='Keterangan')