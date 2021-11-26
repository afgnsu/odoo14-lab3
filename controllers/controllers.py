# -*- coding: utf-8 -*-
# from odoo import http


# class Lab3(http.Controller):
#     @http.route('/lab3/lab3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lab3/lab3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lab3.listing', {
#             'root': '/lab3/lab3',
#             'objects': http.request.env['lab3.lab3'].search([]),
#         })

#     @http.route('/lab3/lab3/objects/<model("lab3.lab3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lab3.object', {
#             'object': obj
#         })
