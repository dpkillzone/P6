import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Load dataset
data = pd.read_csv('diamonds.csv')


# Summary statistics
maks = np.max(data['carat'])
mini = np.min(data['carat'])
mean = np.mean(data['carat'])
median = np.median(data['carat'])
std = np.std(data['carat'])
var = np.var(data['carat'])
rang = np.max(data['carat']) - np.min(data['carat'])

# Create a list of values for boxplot
datalist = data['carat'].values.tolist()

qunatile = np.quantile(data['carat'],[0.25,0.75])


# Create a boxplot
stats = {}
stats['A'] = mpl.cbook.boxplot_stats(data['carat'], labels='A')[0]
stats['A']['q1'], stats['A']['q3'], stats['A']['whishi'], stats['A']['whislo'] = [
    float(qunatile[0]), float(qunatile[1]), float(maks), float(mini)]
plt.boxplot(datalist,vert=False,showfliers=False)

fig, ax = plt.subplots()
ax.bxp([stats['A']], positions=range(1), showfliers=False, vert=False)
xTicksSpacing = 1

ax.set_xticks(range(int(mini),int(maks)+xTicksSpacing, xTicksSpacing))

# Add title and labels
plt.title('Carat Distribution')
plt.xlabel('Carat')
plt.ylabel('Frequency')

# Display the boxplot
plt.show()