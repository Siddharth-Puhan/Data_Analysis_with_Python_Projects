import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', alpha=0.8, data=df)
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Year Vs. CSIRO Adjusted Sea Level')
    plt.show()


    # Create first line of best fit
    year = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']

    slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)

    # Creating a linear regression line function
    def linear_regression_line(x):
        return slope * x + intercept

    # Plotting the scatter plot
    plt.scatter(year, sea_level, label='Sea Levels')

    # Creating a range of years from 1880 to 2050
    year_range = np.arange(1880, 2051)

    # Calculate sea-level predictions for the specified range
    sea_level_predictions = linear_regression_line(year_range)

    # Plot the line of best fit
    plt.plot(year_range, sea_level_predictions, color='red', label='Line of Best Fit')

    # Extrapolate to the year 2050
    sea_level_2050 = linear_regression_line(2050)
    plt.scatter(2050, sea_level_2050, color='green', marker='x', s=100, label='2050 Prediction')


    # Create second line of best fit
    recent_years = year[year >= 2000]
    recent_sea_levels = sea_level[year >= 2000]

    # Calculate the linear regression for the recent data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_years, recent_sea_levels)

    # Create a range of years from 2000 to 2050
    years_2000_to_2050 = np.arange(2000, 2051)

    # Calculate the sea level predictions for the range of years
    sea_level_predictions_recent = linear_regression_line(years_2000_to_2050)

    # Plot the new line of best fit
    plt.plot(years_2000_to_2050, sea_level_predictions_recent, color='blue', label='2000-2050 Prediction')

    # Set plot labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Year vs. CSIRO Adjusted Sea Level')

    # Add a legend
    plt.legend()

    # Show the plot (put at the end of the plot)
    plt.grid(True)
    plt.show()

    # Print the slope and y-intercept
    print(f"Slope: {slope}")
    print(f"Y-Intercept: {intercept}")

    # Predict the sea level in 2050
    print(f"Predicted Sea Level in 2050 for first best line: {sea_level_2050} inches")

    # Predict the sea level in 2050 based on the extrapolated line
    sea_level_2050_prediction = sea_level_predictions_recent[-1]
    print(f"Predicted Sea Level in 2050 for second best line: {sea_level_2050_prediction} inches")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()