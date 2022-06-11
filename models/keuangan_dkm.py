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
    klaim_bensin = fields.Float(string='Klaim Bensin (Liter)', compute='_compute_klaim_bensin')
    bensin_jenis = fields.Many2one('isa_data.keuangan_bensin', string='Jenis Bensin')
    bensin_harga = fields.Float(related='bensin_jenis.harga', string='Harga Bensin')
    klaim_uang = fields.Float(string='Klaim DKM (Rp)', compute='_compute_klaim_uang')
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

    def _compute_klaim_bensin(self):
        for record in self:
            record.klaim_bensin = float(record.jumlah_km) / 8

    def _compute_klaim_uang(self):
        for record in self:
            if record.bensin_jenis:
                record.klaim_uang = record.klaim_bensin * record.bensin_harga
            else:
                record.klaim_uang = False