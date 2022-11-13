import pandas as pd

# Reading the data 
df = pd.read_csv('transactions.csv', index_col=0)
# pandas count distinct values in column 
print(df['Requested Amount'].value_counts())