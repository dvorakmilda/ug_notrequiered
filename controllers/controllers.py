# -*- coding: utf-8 -*-
from odoo import http

# class UgNotrequiered(http.Controller):
#     @http.route('/ug_notrequiered/ug_notrequiered/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ug_notrequiered/ug_notrequiered/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ug_notrequiered.listing', {
#             'root': '/ug_notrequiered/ug_notrequiered',
#             'objects': http.request.env['ug_notrequiered.ug_notrequiered'].search([]),
#         })

#     @http.route('/ug_notrequiered/ug_notrequiered/objects/<model("ug_notrequiered.ug_notrequiered"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ug_notrequiered.object', {
#             'object': obj
#         })