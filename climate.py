# Hunter Downey 
# 6 - 5 - 2025
# Climate Data Functions for Analysis 

import pandas as pd
import os

def load_climate_data(data_folder, file_list):
    data_frames = []
    for file in file_list:
        df = pd.read_csv(os.path.join(data_folder, file), low_memory=False)
        station_name = file.replace("_climate_data.csv", "").capitalize()
        df["Station"] = station_name
        df["DATE"] = pd.to_datetime(df["DATE"], errors='coerce')
        df["Year"] = df["DATE"].dt.year
        df["Month"] = df["DATE"].dt.month
        df["MonthlyTotalLiquidPrecipitation"] = pd.to_numeric(df["MonthlyTotalLiquidPrecipitation"], errors='coerce')
        df["DYTS"] = pd.to_numeric(df["DYTS"], errors='coerce')
        data_frames.append(df)
    return pd.concat(data_frames)

def summarize_annual(data, column):
    grouped = data.groupby(["Year", "Station"])[column].sum().reset_index()
    avg = grouped.groupby("Year")[column].mean().reset_index()
    avg["Station"] = "Average"
    return pd.concat([grouped, avg])

def prep_annual_data(df, rename_dict):
    filtered = df[df["Year"] < 2025].copy()
    filtered["Station"] = filtered["Station"].replace(rename_dict)
    return filtered

def compute_monthly_average(df, column):
    return df.groupby("Month")[column].mean().reset_index()
