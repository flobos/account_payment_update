from odoo import api, fields, models, _

class account_payment_update_model(models.Model):

    _inherit = 'account.payment'

    tipo_pago = fields.Many2one('account.journal', string="Tipo doc.", required=True)
    cuenta = fields.Many2one('res.partner.bank', string="Cuenta", required=True)
    numero_doc = fields.Char(String="Numero doc.", required=True)
    fecha_cobro = fields.Date(string="Fecha cobro cheque", required=True)
    archivo_doc_pago = fields.Binary(string="Archivo doc.")
    fecha_pago = fields.Date(string="Fecha deposito")
    estado_cheque = fields.Selection([
        (1, "Cobrado"),
        (2, "Protestado"),
    ],string="Estado cheque")