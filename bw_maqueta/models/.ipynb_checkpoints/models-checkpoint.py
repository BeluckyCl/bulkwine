# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bw_maqueta(models.Model):
#     _name = 'bw_maqueta.bw_maqueta'
#     _description = 'bw_maqueta.bw_maqueta'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class crm_lead(models.Model):
    _inherit = 'crm.lead'
    bw_category = fields.Many2one(string="Categoría",
                                                 comodel_name='product.category', readonly=False,
                                                 website_form_blacklisted=False, track_visibility="onchange")
    