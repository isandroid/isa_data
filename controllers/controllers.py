# -*- coding: utf-8 -*-
# from odoo import http


# class IsaData(http.Controller):
#     @http.route('/isa_data/isa_data', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/isa_data/isa_data/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('isa_data.listing', {
#             'root': '/isa_data/isa_data',
#             'objects': http.request.env['isa_data.isa_data'].search([]),
#         })

#     @http.route('/isa_data/isa_data/objects/<model("isa_data.isa_data"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('isa_data.object', {
#             'object': obj
#         })
