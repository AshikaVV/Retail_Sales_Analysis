products = ["Shirt", "Jeans", "Kurti", "Saree", "Top"]
prices = [500, 900, 700, 1200, 400]
quantities = [10, 5, 8, 3, 12]

print("RETAIL SALES ANALYSIS")
print("_____________________")

# To Find total revenue

total_revenue = 0

for i in range(len(products)):
    revenue = prices[i] * quantities[i]
    total_revenue = total_revenue + revenue
    print(products[i], "Revenue:", revenue)

print("____________________")
print("Total Revenue:", total_revenue)

# To find Highest revenue product
 
Highest_Revenue = revenue
best_product = ""

for i in range(len(products)):
     revenue = prices[i] * quantities [i]

     if revenue > Highest_Revenue:
        Highest_revenue = revenue
        best_product = products[i]

print("Best Selling Product:", best_product)
print("Highest Revenue:", Highest_Revenue)

# Sales summary  report

revenues = []

for i in range(len(products)):
   revenue = prices[i] * quantities[i]
   revenues.append(revenue)

print("\n___ SALES SUMMARY REPORT ___")
print("Total Revenue:", sum(revenues))
print("Average Revenue:", sum(revenues) / len(revenues))
print("Highest Revenue:", max(revenues))
print("Lowest Revenue:", min(revenues))

# Final Sales Performance

print("\n" + "=" * 42)
print("FINAL SALES PERFORMANCE")
print("=" * 42)

print(f"{'Product':<15}{'Price(Rs.)':>12}{'Revenue(Rs.)':>15}")
print("-" * 42)

for i in range(len(products)):
    revenue = prices[i] * quantities[i]
    print(f"{products[i]:<15}{prices[i]:>12}{revenue:>15}")

print("-" * 42)
print(f"{'TOTAL REVENUE':<27}{sum(revenues):>15}")
print("-" * 42)

import matplotlib.pyplot as plt

revenues = [prices[i] * quantities[i]
            for i in range(len(products))]

plt.bar(products, revenues)
plt.title("Retail Sales Analysis")
plt.xlabel("products")
plt.ylabel("Revenue(Rs.)")
plt.tight_layout()
plt.show()
