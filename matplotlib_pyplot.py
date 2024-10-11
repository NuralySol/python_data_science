import pandas as pd
import matplotlib.pyplot as plt
import pprint as pp
import requests

# 1. Function to fetch country data (for Taiwan in this case)
def get_country_data(country):
    url = f"https://restcountries.com/v3.1/name/{country.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        country_info = response.json()[0]  # Get the first result
        return {
            'Country': country_info.get('name', {}).get('common', 'N/A'),
            'Population': country_info.get('population', 'N/A'),
            'Area_km2': country_info.get('area', 'N/A'),
            'Capital': country_info.get('capital', ['N/A'])[0],
            'Region': country_info.get('region', 'N/A'),
            'Subregion': country_info.get('subregion', 'N/A')
        }
    else:
        return {
            'Country': 'N/A',
            'Population': 'N/A',
            'Area_km2': 'N/A',
            'Capital': 'N/A',
            'Region': 'N/A',
            'Subregion': 'N/A'
        }

# 2. Fetch data for Taiwan
taiwan_data = get_country_data('Taiwan')

# 3. Pretty print the data for better readability
print("Data for Taiwan fetched from the REST Countries API:")
pp.pprint(taiwan_data)

#! 4. Mock-up population change over the years (historical data) (here it is a seed, and used as an example)
years = [2010, 2012, 2014, 2016, 2018, 2020, 2022]
populations = [18000000, 20100000, 22200000, 24300000, 25400000, 27500000, taiwan_data['Population']]

# 5. Create a DataFrame to hold the population data
df_population = pd.DataFrame({
    'Year': years,
    'Population': populations
})

# 6. Plot the population change over the years as a bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df_population['Year'], df_population['Population'], color='blue', label='Population')

# Add titles and labels
plt.title(f"Population Change in Taiwan (2010 - 2022)")
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

# 7. Annotate bars with population values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=10)

# Show the plot
plt.tight_layout()
plt.savefig("taiwan_population_change_bar_annotated.png")
plt.show()