from odoo.tests import common
from odoo.tests import tagged


@tagged('cluedoo')

class SelectFollowers(common.SavepointCase):
    def test_select_followers(self):
        active_id = self._context.get('active_id')
        model = self._context.get('active_model')
        select_tag = self.env['mail.compose.message'].create(
            {
                # "res_partner": "res.partner"
            })
        search_partner = self.env['res.partner'].search([])
        self.select_tag.with_context(
        		"active_id" : "partner.id",
        		"model" : "res.partner"
        	).get_followers()

        self.select_tag.with_context(
        		"active_id" : "partner.id",
        		"active_model" : "res.partner"
        	).send_mail()

        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
        print("Successs")


        # find_tags_mail = self.env['mail.followers'].search([('res_model', '=', model), ('res_id', '=', active_id)])

        # self.assertTrue(inventory.line_ids)

        # bikin mail.compose.message
        # search partner =(.search())
        # select_tag.with_context(isi active_id(partner.id),res.partner).get_followers
        # send_mail()
