def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Display the result
    if final_price == price:
        print(f"No discount applied. The original price is: ${price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
