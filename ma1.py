import pandas as pd
data = pd.read_csv('data.csv',sep=';',engine='python',encoding='UTF8')
print(data)