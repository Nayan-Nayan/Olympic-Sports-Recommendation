import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Olympic Dashboard", page_icon="🏅")

st.title("🏅 Olympic Sports Analytics Dashboard")

# -------------------------
# LOAD DATA (NO CACHE FOR DEBUGGING)
# -------------------------
df = pd.read_csv("custom_olympic_dataset.csv")

# -------------------------
# DEBUG CHECK (REMOVE LATER)
# -------------------------


# -------------------------
# COUNTRY & SPORT SELECTION
# -------------------------
countries = sorted(df['Country'].dropna().unique())
selected_country = st.selectbox("🌍 Select Country", countries)

df_country = df[df['Country'] == selected_country]

sports = sorted(df_country['Sport'].dropna().unique())
selected_sport = st.selectbox("🏅 Select Sport", sports)

df_selected = df_country[df_country['Sport'] == selected_sport]

# -------------------------
# HANDLE EMPTY CASE
# -------------------------
if df_selected.empty:
    st.warning("No data available for this selection")
    st.stop()

# 👉 CRITICAL LINE
row = df_selected.iloc[0]

# -------------------------
# 🎯 SELECTED COMBO CLUSTER (FIX)
# -------------------------
st.subheader("🎯 Selected Country-Sport Cluster")

cluster_map = {
    0: "Emerging / Low Performance",
    1: "Consistent Performer",
    2: "High Performer",
    3: "Specialized Strong Sport"
}

if 'cluster' in df.columns:
    cluster_value = int(row['cluster'])
    cluster_name = cluster_map.get(cluster_value, "Unknown")

    st.success(f"{selected_country} - {selected_sport} → {cluster_name}")
else:
    st.error("Cluster column missing in dataset")



# -------------------------
# SAFE VALUES
# -------------------------
medals = int(row['medals_won']) if pd.notna(row['medals_won']) else 0
gold = int(row['gold_medals']) if pd.notna(row['gold_medals']) else 0
athletes = int(row['athletes_sent']) if pd.notna(row['athletes_sent']) else 0
years = int(row['participation_count']) if pd.notna(row['participation_count']) else 0
medal_rate = round(row['medal_rate'], 2) if pd.notna(row['medal_rate']) else 0

# -------------------------
# 💰 FUNDING RECOMMENDATION
# -------------------------
st.subheader("💰 Funding Allocation Recommendation")

# User input
total_budget = st.number_input(
    "Enter total Olympic funding (USD)",
    min_value=0.0,
    value=1000000.0,
    step=10000.0
)

# Normalize values (to avoid huge imbalance)
max_medals = df['medals_won'].max() if df['medals_won'].max() != 0 else 1
max_athletes = df['athletes_sent'].max() if df['athletes_sent'].max() != 0 else 1

medal_score = medals / max_medals
athlete_score = athletes / max_athletes
rate_score = medal_rate  # already between 0–1

# Weighted score (you can explain this in viva)
score = (0.5 * rate_score) + (0.3 * medal_score) + (0.2 * athlete_score)

# Convert to percentage (cap to avoid unrealistic values)
fund_percent = min(score * 100, 40)  # max 40% allocation

# Calculate amount
allocated_amount = (fund_percent / 100) * total_budget

# Display results
st.success(f"Recommended Funding: {round(fund_percent,2)}% of total budget")

st.info(f"💵 Allocate: ${round(allocated_amount,2):,}")
st.caption("⚠️ Funding recommendation is based on historical performance metrics.")

# Safe medal split
other_medals = max(medals - gold, 0)
silver = int(other_medals * 0.5)
bronze = other_medals - silver

# -------------------------
# DISPLAY STATS
# -------------------------
st.subheader(f"📊 {selected_country} - {selected_sport}")

col1, col2, col3 = st.columns(3)
col1.metric("🏅 Medal Rate", medal_rate)
col2.metric("🥇 Gold", gold)
col3.metric("🎯 Total Medals", medals)

col4, col5, col6 = st.columns(3)
col4.metric("🥈 Silver (est.)", silver)
col5.metric("🥉 Bronze (est.)", bronze)
col6.metric("👥 Athletes", athletes)

col7 = st.columns(1)[0]
col7.metric("📅 Olympic Appearances", years)

# -------------------------
# 🎯 SPORT-LEVEL CLUSTER
# -------------------------
# -------------------------
# 🎯 SPORT-LEVEL CLUSTER (VERY CLEAR)
# -------------------------

# 📊 TOP SPORTS
# -------------------------
st.subheader("📊 Top Sports (by Medal Rate)")

top_sports = df_country.sort_values(by='medal_rate', ascending=False).head(5)

fig, ax = plt.subplots()
ax.bar(top_sports['Sport'], top_sports['medal_rate'])
ax.set_ylabel("Medal Rate")
ax.set_title(f"{selected_country} Top Sports")

st.pyplot(fig)

# -------------------------
# 🥧 MEDAL DISTRIBUTION
# -------------------------
st.subheader("🥧 Medal Distribution")

if medals > 0:
    fig2, ax2 = plt.subplots()
    ax2.pie(
        [gold, silver, bronze],
        labels=["Gold", "Silver", "Bronze"],
        autopct='%1.1f%%'
    )
    st.pyplot(fig2)
else:
    st.info("No medals → pie chart not available")

# -------------------------
# ⚖️ COUNTRY COMPARISON
# -------------------------
st.subheader("⚖️ Compare Countries")

country2 = st.selectbox("Compare with", countries)

df2 = df[df['Country'] == country2]

compare = pd.DataFrame({
    "Country": [selected_country, country2],
    "Avg Medal Rate": [
        df_country['medal_rate'].mean(),
        df2['medal_rate'].mean()
    ]
})

st.bar_chart(compare.set_index("Country"))

# -------------------------
# 🧠 COUNTRY-LEVEL CLUSTER
# -------------------------
st.subheader("🧠 Overall Country Insight")

if 'cluster' in df.columns and not df_country['cluster'].isna().all():

    cluster_counts = df_country['cluster'].value_counts(normalize=True)

    for cluster_id, ratio in cluster_counts.items():
        st.info(f"{cluster_map.get(int(cluster_id), 'Unknown')}: {round(ratio*100,1)}% of sports")

else:
    st.warning("Cluster data not available")

# -------------------------