import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/polls/pres_primary_avgs_1980-2016.csv')

# Group the data by year and party and calculate the mean and standard deviation of the vote percentages
grouped = df.groupby(["year", "party"])["pct"].agg(["mean", "std"]).reset_index()

# Pivot the data to make it easier to plot
pivoted = grouped.pivot(index="year", columns="party")

# Plot the mean vote percentages over time
fig, ax = plt.subplots()
pivoted["mean"].plot(ax=ax)
ax.set_ylabel("Mean Vote Percentage")
ax.set_title("Primary Vote Percentages by Party and Year")
plt.show()

