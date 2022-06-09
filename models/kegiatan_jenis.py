# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KegiatanJenis(models.Model):
    _name = 'isa_data.kegiatan_jenis'
    _description = 'Jenis Kegiatan'

    name = fields.Char(string='Jenis Kegiatan', required=True)
