import pandas as pd
import pathlib

IN_PATH   = pathlib.Path("data/invoices_clean.parquet")
OUT_MONTH = pathlib.Path("data/monthly_totals.csv")
OUT_YEAR  = pathlib.Path("data/yearly_totals.csv")

df = pd.read_parquet(IN_PATH)

mask_argas = df["Name"].str.contains("ARGAS", case=False, na=False)
mask_bgp   = df["Name"].str.contains("BGP ARABIA", case=False, na=False)
df = df[mask_argas | mask_bgp]

df["Invoice Date"] = pd.to_datetime(df["Invoice Date"])
df["month"] = df["Invoice Date"].dt.to_period("M").dt.to_timestamp()
df["year"]  = df["Invoice Date"].dt.to_period("Y").dt.to_timestamp()

monthly = (
    df.groupby(["Name", "month"])["Amount Including Tax [C=A+B]"]
      .sum()
      .reset_index()
      .rename(columns={"Amount Including Tax [C=A+B]": "total_amount"})
)
monthly.to_csv(OUT_MONTH, index=False)
print(f"✅ Monthly totals saved to {OUT_MONTH}")

yearly = (
    df.groupby(["Name", "year"])["Amount Including Tax [C=A+B]"]
      .sum()
      .reset_index()
      .rename(columns={"Amount Including Tax [C=A+B]": "total_amount"})
)
yearly.to_csv(OUT_YEAR, index=False)
print(f"✅ Yearly totals saved to {OUT_YEAR}")
