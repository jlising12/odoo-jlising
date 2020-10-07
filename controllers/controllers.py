# -*- coding: utf-8 -*-
# from odoo import http


# class RequestReferencePo(http.Controller):
#     @http.route('/request_reference_po/request_reference_po/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/request_reference_po/request_reference_po/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('request_reference_po.listing', {
#             'root': '/request_reference_po/request_reference_po',
#             'objects': http.request.env['request_reference_po.request_reference_po'].search([]),
#         })

#     @http.route('/request_reference_po/request_reference_po/objects/<model("request_reference_po.request_reference_po"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('request_reference_po.object', {
#             'object': obj
#         })
