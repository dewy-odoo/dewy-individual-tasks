# DEWY - Scientific Consumables & Instrumentation : Color code the price is different from previous sale price
https://www.odoo.com/web#id=3361925&cids=3&menu_id=4720&action=4665&active_id=3361902&model=project.task&view_type=form

## Steps to complete the dev
- [X] Add a boolean computed field to store price changes in sale.order.line
- [X] Create the function to compute: find previous order lines for the customer and check for a different price
- [X] Add highlight to the view, with invisible tag if price isn't changed

## Issues/Blocking Points
- [X] Issue getting ORM to work with partner_id of sale.order and customer_id of sale.order.line
	# FIX: Needed to use order_id.partner_id, not company_id
- [X] Program was lagging when computing the field
	# FIX: Lowered the number of searches by better incorporating ORM
- [X] View wasn't updating correctly
	# FIX: Xpath was incorrect, had to overwrite inside the tree view (not form)

## Topics I need clarification on
N/A

## Interns who helped me
N/A

## Interns I helped
N/A
