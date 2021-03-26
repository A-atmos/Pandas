import numpy as np
import pandas as pd
import re #regular expressions for filtering data based on string pattern
df = pd.read_csv('pokemon_data.csv')
# print(df.head(5))

df['Total'] = df['HP']+df['Attack'] + df['Sp. Atk']+ df['Sp. Def'] + df['Speed']
# print(df.head(5))

'''# another method
df['Total'] = df.iloc[:,4:10].sum(axis=1)'''

# df = df.drop(columns = ['Total']) -- drop to clear/delete the column
# print(df.head(5))

cols = list(df.columns.values)
# print(cols)
df = df[cols[0:4]+[cols[-1]]+cols[4:len(cols)-1]] #since cols[-1] will be a string, [cols[-1]] is as list
# print(df.head(3))

# print(df['Total'])

'''save'''
df.to_csv('modified_pokemon_data.csv', index = False) #index for the first column

'''also df.to_excel('excel.xlsx', index = False) & df.to_csv('modified.txt', index= False, sep = '\t')'''
"""df.to_csv('modified.txt', index= False, sep = '\t') #sep -- separator"""

# #Filtering data
# print(df.loc[df['Legendary']==True])
"""new = df.loc[df['Type 1']=='Ice']
print(new.loc[new['Legendary']==True])"""
#OR
'''print(df.loc[(df['Type 1']=='Ice') & (df['Legendary']== True)])''' #& for and, | for or

# print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags = re.I, regex = True)].reset_index())
# df.reset_index() function for reseting index
# df.loc[~df['Name'].str.contains('pi[a-z]*'), flags=re.I, regex = True] #Here ~ acts as not(!)


#conditional changes

# df.loc[df['Total']>500,['Legendary']]= True '''multiple changes can also be made'''

# df = pd.read_csv('pokemon_data.csv')
print(df)