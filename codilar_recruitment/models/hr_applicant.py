from odoo import models, fields


class employee(models.Model):
    _inherit = 'hr.applicant'
    personal_phone = fields.Char(string="personal phone")