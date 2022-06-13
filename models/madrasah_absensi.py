# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MadrasahAbsensi(models.Model):
    _name = 'isa_data.madrasah_absensi'
    _description = 'Absensi Madrasah'

    tanggal = fields.Date('Tanggal Absensi', required=True)
    murid_name = fields.Many2one('isa_data.madrasah_absensi', required=True)
    kehadiran = fields.Selection([
    	('hadir', 'Hadir'),
    	('sakit', 'Sakit'),
    	('izin', 'Izin'),
    	('absen', 'Tidak Hadir'),
    	], string='Kehadiran', default='hadir', required=True)
    keterangan = fields.Text(string='Keterangan')