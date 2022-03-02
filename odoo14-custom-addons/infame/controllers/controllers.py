# -*- coding: utf-8 -*-
# from odoo import http


# class Infame(http.Controller):
#     @http.route('/infame/infame/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infame/infame/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infame.listing', {
#             'root': '/infame/infame',
#             'objects': http.request.env['infame.infame'].search([]),
#         })

#     @http.route('/infame/infame/objects/<model("infame.infame"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infame.object', {
#             'object': obj
#         })
