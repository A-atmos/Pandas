import numpy as np
import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df.head(5))

df['Total'] = df['HP']+df['Attack'] + df['Sp. Atk']+ df['Sp. Def'] + df['Speed']
print(df.head(5))
# print(df['Total'])