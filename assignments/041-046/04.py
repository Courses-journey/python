country = input("Input Your Country: ")
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30


if country in countries:
  print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
else:
  print("Your Country Not Eligible For Discount And The Price Is $100")