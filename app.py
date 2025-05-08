import streamlit as st
from calculations import calculate_loan_payments
from plotting import plot_payment_breakdown
import pandas as pd
import io

# Function to generate Excel file
def generate_excel(df, loan_amount, monthly_payment, monthly_income):
    payment_percentage = (monthly_payment / monthly_income) * 100
    advisable = "Yes" if payment_percentage <= 30 else "No"

    # Creating Summary Table
    summary = pd.DataFrame({
        "Loan Amount (₪)": [loan_amount],
        "Monthly Payment (₪)": [monthly_payment],
        "Payment-to-Income Ratio (%)": [payment_percentage],
        "Is it advisable?": [advisable]
    })

    # Writing to Two Excel Sheets
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
        summary.to_excel(writer, index=False, sheet_name="Summary")
        df.to_excel(writer, index=False, sheet_name="Amortization Schedule")
    excel_buffer.seek(0)
    return excel_buffer

# Page Title
st.title("Loan Repayment Calculator")
st.write("""**Welcome to the Loan Repayment Simulator!**
This tool allows you to easily calculate your monthly loan repayments — no need to visit the bank or fill out long forms.
Simply adjust the loan amount, interest rate, and repayment period to get an instant estimate of your total and monthly payments.
It's a quick and user-friendly way to explore your loan options before making a decision.""")

# User Input
loan_amount = st.number_input("Loan Amount (₪)", min_value=1000, max_value=1000000, step=1000, value=40000)
loan_years = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=2)
interest_rate = st.slider("Annual Interest Rate (%)", 0.1, 15.0, step=0.1, value=5.0)
monthly_income = st.number_input("Your Monthly Income (₪)", min_value=1000, max_value=100000, step=500, value=8000)

# Calculating Payments and Amortization Schedule
monthly_payment, df = calculate_loan_payments(loan_amount, loan_years, interest_rate)
payment_percentage = (monthly_payment / monthly_income) * 100
advisable = "Yes ✅" if payment_percentage <= 30 else "No ❌"

# Displaying Results
st.subheader("Results:")
st.write(f"💸 Estimated Monthly Payment: **₪{monthly_payment:,.2f}**")
st.write(f"📊 Payment-to-Income Ratio: **{payment_percentage:.2f}%**")
st.write(f"📌 **Is it advisable to take this loan?** → **{advisable}**")

# Graph
st.subheader("📈 Monthly Payment Breakdown")
fig = plot_payment_breakdown(df)
st.pyplot(fig)

# Displaying Amortization Schedule
st.subheader("📅 Amortization Schedule")
st.dataframe(df, use_container_width=True)

# Downloading Excel File
if st.button("📥 Generate Excel File"):
    excel_file = generate_excel(df, loan_amount, monthly_payment, monthly_income)
    st.download_button("⬇️ Download Excel", data=excel_file,
                       file_name="loan_amortization_schedule.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
