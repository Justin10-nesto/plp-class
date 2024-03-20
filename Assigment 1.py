
def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    return price * (1 - discount_percent / 100)
  else:
    return price

print(calculate_discount(100, 15))