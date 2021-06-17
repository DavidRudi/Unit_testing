from odoo.tests import tagged
from odoo.tests import common

import logging

_logger = logging.getLogger(__name__)

@tagged('cluedoo')
class SnailmailLinesTest(common.SingleTransactionCase):
    def test_snail_mail_merge(self):
        invoices = [self.env.ref('l10n_generic_coa.demo_invoice_3').id, self.env.ref('l10n_generic_coa.demo_invoice_2').id]

        self.wizard_invoice_send = self.env['account.invoice.send'].with_context({'active_ids':invoices}).create({
            # 'invoice_ids': invoices,
            'is_merge': True,
            'snailmail_is_letter': True,
            'is_email': False,
            'is_print': False,
            })

        result = self.wizard_invoice_send.send_and_print_action()

        temp=[]
        for invoice in invoices:
            temp.append(invoice)

        snailmail = self.env['snailmail.letter']
        print("XXXXXXXXXXXXXXXXXXX")
        print(result)
        if (snailmail.search([('is_snailmail_merge','=',True)])):
            print("XXXXXXXXXXXXXXXXXXX 2")
            self.assertEquals(2, len(snailmail_records))
            for doc in range(len(invoices)):
                print("XXXXXXXXXXXXXXXXXXX 3")
                self.assertEquals(snailmail.snailmail_records[doc].document_id, temp[doc])
                self.assertEquals(snailmail.snailmail_records[doc].model_id, 'account.move')
