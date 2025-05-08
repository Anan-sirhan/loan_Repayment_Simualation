
# Loan Repayment Calculator

## Overview

The Loan Repayment Calculator allows users to easily calculate monthly loan repayments. This tool provides an instant estimate of total and monthly payments based on input parameters such as loan amount, interest rate, and loan term. It also includes the option to download a detailed loan repayment schedule in both **PDF** and **Excel** formats.

## Features
- **Loan Repayment Calculator**: Provides the monthly repayment amount based on loan amount, annual interest rate, and loan term.
- **Payment-to-Income Ratio**: Displays the percentage of your monthly income spent on loan repayments.
- **Loan Repayment Schedule**: Users can visualize their monthly payment breakdown in a graph.
- **PDF Export**: Allows users to download loan repayment details in a PDF file.
- **Excel Export**: Allows users to download a detailed loan repayment schedule in an Excel file.

## How to Use

1. **Input Values**:
   - **Loan Amount (₪)**: The total loan amount you want to borrow.
   - **Loan Term (Years)**: The duration of the loan in years.
   - **Annual Interest Rate (%)**: The yearly interest rate of your loan.
   - **Your Monthly Income (₪)**: Your monthly income to evaluate your payment-to-income ratio.

2. **Results**:
   - The monthly repayment amount is calculated and displayed.
   - The payment-to-income ratio is calculated to indicate how much of your monthly income will go towards repaying the loan.
   - A breakdown of the monthly payments is visualized in a graph.

3. **Download Options**:
   - Click on **Generate PDF** to download the loan repayment details in PDF format.
   - Click on **Generate Excel File** to download the detailed loan repayment schedule in Excel format.

## File Exports

- **PDF Export**: The PDF file includes details of the loan amount, monthly payment, and repayment schedule summary.
- **Excel Export**: The Excel file includes a detailed loan repayment schedule with columns for the principal, interest, and remaining balance for each month, as well as the total loan amount and monthly payment.

## Installation Instructions

1. Install the necessary Python libraries:
   ```bash
   pip install streamlit pandas fpdf openpyxl
   ```

2. Save the script (e.g., `loan_calculator.py`).

3. Run the Streamlit app:
   ```bash
   streamlit run loan_calculator.py
   ```

4. Open the app in your browser and enter the required loan details.

## Example

1. Enter the **Loan Amount**, **Loan Term**, **Interest Rate**, and **Monthly Income** in the input fields.
2. View the **monthly payment** and **payment-to-income ratio** results.
3. Download the **loan repayment schedule** in PDF or Excel format by clicking the respective buttons.

## Code Overview

The app consists of the following functions:

- **generate_pdf**: Generates a PDF with loan repayment details and allows the user to download it.
- **generate_excel**: Generates an Excel file containing the loan repayment schedule.
- **calculate_loan_payments**: Calculates the monthly loan payments, total interest, and generates the repayment schedule.
- **plot_payment_breakdown**: Plots a graph showing the breakdown of the monthly loan payments.

## Contribution

Feel free to fork the repository, make changes, and create pull requests to improve the tool. If you encounter any issues, open an issue in the repository for support.
