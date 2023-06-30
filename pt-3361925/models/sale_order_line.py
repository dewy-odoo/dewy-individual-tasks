import datetime
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_changed = fields.Boolean(compute='_compute_changed_price')
    
    @api.onchange('order_id.partner_id', 'price_unit')
    def _compute_changed_price(self):
        for record in self:
            prevItem = self.env['sale.order.line'].search_read(['&', ('order_partner_id.id', '=', record.order_id.partner_id.id),
                                                                ('product_id.id', '=', record.product_id.id),
                                                                # ('create_date', '<=', datetime.datetime.now()),
                                                                # ('price_unit', '!=', self.price_unit)
                                                                ],
                                                                order='__last_update desc', limit=1)
            if len(prevItem) > 0 and prevItem[0]['price_unit'] != self.price_unit:
                record.price_changed = True
            else:
                record.price_changed = False