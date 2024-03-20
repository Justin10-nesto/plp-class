# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price = 0, discount_percent= 0):
   
  if not (price and discount_percent):
      price = float(input("Enter the price of the item: "))
      discount_percent = float(input("Enter the discount percentage: "))
      return calculate_discount(price, discount_percent)
  
  if discount_percent >= 20:
    return price * (1 - discount_percent / 100)
  else:
    return price

fiinal_price =calculate_discount()
print("The final price is:", fiinal_price)