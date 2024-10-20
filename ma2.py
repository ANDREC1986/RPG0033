import pandas as pd
data = pd.read_csv('data.csv',sep=';',engine='python',encoding='UTF8')
data2 = data.filter(['Duration','Date', 'Pulse'], axis=1)
print(data2)