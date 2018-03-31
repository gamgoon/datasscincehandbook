import urllib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

URL = ("http://ichart.finance.yahoo.com/" + "table.csv?s=GOOG&c=2000") # 현재 서비스 되지 않음! ㅡ.ㅡ;
dat = urllib.request.urlopen(URL).read()
open('foo.csv', 'w').write(dat)

df = pd.read_csv('foo.csv')
df.index = df['Date'].astype('datetime64')
df['LogClose'] = np.log(df['Close'])
df['Close'].plot()
plt.title("일반 축")
plt.show()
df['Close'].plot(logy=True)
plt.title("로그 축")
plt.show()