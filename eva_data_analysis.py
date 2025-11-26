import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png' # assign file to output graph into

print("--START--")
print(f"Reading JSON File {input_file}")
# Read the data from JSON into a pandas dataframe
eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
eva_df['eva'] = eva_df['eva'].astype(float)

# Clean the data by removing any rows where duration or date are missing
eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)

print(f"Saving to CSV file {output_file}")
# Save dataframe to csv for later analysis
eva_df.to_csv(output_file, index=False, encoding='utf-8')

# Sort dataframe by date so that it's ready to be plotted with date on the x axis
eva_df.sort_values('date', inplace=True)

print(f"Plotting cumulative spacewalk duration and saving to {graph_file}")
# Create data necessary for plotting cumulative time in space over the years
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# create a plot of year vs total time in space
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
print("--END--")
