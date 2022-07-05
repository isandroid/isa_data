# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HomeopatiStok(models.Model):
    _name = 'isa_data.homeopati_stok'
    _description = 'Data Stok Homeopati'

    tanggal = fields.Date(string='Tanggal', required=True)
    remedi = fields.Many2one('isa_data.homeopati_remedi', string='Remedi', required=True)
    potensi = fields.Char(related='remedi.potensi', string='Potensi', store=True)
    kondisi = fields.Integer(string='Prosentase Isi', required=True)
    keterangan = fields.Text(string='Keterangan')

    # def name_get(self):
    #     return self.mapped(lambda it: (it.id, f"{it.remedi} - {it.potensi}"))