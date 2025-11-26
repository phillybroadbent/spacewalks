import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe. 
    Clean the data by removing any rows where the duration or date value is missing.
    
    Args:
        input_file(file or str): The file object or path to the JSON file
        
    Returns:
        eva_df(pd.Dataframe): The cleaned and sorted data as a dataframe structure.
    """
    print(f"Reading JSON File {input_file}")
    # Read the data from JSON into a pandas dataframe
    eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float)

    # Clean the data by removing any rows where duration or date are missing
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return eva_df

def write_dataframe_to_csv(df, output_file):
    """
    Write the dataframe to a CSV file.

    Args:
        df (pd.Dataframe): The input dataframe
        output_file (file or str): The file object or path to the output CSV file.
        
    Returns:
        None
    """

    print(f"Saving to CSV file {output_file}")
    # Save dataframe to csv for later analysis
    df.to_csv(output_file, index=False, encoding='utf-8')
    
def plot_cumulative_time_in_space(df, graph_file):
    """
    Plot the cumulative time spent in space over the years.
    Convert the duration column from strings to number of hours
    Calculate the cumulative sum of durations
    Generate a plot of cumulative time spent in space over the years and save it to the specified location.

    Args:
        df (pd.DataFrame): The input dataframe
        graph_file (file or str): The file object or path to the output graph file.
        
    Returns:
        None
    """
    print(f"Plotting cumulative spacewalk duration and saving to {graph_file}")
    # Create data necessary for plotting cumulative time in space over the years
    df['duration_hours'] = df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    df['cumulative_time'] = df['duration_hours'].cumsum()

    # create a plot of year vs total time in space
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show() 


# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png' # assign file to output graph into

print("--START--")

# Read the data from JSON file
eva_data = read_json_to_dataframe(input_file)

# Convert and export the data to csv file
write_dataframe_to_csv(eva_data, output_file)

# Sort dataframe by date so that it's ready to be plotted with date on the x axis
eva_data.sort_values('date', inplace=True)

plot_cumulative_time_in_space(eva_data, graph_file)


print("--END--")
