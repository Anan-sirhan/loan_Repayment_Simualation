import streamlit as st
from calculations import calculate_loan_payments
from plotting import plot_payment_breakdown

st.title("Loan Repayment Calculator")

loan_amount = st.number_input("Loan Amount (₪)", min_value=1000, max_value=1000000, step=1000, value=40000)
loan_years = st.number_input("Loan Term (Years)", min_value=1, max_value=30, value=2)
interest_rate = st.slider("Annual Interest Rate (%)", 0.1, 15.0, step=0.1, value=5.0)
monthly_income = st.number_input("Your Monthly Income (₪)", min_value=1000, max_value=100000, step=500, value=8000)

monthly_payment, df = calculate_loan_payments(loan_amount, loan_years, interest_rate)
payment_percentage = (monthly_payment / monthly_income) * 100

st.subheader("Results:")
st.write(f"💸 Estimated Monthly Payment: **₪{monthly_payment:,.2f}**")
st.write(f"📊 Payment-to-Income Ratio: **{payment_percentage:.2f}%**")

if payment_percentage < 25:
    st.success("The payment is reasonable relative to your income ✅")
elif payment_percentage < 40:
    st.warning("The payment is getting relatively high ⚠️")
else:
    st.error("The payment is too high compared to your income 🚫")

st.subheader("📈 Monthly Payment Breakdown")
fig = plot_payment_breakdown(df)
st.pyplot(fig)

with st.expander("View Detailed Table"):
    st.dataframe(df.style.format({"Payment": "₪{:.2f}", "Principal": "₪{:.2f}", "Interest": "₪{:.2f}", "Remaining Balance": "₪{:.2f}"}))
