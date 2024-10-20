import pandas as pd
pd.set_option('display.max_rows',9999)
data = pd.read_csv('data.csv',sep=';',engine='python',encoding='UTF8')
data2 = data.filter(['Duration','Date', 'Pulse'])
print(data.shape)
print(data.isnull().sum().sum())
print(data.dtypes)
print(data.info())