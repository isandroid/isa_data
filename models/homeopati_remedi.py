# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HomeopatiRemedi(models.Model):
    _name = 'isa_data.homeopati_remedi'
    _description = 'Data Remedi Homeopati'

    remedi = fields.Char(string='Remedi', required=True)
    name = fields.Char(compute='_compute_name', string='Remedi 2', required=True, oldname='remedi', store=True)
    potensi = fields.Char(string='Potensi')
    tautan = fields.Char(string='Tautan')

    # def name_get(self):
        # return self.mapped(lambda it: (it.id, f"{it.remedi} - {it.potensi}"))

    # @api.multi
    # def name_get(self):
    #     result = []
    #     for me_id in self :
    #         result.append((me_id.id, "%s"%(me_id.remedi)))
    #     return result

    @api.depends('remedi', 'potensi')
    def _compute_name(self):
        for me_id in self :
            if me_id.potensi:
                me_id.name = f"{me_id.remedi} - {me_id.potensi}"
            else:
                me_id.name = f"{me_id.remedi}"