# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
import base64





class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_rfq_send(self):
        res=super(PurchaseOrder, self).action_rfq_send()
        pdf = self.env.ref('stock.action_report_delivery').sudo()._render_qweb_pdf([self.picking_ids.id])[0]
        b64_pdf = base64.encodebytes(pdf)
        # name="delivery_note"
        attachment = self.env['ir.attachment'].create({
            'name': self.picking_ids.name + '.pdf',
            'type': 'binary',
            'datas': b64_pdf,
            'res_model': 'stock.picking',
            'res_id': self.picking_ids.id,
            'mimetype': 'application/x-pdf'
        })
        template_id = self.env.ref('purchase.email_template_edi_purchase_done').id
        template = self.env['mail.template'].browse(template_id)
        template.attachment_ids = [attachment.id]
        return res
