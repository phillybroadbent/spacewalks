import json
import csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into pandas dataframe
    Clean the data by removing incomplete rows and sort by date
    
    Args:
        input_file(str): The path to the JSON file
        
    Returns:
        eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe structure
    """
    # read in json file
    eva_data = pd.read_json(input_file, convert_dates=['date'])
    # convert eva column to float
    eva_data['eva'] = eva_data['eva'].astype(float)
    # removing missing values
    eva_data.dropna(axis=0, inplace=True)
    # sort values by date
    eva_data.sort_values('date', inplace=True)
    return eva_data

def write_dataframe_to_csv(df, output_file):
    """
    Write the dataframe to csv file

    Args:
        df (pd.DataFrame): The input dataframe
        output_file (str): The path to the output CSV file
    """
    # write out data to csv
    df.to_csv(output_file, index=False)


# Main code

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding="utf-8")
output_file = open('./eva-data.csv','w', encoding="utf-8")
graph_file = './cumulative_eva_graph.png'  


print("--START--")
print(f'Reading JSON file {input_file}')

eva_data = read_json_to_dataframe(input_file)

write_dataframe_to_csv(eva_data, output_file)

# create new column duration hours
eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0])+ int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()

print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
# Plot cumulative time spent in space over years
plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
print("--END--")