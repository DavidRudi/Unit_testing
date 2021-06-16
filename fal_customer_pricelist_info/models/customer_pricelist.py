from odoo import models, api, fields

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    customer_name = fields.Char(string='Customer Name')
    customer_ean = fields.Char(string='Customer EAN')
    customer_reference = fields.Char(string='Customer Reference')