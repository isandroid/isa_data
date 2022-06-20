# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HomeopatiPengobatan(models.Model):
    _name = 'isa_data.homeopati_pengobatan'
    _description = 'Data Pengobatan Homeopati'

    tanggal = fields.Date(string='Tanggal', required=True)
    pasien_nama = fields.Many2one('isa_data.homeopati_pasien', string='Nama Pasien', required=True)
    pasien_aims = fields.Integer(related='pasien_nama.aims', string='AIMS', store=True)
    pasien_jemaat = fields.Many2one(related='pasien_nama.jemaat', string='Jemaat', store=True)
    keluhan = fields.Text(string='Keluhan', required=True)
    remedi = fields.Many2many('isa_data.homeopati_remedi', string='Remedi')

    # def name_get(self):
    #     return self.mapped(lambda it: (it.id, f"{it.nama} - {it.jemaat}"))