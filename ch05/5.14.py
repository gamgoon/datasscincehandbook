import matplotlib.pyplot as plt
import statsmodels.api as sm

dta = sm.datasets.co2.load_pandas().data
dta.plot()
plt.title("co2")
plt.ylabel("PPM")
plt.show()