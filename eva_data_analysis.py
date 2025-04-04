import json
import csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re

def main(input_file, output_file, graph_file):
    print("--START--")
    print(f'Reading JSON file {input_file}')

    eva_data = read_json_to_dataframe(input_file)
    
    eva_data = add_crew_size_column(eva_data)

    write_dataframe_to_csv(eva_data, output_file)

    plot_cumulative_time_in_space(eva_data, graph_file)

    print("--END--")
    
    
def calculate_crew_size(crew):
    """
    Calculate the size of the crew for a single crew entry

    Args:
        crew (str): The text entry in the crew column containing a list of crew member names

    Returns:
        (int): The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1

def add_crew_size_column(df):
    """
    Add crew_size column to the dataset containing the value of the crew size

    Args:
        df (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of df with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy

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
    
def text_to_duration(duration):
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60
    return duration_hours

def add_duration_hours_variable(df):
    df_copy = df.copy()
    df_copy['duration_hours'] = df_copy['duration'].apply(
        text_to_duration
    )
    return df_copy
    
def plot_cumulative_time_in_space(df, graph_file):
    df = add_duration_hours_variable(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()

    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    # Plot cumulative time spent in space over years
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()

# Main code

if __name__ == "__main__":
    if len(sys.argv) < 3:
        input_file = 'data/eva-data.json'
        output_file = 'results/eva-data.csv'
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

    graph_file = 'results/cumulative_eva_graph.png'
    main(input_file, output_file, graph_file)  
