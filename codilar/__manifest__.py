{
    'name': 'Employee',
    'version': '1.0',
    'sequence': -100,
    'author': 'vismaya',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_details.xml',
        'views/employee_department.xml',
        'views/employee_sale.xml',
        'views/employee_recruitment.xml',
        'data/mail_template.xml',
        'report/report.xml',
        'report/report_sale_order_temp.xml',
        'report/report_sale_order_add_field.xml'
    ]
}
