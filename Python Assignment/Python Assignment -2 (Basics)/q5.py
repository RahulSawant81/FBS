# Selling price of book

cost_price = float(input("Enter the cost price of the book: "))
discount = float(input("Enter the discount percentage: "))


discount_amount = (discount / 100) * cost_price
selling_price = cost_price - discount_amount

print("Selling price of the book =", selling_price)

# Output:
# Enter the cost price of the book: 500
# Enter the discount percentage: 20
# Selling price of the book = 400.0

