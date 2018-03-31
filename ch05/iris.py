import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import sklearn.datasets

def get_iris_df():
    ds = sklearn.datasets.load_iris()
    # print(ds)
    df = pd.DataFrame(ds['data'], columns=ds['feature_names'])
    # print(df)
    code_species_map = dict(zip(range(3), ds['target_names']))
    # print(code_species_map)
    df['species'] = [code_species_map[c] for c in ds['target']]
    # print(df['species'])
    return df

df = get_iris_df()
# print(df)