products = ["Shirt", "Jeans", "Kurti", "Saree", "Top"]
prices = [500, 900, 700, 1200, 400]
quantities = [10, 5, 8, 3, 12]

print("RETAIL SALES ANALYSIS")
print("_____________________")

total_revenue = 0

for i in range(len(products)):
    revenue = prices[i] * quantities[i]
    total_revenue = total_revenue + revenue
    print(products[i], "Revenue:", revenue)

print("____________________")
print("Total Revenue:", total_revenue)
