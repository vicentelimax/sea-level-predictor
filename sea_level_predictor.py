import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    
    # Create first line of best fit
    result_predict_80_13 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values_ln1 = np.arange(1880, 2051)
    y_values_ln2 = result_predict_80_13.slope * x_values_ln1 + result_predict_80_13.intercept

    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', marker='o', color='royalblue')

    plt.plot(x_values_ln1, y_values_ln2, color='red', label= 'Fitted line')

    # Create second line of best fit
    result_predic_00_13 = linregress(df.query('Year >= 2000')['Year'],
                                 df.query('Year >= 2000')['CSIRO Adjusted Sea Level'])

    x_value_ln2 = np.arange(2000, 2051)
    y_values_ln2 = result_predic_00_13.slope * x_value_ln2 + result_predic_00_13.intercept

    plt.plot(x_value_ln2, y_values_ln2, color='gold', label= 'Fitted line')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()