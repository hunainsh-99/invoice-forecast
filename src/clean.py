import pandas as pd
import pathlib

RAW = pathlib.Path("data/InvoiceList.xlsx")
CLEAN = pathlib.Path("data/invoices_clean.parquet")

df = pd.read_excel(RAW, header=1)
df.columns = [c.strip().replace("\n", " ") for c in df.columns]
df["Invoice Date"] = pd.to_datetime(df["Invoice Date"], format="%d-%b-%Y")

num_cols = [
    "Amount Excluding Tax [A]",
    "Tax Amount [B]",
    "Amount Including Tax [C=A+B]",
    "Paid As of Now",
    "Due As of Now"
]
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce")

df.to_parquet(CLEAN, index=False)
print(f"✅ Cleaned data saved to {CLEAN}")


