# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Jemaat(models.Model):
    _name = 'isa_data.jemaat'
    _description = 'Data Jemaat'

    name = fields.Char(string='Jemaat', required=True)
    kode = fields.Char(string='Kode Jemaat', required=True)
    nomor = fields.Integer(string='Nomor Jemaat')
