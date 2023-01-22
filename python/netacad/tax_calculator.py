income = float(input("Enter the annual income: "))

#
# Write your code here.
#
# this is the limit where tax is differently calculated
HIGH_TAX_POINT = 85528

if income > HIGH_TAX_POINT:
    # add 14839.02 to 32% of income over the limit 
    tax = (income - HIGH_TAX_POINT) * 32 / 100 + 14839.02
else:
    # subtract 556.02 from the 18% of income
    tax = income * 18 / 100 - 556.02

# for tax less than 0 assign 0.0 as the tax 
if tax < 0: tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
