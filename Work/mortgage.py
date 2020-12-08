# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
i=0

while principal > 0:
    i+=1
    if i==extra_payment_start_month:
        for j in range(extra_payment_end_month-extra_payment_start_month):
            principal = principal * (1+rate/12) - payment - extra_payment
            total_paid = total_paid + payment + extra_payment
            print(f'{i:<10} ${total_paid:<25} ${principal}')
            i+=1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(f'{i:<10} ${total_paid:<25} ${principal}')
if principal<0:
    total_paid=total_paid+principal
print(f'Total paid : ${total_paid}')
print(f'Months : {i}')