# Columbia FinTech Module 1 Challenge

import csv
from pathlib import Path


print("------------------------------------------------")
print("PART 1: Automate the Calculations               ")
print("------------------------------------------------")
print()

# Given the following loan cost (list)...
loan_costs = [500, 600, 200, 1000, 450]

#Calculate the total number of loans in the list and print.
total_num_loans = len(loan_costs)
print("Total number of loans : ", total_num_loans)

# Calculate the total of all loans in the list and print
total_sum_loans = sum(loan_costs)
print("Total sum of all loans : ", total_sum_loans)

# Calculate the average loan price and print.
avg_loan_price = total_sum_loans / total_num_loans;
print("Average loan price: ", round(avg_loan_price,2))
print()


print("------------------------------------------------")
print("PART 2: Analyze Loan Data")
print("------------------------------------------------")
print()

# Given the following loan data (dictionary)...
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Print all the loan details...
print("Loan Details")
print("------------")
# "get" the loan_price from the loan data dictionary and print.
loan_price = loan.get("loan_price")
print("Loan Price :", loan_price)

# "get" the future_value from the loan data dictionary and print.
future_value = loan.get("future_value")
print("Future value :", future_value)

# "get" the remaining_months from the loan data dictionary and print.
remaining_months = loan.get("remaining_months")
print("Remaining months :", remaining_months)

# discount rate = minimum required return = 20%
discount_rate = 0.20
print("Discount Rate :", discount_rate)

# Compute the present value of the future value, at the discount_rate, with remaining months of the loan = remaining_months
present_value = future_value / (1 + (discount_rate / 12)) ** remaining_months

# Print to the user the discount rate used and the computed present value of the loan
print("Present value :", round(present_value,2))
print()

# If the present value of the loan is greater than or equal to the loan price, then print a message that says the loan is worth at least the cost to buy it.
# else, if the present value of the loan is less than the loan loan price, then print a message that says that the loan is too expensive and not worth the price.
if (present_value >= loan_price):
   print("*** The loan is worth at least the cost to buy it")
else:
   print("***The loan is too expensive and not worth the price")
print()


print("------------------------------------------------")
print("PART 3: Perform Financial Calculations          ")
print("------------------------------------------------")
print()

# Given the following loan data (dictionary)...
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Function that will calculate the present value of a loan
#    Input parameters: future value, remaining months, and annual discount rate
#    Output (Return) values: present value
def get_present_value(future_value, remaining_months, annual_discount_rate):
   present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
   return present_value

# Get the loan details from dictionary and store in its own variable
# (note, could of applied the .get methods directly in the parameter list of the function -
#  but I preferred to store local variables of each loan component.)

# "get" the future_value from the new loan data dictionary.
future_value = new_loan.get("future_value")
# "get" the remaining_months from the new loan data dictionary.
remaining_months = new_loan.get("remaining_months")
# annual_discount_rate rate = 20%
annual_discount_rate = 0.2

# Call the get_present_value function, assign the returned result to present_value and print.
present_value = get_present_value(future_value, remaining_months, annual_discount_rate)
print(f"The present value of the loan is: {round(present_value,2)}")
print()


print("------------------------------------------------")
print("PART 4: Conditionally filter lists of loans     ")
print("------------------------------------------------")
print()

# Given the following list of loan data (list of loan data dictionary)...
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list to hold the inexpensive lists
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
max_loan_price = 500    # set the max $ value for the loan willing to accept = $500
for loan in loans:
   # "get" the loan_price from the loans dictionary.
   loan_price = loan.get("loan_price")
   # If the loan price is less than the maximum acceptable loan price, add to the inexpensive_loans list
   if (loan_price <= max_loan_price):
      inexpensive_loans.append(loan)

# Loop through the `inexpensive_loans` list, and print the loan details
print("Inexpensive Loans:")
for inexpensive_loan in inexpensive_loans:
   print(inexpensive_loan)
print()


print("------------------------------------------------")
print("PART 5: Save the results                        ")
print("------------------------------------------------")
print()

# Set the output header of the csv file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# Open the csv file for "writing"
with open(output_path, 'w', newline='') as csvfile:
   # Use the "csv" module/library methods to allow writing to the csc file inexpensive_loans.csv
   csvwriter = csv.writer(csvfile)
   csvwriter.writerow(header)

   # Loop through the inexpensive_loans list of loans and write to the csv file in comma delimited form
   for inexpensive_loan in inexpensive_loans:
      csvwriter.writerow(inexpensive_loan.values())

# Report to the user (console) that the csv file has been saved/written
print("(Results saved to inexpensive_loans.csv file)")
print()


print("------------------------------------------------")
print("FINISHED!                                       ")
print("------------------------------------------------")
print()
print()


