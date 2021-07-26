# -*- coding: utf-8 -*-
# from odoo import http


# class BwMaqueta(http.Controller):
#     @http.route('/bw_maqueta/bw_maqueta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bw_maqueta/bw_maqueta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bw_maqueta.listing', {
#             'root': '/bw_maqueta/bw_maqueta',
#             'objects': http.request.env['bw_maqueta.bw_maqueta'].search([]),
#         })

#     @http.route('/bw_maqueta/bw_maqueta/objects/<model("bw_maqueta.bw_maqueta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bw_maqueta.object', {
#             'object': obj
#         })
