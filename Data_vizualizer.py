import time
import matplotlib.pyplot as plt
import pandas as pd

# Ask the user for the input dataset file
input_file = input('Input 1000 Sales Records.csv')

# Load the input dataset file using pandas
data = pd.read_csv(input_file)

# Create a line plot of the data
plt.plot(data['Unit Price'], data['Total Profit'], '.')

# Add a title and axis labels to the plot
plt.title('Data Visualization Example')
plt.xlabel('Unit Price')
plt.ylabel('Total Profit')

# Save the plot to a file
plt.savefig('output_plot.png')

print('Check your folder')
time.sleep(2)
input("Нажмите Enter для выхода")