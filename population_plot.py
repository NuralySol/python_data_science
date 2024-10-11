import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

#! Script for bar chart racing!
# 1. Mock population data for the top 10 most populous countries over 10 years (2013-2022)
years = list(range(2013, 2023))
countries = [
    "China",
    "India",
    "United States",
    "Indonesia",
    "Pakistan",
    "Brazil",
    "Nigeria",
    "Bangladesh",
    "Russia",
    "Mexico",
]

#! Mock population data (in millions) for the last 10 years can be an API 
population_data = {
    "China": [1370, 1379, 1386, 1392, 1398, 1403, 1406, 1409, 1411, 1412],
    "India": [1250, 1276, 1302, 1327, 1353, 1378, 1401, 1424, 1447, 1469],
    "United States": [316, 319, 321, 324, 326, 328, 331, 333, 335, 337],
    "Indonesia": [250, 255, 260, 265, 270, 273, 276, 279, 281, 284],
    "Pakistan": [182, 187, 193, 199, 205, 211, 216, 220, 224, 229],
    "Brazil": [200, 202, 204, 206, 208, 210, 211, 212, 213, 214],
    "Nigeria": [174, 179, 185, 190, 196, 201, 206, 211, 216, 221],
    "Bangladesh": [156, 159, 162, 165, 168, 171, 174, 177, 179, 181],
    "Russia": [143, 143, 143, 144, 144, 145, 146, 146, 146, 147],
    "Mexico": [122, 123, 125, 126, 128, 129, 130, 131, 132, 133],
}

# Convert the data into a DataFrame for easier manipulation
df = pd.DataFrame(population_data, index=years)

# 2. Setup the figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 1600)  # Set x-axis range (for population in millions)
ax.set_ylim(-0.5, 9.5)  # Set y-axis range (10 countries)

# Keep track of the previous rankings to detect overtakes
previous_ranks = df.loc[2013].sort_values(ascending=True).index.tolist()

# Function to smoothly transition bars
def interpolate_bars(data1, data2, fraction):
    return data1 + (data2 - data1) * fraction

# 3. Function to update the plot for each year
def update(frame):
    global previous_ranks  # Declare the global variable
    ax.clear()
    year = int(frame)  # Remove the fractional part of the year

    # Interpolate between two consecutive years for smoother transition
    if year < 2022:
        year_fraction = frame % 1  # Get the fraction of the year to control smoothness
        current_year_data = df.loc[year]
        next_year_data = df.loc[year + 1]
        data = interpolate_bars(current_year_data, next_year_data, year_fraction)
    else:
        data = df.loc[year]

    # Sort countries by interpolated population for the current frame
    sorted_data = data.sort_values(ascending=True)

    # Smooth bar color transitions using the frame number for slight fade effects
    bar_colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(countries)))

    # Animate bar positions: Interpolate y positions when countries overtake
    current_ranks = sorted_data.index.tolist()

    # Check for overtakes and highlight changes
    highlighted_colors = []
    for i, country in enumerate(current_ranks):
        if previous_ranks.index(country) != i:
            highlighted_colors.append("orange")  # Flash bar in orange if there's an overtake
        else:
            highlighted_colors.append(bar_colors[i])  # Otherwise, use normal colors

    # Create the bar chart with potential highlights
    bars = ax.barh(sorted_data.index, sorted_data.values, color=highlighted_colors)

    # Annotate bars with population values
    for i, (bar, value) in enumerate(zip(bars, sorted_data.values)):
        ax.text(value + 10, bar.get_y() + bar.get_height() / 2, f"{value:.0f}", va="center")

    # Add titles and labels
    ax.set_title(f"Top 10 Countries by Population in {year}", fontsize=16)  # Only integer year
    ax.set_xlabel("Population (millions)")
    ax.set_ylabel("Countries")

    # Save the current rankings for the next frame to detect changes
    previous_ranks = current_ranks

    ax.set_xlim(0, 1600)

# 4. Create the animation using FuncAnimation
frames = np.arange(2013, 2023, 0.1)  # Interpolate between years for smoother transition
anim = FuncAnimation(fig, update, frames=frames, repeat=False, interval=100)

# 5. Save the animation as an MP4 with higher fps
anim.save("top_10_countries_population.mp4", writer="ffmpeg", fps=30)

plt.show()