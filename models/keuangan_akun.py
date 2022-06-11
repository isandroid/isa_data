# -*- coding: utf-8 -*-

from odoo import models, fields, api

class KeuanganAkun(models.Model):
    _name = 'isa_data.keuangan_akun'
    _description = 'Akun Keuangan'

    name = fields.Char(string='Nama Akun', required=True)
    kode = fields.Char(string='Kode Akun', required=True)
    jenis = fields.Selection([
		('1', 'Harta'),
		('2', 'Kewajiban'),
		('3', 'Modal'),
		('4', 'Pendapatan'),
		('5', 'Beban'),
		('6', 'Lainnya'),
    	], string='Jenis Akun', required=True)