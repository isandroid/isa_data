# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MadrasahMurid(models.Model):
    _name = 'isa_data.madrasah_murid'
    _description = 'Data Murid Madrasah'

    name = fields.Char(string='Nama Murid', required=True)
    kelas = fields.Integer(string='Kelas', required=True)
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    keterangan = fields.Text('Keterangan')