from odoo import fields, models,api,_
from odoo.exceptions import UserError
from odoo.tools.misc import formatLang, format_date, get_lang

from uuid import uuid4
import qrcode
import base64
import logging
from odoo.addons import decimal_precision as dp

from lxml import etree

from odoo import fields, models
import requests
import json
from datetime import datetime,date
import convert_numbers


class AccountMove(models.Model):
    _inherit = 'account.move'
    _order = "invoice_nat_times desc"




    def action_invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        if any(not move.is_invoice(include_receipts=True) for move in self):
            raise UserError(_("Only invoices could be printed."))

        self.filtered(lambda inv: not inv.is_move_sent).write({'is_move_sent': True})
        if self.user_has_groups('account.group_account_invoice'):
            print('yashhhhhh')
            # return self.env.ref('account.account_invoices').report_action(self)
            return self.env.ref('natcom_dec_last.natcom_natcom_dec_view').report_action(self)
        else:
            return self.env.ref('account.account_invoices_without_payment').report_action(self)




