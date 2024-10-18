
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("data/bmw_electric_sales.xlsx")

plt.figure(figsize=(10, 6))
plt.bar(data['Year'], data['Sales In Unit'], color='skyblue')
plt.xticks(data['Year'])  # Set x-axis to display years
plt.title("BMW Electric I Series World-Wide Sales", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Sales In Unit")
plt.grid(False)


plt.tight_layout()
plt.savefig('img/bmw_sales_plot.png')
plt.show()

print("BMW sales plot saved as 'bmw_sales_plot.png'")
