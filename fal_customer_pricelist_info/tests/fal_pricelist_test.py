from odoo.addons.product.tests.test_pricelist import TestPricelist
from odoo.tests import tagged

@tagged('cluedoo')
class CustomerPricelistTest(TestPricelist):

	def setUp(self):
		res = super(CustomerPricelistTest, self).setUp()
		self.sale_pricelist_id = self.env['product.pricelist'].create({
            'name': 'Sale pricelist',
            'item_ids': [(0, 0, {
                'compute_price': 'formula',
                'base': 'list_price',
                'price_discount': 10,
                'product_id': self.usb_adapter.id,
                'applied_on': '0_product_variant',
                'customer_name':'test name',
				'customer_ean': 'test ean',
				'customer_reference': 'test reference',
            })]
        })
		return res
		