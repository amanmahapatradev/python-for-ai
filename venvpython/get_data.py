from datetime import datetime, timedelta
import pandas as pd
import requests
import matplotlib.pyplot as plt
import os

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 48.85,
    "longitude": 2.35,
    "start_date": start_date,
    "end_date": end_date,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
}

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

daily_data = data["daily"]

df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)

df["date"] = pd.to_datetime(df["date"])

print(df)

#-------------------------------------------------------
#Create the plot


plt.figure(figsize=(10, 5))

# Plot maximum and minimum temperatures
plt.plot(
    df["date"],
    df["max_temp"],
    marker="o",
    color="#e74c3c",
    linewidth=2,
    label="Max Temp (°C)",
)
plt.plot(
    df["date"],
    df["min_temp"],
    marker="o",
    color="#3498db",
    linewidth=2,
    label="Min Temp (°C)",
)

# Optional: fill the area between min and max
plt.fill_between(
    df["date"], df["min_temp"], df["max_temp"], alpha=0.15, color="#e67e22"
)

# Formatting
plt.title("Daily Temperature Trends (Aug 22 - Aug 29, 2026)", fontsize=14, pad=12)
plt.xlabel("Date", fontsize=11)
plt.ylabel("Temperature (°C)", fontsize=11)
plt.xticks(df["date"], df["date"].dt.strftime("%b %d"), rotation=0)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(frameon=True)
plt.tight_layout()

plt.show()

#-------------------------------------------------------------------------------

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")            