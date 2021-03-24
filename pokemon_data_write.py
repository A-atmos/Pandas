import numpy as np
import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df.head(5))

df['Total'] = df['HP']+df['Attack'] + df['Sp. Atk']+ df['Sp. Def'] + df['Speed']
# print(df.head(5))

'''# another method
df['Total'] = df.iloc[:,4:10].sum(axis=1)'''

# df = df.drop(columns = ['Total']) -- drop to clear/delete the column
# print(df.head(5))

cols = list(df.columns.values)
print(cols)
df = df[cols[0:4]+[cols[-1]]+cols[4:len(cols)-1]] #since cols[-1] will be a string, [cols[-1]] is as list
print(df.head(3))

# print(df['Total'])

'''save'''
df.to_csv('modified_pokemon_data.csv', index = False) #index for the first column

