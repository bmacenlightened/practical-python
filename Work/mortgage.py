# mortgage.py
#
# Exercise 1.7
# mortgage.py

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month = month + 1
    month_pay = payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        month_pay = month_pay + extra_payment

    if principal * (1+rate/12) < month_pay:
        month_pay = principal * (1+rate/12)

    principal = principal * (1+rate/12) - month_pay
    total_paid = total_paid + month_pay

    print(f"{month} {total_paid} {principal}")

print('Total paid', total_paid)