import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

st.set_page_config(page_title="Palivo vs mzdy", layout="wide")

# Dáta
data = {
    "Country": [
        "Luxembourg","Ireland","Austria","Denmark","Sweden",
        "Germany","Belgium","Netherlands","France","Spain",
        "Slovenia","Italy","Malta","Poland","Cyprus",
        "Lithuania","Estonia","Croatia","Czechia","Hungary",
        "Romania","Slovakia","Latvia","Bulgaria","Portugal","Greece"
    ],
    "Petrol_Liters": [
        3804,2463,2598,2384,2355,
        2247,2218,2032,1878,1881,
        1677,1604,1567,1554,1508,
        1288,1242,1235,1178,1068,
        1036,944,931,915,900,679
    ],
    "Diesel_Liters": [
        3750,2328,2466,2682,2111,
        2350,2020,2143,1864,1750,
        1628,1584,1736,1482,1331,
        1220,1249,1176,1252,1026,
        1016,990,925,821,930,799
    ]
}

df = pd.DataFrame(data)

# zoradenie
df = df.sort_values("Petrol_Liters", ascending=True)

# mzdy (správne mapovanie)
gross_salary_map = {
    "Luxembourg": 6900, "Ireland": 4500, "Austria": 4700, "Denmark": 5960,
    "Sweden": 4100, "Germany": 4550, "Belgium": 4300, "Netherlands": 4850,
    "France": 3960, "Spain": 2950, "Slovenia": 2850, "Italy": 3150,
    "Malta": 2100, "Poland": 2350, "Cyprus": 2400, "Lithuania": 2350,
    "Estonia": 2250, "Croatia": 2100, "Czechia": 2100, "Hungary": 1800,
    "Romania": 1850, "Slovakia": 1700, "Latvia": 1750, "Bulgaria": 1400,
    "Portugal": 1820, "Greece": 1450
}

df["Gross_Salary"] = df["Country"].map(gross_salary_map)

st.title("Koľko paliva si kúpiš za priemernú mzdu")

fig, ax = plt.subplots(figsize=(14, 10))

# farby
petrol_colors = ["red" if c == "Slovakia" else "steelblue" for c in df["Country"]]

# grafy
ax.barh(df["Country"], df["Petrol_Liters"], color=petrol_colors, alpha=0.9)
ax.barh(df["Country"], df["Diesel_Liters"], color="orange", alpha=0.5)

# mzdy (texty)
for i, row in enumerate(df.itertuples()):
    ax.text(
        40,
        i,
        f"{row.Gross_Salary:,} €".replace(",", " "),
        va="center",
        fontsize=9,
        fontweight="bold"
    )

ax.set_xlabel("Počet litrov za priemernú mzdu")
ax.set_ylabel("Krajina")

ax.grid(axis="x", linestyle="--", alpha=0.3)

legend_elements = [
    Patch(facecolor="steelblue", label="Benzín"),
    Patch(facecolor="orange", alpha=0.5, label="Diesel")
]

ax.legend(handles=legend_elements)

st.pyplot(fig)
