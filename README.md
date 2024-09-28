This module does the following:

Extends the stock.landed.cost model to include a new One2many field new_unit_cost_line_ids.
Creates a new model stock.landed.cost.new.unit to store the new unit cost calculations.
Adds an onchange method to recalculate the new unit costs whenever the pickings or cost lines change.
Extends the stock landed cost form view to include a new tab "New Unitary Cost" with a table showing the calculated new unit costs.

The new unit cost is calculated by:

Summing up the total quantity of each product across all selected pickings.
Getting the current unit cost of the product.
Calculating the total landed cost (sum of all cost lines).
Calculating the new unit cost as: current unit cost + (total landed cost / total quantity)

To use this module:

Place the extended_landed_cost folder in your Odoo addons directory.
Update the addons list in Odoo.
Install the module from the Odoo Apps menu.

After installation, you'll see a new tab in the Stock Landed Cost form view called "New Unitary Cost". This tab will show a table with the products, their quantities, current unit costs, and calculated new unit costs based on the landed cost lines.
