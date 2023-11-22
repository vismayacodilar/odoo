from odoo import models, fields


class Employee(models.Model):
    _name = 'employee.details'

    name = fields.Char(string="Emp name")
    email = fields.Char(string="email")
    age = fields.Integer(string="age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    company = fields.Many2one('res.company')
    address = fields.Char(string="address")
    phone_number = fields.Char(string="Phone number")
    description = fields.Text(string="Description")
    personal_email = fields.Char(string="personal email")

    def action_email_send(self):
        for rec in self:
            rec.env.ref('codilar.email_template_name').send_mail(rec.id, force_send=True)
