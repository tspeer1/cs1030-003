import pandas as pd
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/polls/pres_primary_avgs_1980-2016.csv')

# Filter the DataFrame to only include rows where the nominee won the general election
nominees = df[df["nominee"] == True]

# Calculate the difference between the final primary polling average and the actual general election vote share
nominees["polling_error"] = nominees["final_estimate"] - nominees["share"]

# Calculate the mean and standard deviation of the polling errors
mean_error = np.mean(nominees["polling_error"])
std_error = np.std(nominees["polling_error"])

print("Mean polling error:", mean_error)
print("Standard deviation of polling errors:", std_error)
