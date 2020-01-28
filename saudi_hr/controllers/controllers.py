# -*- coding: utf-8 -*-
from odoo import http

# class SaudiHr(http.Controller):
#     @http.route('/saudi_hr/saudi_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saudi_hr/saudi_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saudi_hr.listing', {
#             'root': '/saudi_hr/saudi_hr',
#             'objects': http.request.env['saudi_hr.saudi_hr'].search([]),
#         })

#     @http.route('/saudi_hr/saudi_hr/objects/<model("saudi_hr.saudi_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saudi_hr.object', {
#             'object': obj
#         })