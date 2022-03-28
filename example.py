from main import Taxation
myEmployee = Taxation(full_time=True, student_loan=False, hours_per_week=40, tax_year='2022-2023')
myEmployee.print_tax_ticket(27000,0)