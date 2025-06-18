import requests
import pandas as pd
url= 'https://api.spacexdata.com/v4/launches'
response = requests.get(url)
data= response.json()
df=pd.json_normalize(data)
df.to_csv("space_x.csv",index=False)