import pandas as pd
import matplotlib.pyplot as plt

hist = pd.read_csv("data/monthly_totals.csv", parse_dates=["month"])
fcst = pd.read_csv("data/revenue_forecast.csv", parse_dates=["ds"])

H = hist.pivot(index="month", columns="Name", values="total_amount")
F = fcst .pivot(index="ds",    columns="Name", values="forecast")

plt.figure(figsize=(10,6))
for comp in H.columns:
    plt.plot(H.index, H[comp],      label=f"{comp} (history)")
    plt.plot(F.index, F[comp], "--", label=f"{comp} (forecast)")
plt.title("Historical & 12-Month Revenue Forecast")
plt.xlabel("Date")
plt.ylabel("Amount Including Tax")
plt.legend()
plt.tight_layout()
plt.savefig("rev_history_forecast.png")

