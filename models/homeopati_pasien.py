# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HomeopatiPasien(models.Model):
    _name = 'isa_data.homeopati_pasien'
    _description = 'Data Pasien Homeopati'

    nama = fields.Char(string='Nama Pasien', required=True)
    aims = fields.Integer(string='AIMS')
    jemaat = fields.Many2one('isa_data.jemaat', string='Jemaat')
    alamat = fields.Text(string='Alamat')
    hp = fields.Char(string='Nomor HP')

    def name_get(self):
        return self.mapped(lambda it: (it.id, f"{it.nama} - {it.aims}"))