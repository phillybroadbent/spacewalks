# Spacewalks 

[![DOI](https://sandbox.zenodo.org/badge/892714745.svg)](https://handle.stage.datacite.org/10.5072/zenodo.136991)

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of spacewalks:

- Generates a csv table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requistites

Spacewalks was developed using Python version 3.12

To install and run spacewalks you will need to have Python >= 3.12

You will also need the following libraries:

- [Numpy](https://www.numpy.org) >= 2.0.0 Spacewalk's test suite uses Numpy's statistical functions.
- [Matplotlib](https://matplotlib.org/stable/index.html) >= 3.0.0 Spacewalks uses Matplotlib to make plots.
- [pytest](https://docs.pytest.org/en/8.2.x/#) >= 8.2.0 Spacewalks uses pytest for its test suite
- [pandas](https://pandas.pydata.org) >= 2.2.0 Spacewalks uses pandas for data frames and data analysis

## Installation instructions

+ Clone the Spacewalks repository to your local machine using Git.
If you don't have Git installed, you can download it from the official Git website.

```
git clone https://github.com/your-repository-url/spacewalks.git
cd spacewalks
```

+ Install the necessary dependencies:
```
python3 -m pip install pandas==2.2.2 matplotlib==3.8.4 numpy==2.0.0 pytest==7.4.2
```

+ To ensure everything is working correctly, run the tests using pytest.

```
python3 -m pytest
```

## Usage Example

To run an analysis using the eva_data_analysis.py script from the command line terminal,
launch the script using Python as follows:

```
# Usage Examples
python3 eva_data_analysis.py data/eva-data.json results/eva-data.csv
```

The first argument is path to the JSON data file.
The second argument is the path the CSV output file.