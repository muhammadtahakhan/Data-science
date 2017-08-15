import pandas as pd


ufo = pd.read_table('./ufo.csv', sep=',')
print(type(ufo))
print(type(ufo['City']))
print(ufo.head())


ufo['Location'] = ufo.City+', '+ufo.State
print()
print(ufo.head())