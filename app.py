import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Invoice Revenue Dashboard")

hist = pd.read_csv("data/monthly_totals.csv", parse_dates=["month"])
fcst = pd.read_csv("data/revenue_forecast.csv", parse_dates=["ds"])

companies = hist['Name'].unique().tolist()
sel = st.multiselect("Select companies", companies, default=companies)

filtered_hist = hist[hist['Name'].isin(sel)]
filtered_fcst = fcst[fcst['Name'].isin(sel)]

H = filtered_hist.pivot(index='month', columns='Name', values='total_amount')
F = filtered_fcst.pivot(index='ds', columns='Name', values='forecast')

fig, ax = plt.subplots(figsize=(10, 6))
for comp in H.columns:
    ax.plot(H.index, H[comp], label=f"{comp} history")
    ax.plot(F.index, F[comp], "--", label=f"{comp} forecast")
ax.set_title("Historical & 12-Month Revenue Forecast")
ax.set_xlabel("Date")
ax.set_ylabel("Amount Including Tax")
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Historical Data")
    st.dataframe(filtered_hist)
with col2:
    st.subheader("Forecast Data")
    st.dataframe(filtered_fcst)
