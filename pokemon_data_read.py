import pandas as pd
import numpy as np
df = pd.read_csv('pokemon_data.csv') 
# df = pd.read_csv('pokemon_data.csv', delimiter="\t") -- for tab seperated csv file
# print(df)



# print(df['Name'])
# print(df[['Name','Type 1', 'HP', 'Generation']])



# count = int()
# for index, row in df.iterrows():
#     if row['Legendary'] or row['HP']>=100 :
#         print(index, row['Name'])
#         count +=1
# print(count)



print(df.loc[df['Legendary']==True])
# ''' df.iloc[1:4] -- gives all the data of row 1 to 4'''



# for name in df['Name']:
#     print(name)


# '''k= int()
# for legen in df['Legendary']:
#     if legen:
#         k=k+1
#     else: None

# print(f"No of legendary is", k)'''



'''# dates = pd.date_range("20130101", periods=6)
# print(dates)
# df.describe()
# df.sort_values('Name', ascending= False)
# '''
