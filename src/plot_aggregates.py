import pandas as pd
import matplotlib.pyplot as plt

# load aggregated totals
monthly = pd.read_csv("data/monthly_totals.csv", parse_dates=["month"])
yearly  = pd.read_csv("data/yearly_totals.csv",  parse_dates=["year"])

# pivot so each company is its own column
m = monthly.pivot(index="month", columns="Name", values="total_amount")
y = yearly .pivot(index="year",  columns="Name", values="total_amount")

# plot monthly revenue
plt.figure(figsize=(10,5))
for company in m.columns:
    plt.plot(m.index, m[company], marker="o", label=company)
plt.title("Monthly Revenue by Company")
plt.ylabel("Total Amount")
plt.legend()
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

# plot yearly revenue
plt.figure(figsize=(8,4))
width = 0.35
years = y.index.year
for i, company in enumerate(y.columns):
    plt.bar(years + (i*width - width/2), y[company], width=width, label=company)
plt.title("Yearly Revenue by Company")
plt.ylabel("Total Amount")
plt.xticks(years)
plt.legend()
plt.tight_layout()
plt.savefig("yearly_revenue.png")

