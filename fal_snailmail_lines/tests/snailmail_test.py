from odoo.addons.snailmail_account.tests.test_pingen_send import TestPingenSend
from odoo.tests import tagged
import logging

_logger = logging.getLogger(__name__)

@tagged('cluedoo')
class SnailmailLinesTest(TestPingenSend):
    def setUp(self):
        invoices = []
        for i in range(2):
            invoice = []
            invoice.pingen_url = "https://stage-api.pingen.com/document/upload/token/30fc3947dbea4792eb12548b41ec8117/"
            invoice.sample_invoice = self.create_invoice()
            invoice.sample_invoice.partner_id.vat = "BE000000000"
            invoices.append(invoice)
            _logger.info(invoices.id,"ID Invoice")

        self.letter = self.env['account.invoice.send'].create({
            'invoice_ids': invoices,
            'is_merge': True,
            'snailmail_is_letter': True,
            'is_email': False,
            'is_print': False,
            })

        self.send_and_print_action()

        temp=[]
        for invoice in invoices:
            temp.append(invoice.id)

        snailmail = self.env['snailmail.letter']
        if (snailmail.search([('is_snailmail_merge','=',True)])):
            self.assertEquals(2, len(snailmail_records))
            for doc in range(len(invoices)):
                self.assertEquals(snailmail.snailmail_records[doc].document_id, temp[doc])
                self.assertEquals(snailmail.snailmail_records[doc].model_id, 'account.move')