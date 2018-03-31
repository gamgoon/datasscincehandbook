import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from iris import get_iris_df, df

colors = ['r', 'g', 'b']
markers = ['.', '*', '^']
fig, ax = plt.subplots(1,1)
for i, spec in enumerate(df['species'].unique()):
    ddf = df[df['species']==spec]
    ddf.plot(kind='scatter', x='sepal length (cm)', y='sepal width (cm)',
        alpha=0.5, s=10*(i+1), ax=ax, color=colors[i], marker=markers[i], label=spec)

plt.legend()
plt.show()