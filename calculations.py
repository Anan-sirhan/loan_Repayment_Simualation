import numpy as np
import pandas as pd

def calculate_loan_payments(loan_amount, years, annual_rate):
    months = years * 12
    monthly_rate = annual_rate / 100 / 12

    if monthly_rate == 0:
        monthly_payment = loan_amount / months
    else:
        monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / \
                          ((1 + monthly_rate) ** months - 1)

    balance = loan_amount
    data = []

    for i in range(1, months + 1):
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance -= principal
        data.append([i, monthly_payment, principal, interest, max(balance, 0)])

    df = pd.DataFrame(data, columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance"])
    return monthly_payment, df
