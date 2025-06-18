import pandas as pd
df=pd.read_csv(r"C:\Users\imean\OneDrive\Desktop\projecttss\Space Launch Tracker\Data\Global_Space_Exploration_Dataset.csv")
isro_data = df[df['Country'].str.contains('India',na = True)]
isro_data.to_csv("isro_data.csv",index= False)