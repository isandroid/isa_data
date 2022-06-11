# -*- coding: utf-8 -*-

from odoo import models, fields, api

class KeuanganDkm(models.Model):
    _name = 'isa_data.keuangan_dkm'
    _description = 'Data DKM'

    tempat_asal = fields.Char(string='Tempat Asal', required=True)
    tempat_tujuan = fields.Char(string='Tempat Tujuan', required=True)
    tanggal_berangkat = fields.Date(string='Tanggal Berangkat', required=True) 
    tanggal_kembali = fields.Date(string='Tanggal Kembali', required=True)
    km_awal = fields.Float(string='KM Awal')
    km_akhir = fields.Float(string='KM Akhir')
    jumlah_km = fields.Float(string='Jumlah KM', compute='_compute_jarak_km')
    keuangan_biaya = fields.Integer(string='Jumlah (Rp)')
    name = fields.Many2one('isa_data.kegiatan', string='Nama Kegiatan', required=True)
    keuangan_akun = fields.Many2one('isa_data.keuangan_akun', string='POS Pengeluaran')
    lampiran = fields.Binary(string='Struk/Kwitansi', store=True, attachment=False)


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
    def _compute_jarak_km(self):
        for record in self:
            record.jumlah_km = float(record.km_akhir) - float(record.km_awal)
