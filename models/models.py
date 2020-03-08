# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ug_account_analytic_line(models.Model):
    _inherit = 'account.analytic.line'
    name = fields.Char(required=False )
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100