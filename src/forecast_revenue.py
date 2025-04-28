import pandas as pd
from prophet import Prophet
import pathlib

IN  = pathlib.Path("data/monthly_totals.csv")
OUT = pathlib.Path("data/revenue_forecast.csv")

df = pd.read_csv(IN, parse_dates=["month"])
results = []

for name, group in df.groupby("Name"):
    m = group.rename(columns={"month":"ds", "total_amount":"y"})[["ds","y"]]
    model = Prophet(yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=False)
    model.fit(m)
    future = model.make_future_dataframe(periods=12, freq="MS")
    fcst = model.predict(future)[["ds","yhat"]].tail(12)
    fcst["Name"] = name
    results.append(fcst.rename(columns={"yhat":"forecast"}))

out_df = pd.concat(results)
out_df.to_csv(OUT, index=False)
print(f"✅ 12-month revenue forecast saved to {OUT}")

