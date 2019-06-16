import pandas as pd 

#read the College csv into a pandas dataframe 
dt = pd.DataFrame.from_csv("/Users/dongheelee/Documents/data_mining_2019/College.csv")
print(dt)

print(dt.columns)

#integer-location based indexing
#gets the last column (Grad.Rate)
print(dt.iloc[:,-1])