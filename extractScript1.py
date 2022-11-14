import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from array import array

# Reading the data 
df = pd.read_csv('transactions.csv', index_col=0)
# pandas count distinct values in column 
# creating the dataset
data = df['Requested Amount'].value_counts().to_dict()
print(data)

packages = list(data.keys())
val = list(data.values())
# print(val) 
# fig = plt.figure(figsize = (10, 5))
 
# # creating the bar plot
# plt.scatter(array("f", packages), array("i", val))
 
# plt.xlabel("Packages offered")
# plt.ylabel("No. of customers enrolled")
# plt.title("customer-package distribution")
# plt.show()

plt.pie(val, labels = packages)
plt.show() 