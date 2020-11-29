# Dataframes-CSV.py
import pandas as pd

# import the cars.csv file
cars = pd.read_csv('cars.csv')
# print out cars
print(cars)
print()

# indexing dataframes
cars2 = pd.read_csv('cars.csv', index_col = 0)
# print out the country colum as a pandas series
print(cars2['cars_per_cap'])
print()
# print out the country column as a pandas dataframe
print(cars2[['cars_per_cap']])
print()
# print out a dataframe with country and drives_right columns
print(cars2[['cars_per_cap', 'country']])
print()

# print out the first 4 observations (rows)
print(cars2[0:4])
print()
# print the 5th and 6th rows
print(cars2[4:6])
print()

# print out Japan by index
print(cars2.iloc[2])
print()
# print out Australia and Egypt by label
print(cars2.loc[['AUS', 'EG']])