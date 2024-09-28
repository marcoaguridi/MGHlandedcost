from odoo import api, fields, models

class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    new_unit_cost_line_ids = fields.One2many('stock.landed.cost.new.unit', 'cost_id', string='New Unit Cost Lines')

    @api.onchange('picking_ids', 'cost_lines')
    def _onchange_recalculate_new_unit_cost(self):
        self.new_unit_cost_line_ids = [(5, 0, 0)]
        if self.picking_ids and self.cost_lines:
            products = self.picking_ids.mapped('move_lines.product_id')
            for product in products:
                moves = self.picking_ids.mapped('move_lines').filtered(lambda m: m.product_id == product)
                total_qty = sum(moves.mapped('product_uom_qty'))
                current_unit_cost = product.standard_price
                total_landed_cost = sum(self.cost_lines.mapped('price_unit'))
                new_unit_cost = current_unit_cost + (total_landed_cost / total_qty)
                
                self.new_unit_cost_line_ids = [(0, 0, {
                    'product_id': product.id,
                    'quantity': total_qty,
                    'current_unit_cost': current_unit_cost,
                    'new_unit_cost': new_unit_cost,
                })]

class StockLandedCostNewUnit(models.Model):
    _name = 'stock.landed.cost.new.unit'
    _description = 'New Unit Cost Calculation'

    cost_id = fields.Many2one('stock.landed.cost', string='Landed Cost')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity')
    current_unit_cost = fields.Float(string='Current Unit Cost')
    new_unit_cost = fields.Float(string='New Unit Cost')
