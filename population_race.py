import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.interpolate import make_interp_spline


# 1. Mock population data for 5 Western European countries over 20 years (2000-2020)
years = list(range(2000, 2021))
countries = ["Germany", "France", "United Kingdom", "Spain", "Italy"]

# Mock population data (in millions) for the last 20 years
population_data = {
    "Germany": [82, 82.5, 82.6, 82.4, 82.2, 82.0, 81.9, 82.1, 82.3, 82.5, 82.7, 82.8, 83.0, 83.2, 83.4, 83.6, 83.8, 84.0, 84.2, 84.4, 84.5],
    "France": [60.7, 61.0, 61.3, 61.6, 61.9, 62.2, 62.5, 62.8, 63.1, 63.4, 63.7, 64.0, 64.3, 64.6, 64.9, 65.2, 65.5, 65.8, 66.1, 66.3, 66.5],
    "United Kingdom": [58.8, 59.0, 59.3, 59.6, 59.9, 60.2, 60.5, 60.8, 61.1, 61.4, 61.7, 62.0, 62.3, 62.6, 62.9, 63.2, 63.5, 63.8, 64.1, 64.4, 64.6],
    "Spain": [40.7, 40.9, 41.2, 41.5, 41.8, 42.1, 42.4, 42.7, 43.0, 43.3, 43.6, 43.9, 44.2, 44.5, 44.8, 45.1, 45.4, 45.7, 46.0, 46.2, 46.4],
    "Italy": [57.0, 57.2, 57.4, 57.6, 57.8, 58.0, 58.2, 58.4, 58.6, 58.8, 59.0, 59.2, 59.4, 59.6, 59.8, 60.0, 60.2, 60.4, 60.6, 60.8, 61.0],
}

# Convert the data into a DataFrame for easier manipulation
df = pd.DataFrame(population_data, index=years)

# Since we want to remove the floats from the years, we'll skip interpolation
years_smooth = years  # Use integer years
df_smooth = df        # Use the original data

# 2. Setup the figure for the animated line chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot setup
ax.set_xlim(2000, 2020)
ax.set_ylim(40, 90)  # Assuming population range in millions
ax.set_title("Population Change in 5 Western European Countries (2000 - 2020)")
ax.set_xlabel("Year")
ax.set_ylabel("Population (in millions)")

# Initialize the lines for each country
lines = {}
for country in countries:
    line, = ax.plot([], [], label=country, lw=2)
    lines[country] = line

# Add the legend to the plot
ax.legend(loc="upper left")

# Set x-axis ticks to integer years
ax.set_xticks(years)
ax.set_xticklabels(years)

# 3. Update function for the animation
def update(frame):
    for country in countries:
        # Get data up to the current frame
        x_data = np.array(years_smooth[:frame + 1])
        y_data = np.array(df_smooth[country].iloc[:frame + 1])

        # Create a spline of the data
        if len(x_data) > 3:  # Need at least 4 points for spline
            x_smooth = np.linspace(x_data.min(), x_data.max(), 300)
            spline = make_interp_spline(x_data, y_data, k=3)
            y_smooth = spline(x_smooth)
            lines[country].set_data(x_smooth, y_smooth)
        else:
            lines[country].set_data(x_data, y_data)
    return lines.values()

# 4. Create the animation
anim = FuncAnimation(fig, update, frames=len(years_smooth), interval=500, blit=True)

# 5. Save the animation as an MP4 file
anim.save("western_europe_population_race.mp4", writer="ffmpeg", fps=2)

# 6. Show the animated plot
plt.show()