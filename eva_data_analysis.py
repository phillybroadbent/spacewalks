import json
import csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding="utf-8")
output_file = open('./eva-data.csv','w', encoding="utf-8")
graph_file = './cumulative_eva_graph.png'  


print("--START--")
print(f'Reading JSON file {input_file}')

# read in json file
eva_df = pd.read_json(input_file, convert_dates=['date'])
# convert eva column to float
eva_df['eva'] = eva_df['eva'].astype(float)
# removing missing values
eva_df.dropna(axis=0, inplace=True)
# sort values by date
eva_df.sort_values('date', inplace=True)

# write out data to csv
eva_df.to_csv(output_file, index=False)

# create new column duration hours
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0])+ int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
# Plot cumulative time spent in space over years
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
print("--END--")