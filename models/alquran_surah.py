# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AlquranSurah(models.Model):
    _name = 'isa_data.alquran_surah'
    _description = 'isa_data.alquran_surah'

    nomor = fields.Integer(string='Nomor Surah')
    name = fields.Char(string='Nama Surah')
    arab = fields.Char(string='Bahasa Arab')
    arti = fields.Char(string='Arti Surah')
    ayat_jumlah = fields.Integer(string='Jumlah Ayat')
    tempat_turun = fields.Char(string='Tempat Turun')
    urutan_pewahyuan = fields.Integer(string='Urutan Pewahyuan')