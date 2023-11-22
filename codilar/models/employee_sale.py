from odoo import models, fields, api


class Employees(models.Model):
    _name = 'employee.sale'

    Dep_name = fields.Many2one('employee.department', string='dep name')
    sale_amount = fields.Float(string="sale amount")
    sale_cost = fields.Float(string="sale cost")
    total = fields.Integer(string="total")
    result = fields.Integer(string="result" ,compute="_compute_total", store=True)
    recordd =fields.Integer(string="record")

    @api.onchange('sale_amount', 'sale_cost')
    def onchange_total_fields(self):
        for total in self:
            total.total = total.sale_cost + total.sale_amount

    def total_result(self):
        print("self",self)
        for record in self:
            record.total = record.sale_amount + record.sale_cost

    @api.depends('sale_amount', 'sale_cost')
    def _compute_total(self):
        for record in self:
            record.result = record.sale_amount + record.sale_cost
