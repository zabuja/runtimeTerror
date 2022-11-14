import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from array import array

# Reading the data 
df = pd.read_csv('transactions.csv', index_col=0)
# pandas count distinct values in column 
# creating the dataset
data = df['Requested Amount'].value_counts().to_dict()

answer = df['Requested Amount'].sum()
print(answer)

count = data = df['Requested Amount'].value_counts().sum()
print(count)


print(answer/count)