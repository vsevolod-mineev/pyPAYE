# paye-calculator
A Python class which calculates PAYE, National Insurance (N.I.), Employer's N.I. and Student Loan Repayment Deductions for the U.K. tax system for 2016-2017, 2017-2018, 2018-2019, 2019-2020, 2020-2021, 2021-2022 and 2022-2023. 

This script has been updated and improved from the previous work done by Click Technology here: https://github.com/clicktechnology/pyPAYE
 
# Installation
 
You can install this script with...
```
pip install pyPAYE
```

# Usage

Create a file called `example.py` using an editor of your choice with the following content:
```
from main import Taxation
myEmployee = Taxation(full_time=True, student_loan=False, hours_per_week=40, tax_year='2022-2023')
myEmployee.print_tax_ticket(27000,0)
```
    
The result shown is..

```
Tax Receipt for tax year 2022-2023
----------------------------------------------
Gross Annual Pay                 : £ 27,000.00
Gross Monthly Pay                : £  2,250.00
PAYE                   (monthly) : £    240.50
Student Loans PLAN 0   (monthly) : £      0.00
Employee NI            (monthly) : £    189.03
Employer NI            (monthly) : £    224.50
----------------------------------------------
Net Monthly Pay        (monthly) : £  1,820.47
----------------------------------------------
Total Tax              (monthly) : £    654.03

```
In the root of the package, the file called test.py contains additional calculations and examples of the calculation of Employer's NI, Employee's NI and Student Loan Repayments for both Plan 1 and Plan 2 repayment options.
