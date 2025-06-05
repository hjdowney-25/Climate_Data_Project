# Hunter Downey 
# 6 - 5 - 2025
# Climate Data Workflow

from climate import load_climate_data, summarize_annual, prep_annual_data, compute_monthly_average
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# File setup
data_folder = "data"
file_list = [
    "fondy_climate_data.csv",
    "gb_climate_data.csv",
    "oshkosh_climate_data.csv",
    "sheboygan_climate_data.csv"
]
rename_dict = {
    "Fondy": "Fond Du Lac",
    "Gb": "Green Bay"
}

# Load and prepare data
climate_data = load_climate_data(data_folder, file_list)
precip_summary = summarize_annual(climate_data, "MonthlyTotalLiquidPrecipitation")
filtered_data = prep_annual_data(precip_summary, rename_dict)

# Step 3: Lineplot (excluding average)
station_only = filtered_data[filtered_data["Station"] != "Average"]

plt.figure(figsize=(12, 6))
sns.lineplot(data=station_only, x="Year", y="MonthlyTotalLiquidPrecipitation", hue="Station", marker="o")
plt.title("Total Annual Precipitation by Station \n in Northeast WI from 2010 - 2024 ", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Precipitation (inches)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title="Station", fontsize=12, title_fontsize=13)
plt.grid(True)
plt.tight_layout()
plt.savefig("images/precip_by_station_trend.png")
plt.show()

# Step 4: Create separate barplot for the average only
avg_only = filtered_data[filtered_data["Station"] == "Average"]

plt.figure(figsize=(12, 6))
sns.barplot(data=avg_only, x="Year", y="MonthlyTotalLiquidPrecipitation", color="steelblue")
plt.title("Average Total Annual Precipitation \n in Northeast WI from 2010 - 2024", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Avg. Precipitation (inches)", fontsize=14)
plt.xticks(rotation=45, fontsize=11)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("images/average_annual_precip_barplot.png")
plt.show()

# Thunderstorm plots
tstorm_summary = summarize_annual(climate_data, "DYTS")
tstorm_filtered = prep_annual_data(tstorm_summary, rename_dict)

# --- Lineplot: Thunderstorm Days by Station ---
tstorm_station_only = tstorm_filtered[tstorm_filtered["Station"] != "Average"]

plt.figure(figsize=(12, 6))
sns.lineplot(data=tstorm_station_only, x="Year", y="DYTS", hue="Station", marker="o")
plt.title("Total Days with Thunderstorms by Station \n in Northeast WI from 2010 - 2024", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Thunderstorm Days", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title="Station", fontsize=12, title_fontsize=13)
plt.grid(True)
plt.tight_layout()
plt.savefig("images/tstorm_by_station_trend.png")
plt.show()

# --- Barplot: Average Thunderstorm Days ---
tstorm_avg_only = tstorm_filtered[tstorm_filtered["Station"] == "Average"]

plt.figure(figsize=(12, 6))
sns.barplot(data=tstorm_avg_only, x="Year", y="DYTS", color="steelblue")
plt.title("Average Annual Thunderstorm Days \n in Northeast WI from 2010 - 2024", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Avg. Thunderstorm Days", fontsize=14)
plt.xticks(rotation=45, fontsize=11)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("images/average_annual_tstorm_barplot.png")
plt.show()

# Monthly averages
monthly_precip = compute_monthly_average(climate_data, "MonthlyTotalLiquidPrecipitation")
monthly_tstorms = compute_monthly_average(climate_data, "DYTS")

# Bar plot: Monthly Avg Precipitation
plt.figure(figsize=(10, 5))
sns.barplot(data=monthly_precip, x="Month", y="MonthlyTotalLiquidPrecipitation", color="steelblue")
plt.title("Average Monthly Precipitation \n in Northeast WI from 2010 - 2024", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Avg. Precipitation (inches)", fontsize=14)
plt.xticks(ticks=np.arange(0, 12), labels=[
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
], fontsize=11)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("images/monthly_avg_precip_barplot.png")
plt.show()

# Bar plot: Monthly Avg Thunderstorm Days
plt.figure(figsize=(10, 5))
sns.barplot(data=monthly_tstorms, x="Month", y="DYTS", color="darkorange")
plt.title("Average Monthly Thunderstorm Days \n in Northeast WI from 2010 - 2024", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Avg. Thunderstorm Days", fontsize=14)
plt.xticks(ticks=np.arange(0, 12), labels=[
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
], fontsize=11)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("images/monthly_avg_tstorm_barplot.png")
plt.show()
