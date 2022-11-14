# The logic can be check that if phone number email id is not present for any subscription that may be fraud

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from array import array

# Reading the data 
df = pd.read_csv('transactions.csv', index_col=0)
# pandas count distinct values in column 
# creating the dataset
df["Phone"].isnull().sum()

print((df["Name"].values == '').sum())

