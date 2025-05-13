# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        print("Sorry, No discount for you.")
        return price

# User input
price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))


# Function call
final_price = calculate_discount(price, discount)

# Print final result
print("Final price: $" + str(final_price))
