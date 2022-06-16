# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HomeopatiResep(models.Model):
    _name = 'isa_data.homeopati_resep'
    _description = 'Data Resep Homeopati'

    penyakit = fields.Char(string='Penyakit', required=True)
    remedi = fields.Many2many('isa_data.homeopati_remedi', string='Remedi', required=True)
    resep_huzur = fields.Selection([
        ('y', 'Ya'),
        ('t', 'Tidak'),
        ], string='Resep Huzur?', default='t')
    keterangan = fields.Text(string='Keterangan')

    # def name_get(self):
    #     return self.mapped(lambda it: (it.id, f"{it.remedi} - {it.potensi}"))