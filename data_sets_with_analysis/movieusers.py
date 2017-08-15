import pandas as pd
import numpy as np


colums = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
orders =  pd.read_table('./movieusers.tsv', sep='|', header=None, names=colums)

print(orders.head())
