import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from iris import get_iris_df, df

col = df['petal length (cm)']
print(col)
average = col.mean() # 평균
print(average)
std = col.std()    # 표준편차?
print(std)
median = col.quantile(0.5)  # 중간값
print(median)
percentile25 = col.quantile(0.25) # 25% 백분위수
print(percentile25)
percentile75 = col.quantile(0.75) # 75% 백분위수
print(percentile75)
