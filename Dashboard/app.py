import streamlit as st
import pandas as pd
import plotly.express as px

# Load data with uppercase column names
df = pd.read_csv("cleaned_combined.csv", parse_dates=["LAUNCH_DATE"])

# ---------------- Sidebar Filters ----------------
st.sidebar.title("🔍 Filter Launch Data")
agencies = df["AGENCY"].unique().tolist()
agency_filter = st.sidebar.multiselect("Select Agency", agencies, default=agencies)

years = df["LAUNCH_DATE"].dt.year
year_range = st.sidebar.slider("Select Launch Year Range", int(years.min()), int(years.max()), (int(years.min()), int(years.max())))

status = st.sidebar.selectbox("Select Success Status", options=["All", "Success", "Failure"])

# Apply filters
filtered_df = df[df["AGENCY"].isin(agency_filter)]
filtered_df = filtered_df[filtered_df["LAUNCH_DATE"].dt.year.between(*year_range)]
if status == "Success":
    filtered_df = filtered_df[filtered_df["SUCCESS"] == True]
elif status == "Failure":
    filtered_df = filtered_df[filtered_df["SUCCESS"] == False]

# ---------------- Main Dashboard ----------------
st.title("🚀 Space Launch Tracker: ISRO vs SpaceX")

# KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric("🚀 Total Missions", len(filtered_df))
col2.metric("✅ Success Rate", f"{(filtered_df['SUCCESS'].mean() * 100):.2f}%" if not filtered_df.empty else "0.00%")
col3.metric("📅 Year Range", f"{filtered_df['LAUNCH_DATE'].dt.year.min()} - {filtered_df['LAUNCH_DATE'].dt.year.max()}")

# Mission Count by Agency
st.subheader("📊 Mission Count by Agency")
fig1 = px.histogram(filtered_df, x="AGENCY", color="SUCCESS", barmode="group", title="Mission Counts")
st.plotly_chart(fig1, use_container_width=True)

# Launches Over Time
st.subheader("📈 Launch Trend Over Time")
df_trend = filtered_df.groupby([filtered_df["LAUNCH_DATE"].dt.year, "AGENCY"]).size().reset_index(name="MISSIONS")
fig2 = px.line(df_trend, x="LAUNCH_DATE", y="MISSIONS", color="AGENCY", markers=True, labels={"LAUNCH_DATE": "Year"})
st.plotly_chart(fig2, use_container_width=True)

# Pie Chart: Successful Launches
st.subheader("🥧 Successful Missions Distribution")
success_df = filtered_df[filtered_df["SUCCESS"] == True]
fig3 = px.pie(success_df, names="AGENCY", title="Successful Launches by Agency")
st.plotly_chart(fig3)

# Data Table + Download
st.subheader("🧾 Launch Data Table")
st.dataframe(filtered_df)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Filtered Data", csv, "filtered_launch_data.csv", "text/csv")
