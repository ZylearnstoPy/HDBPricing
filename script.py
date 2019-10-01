import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso, Ridge, LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score

#Step 1: Reading the .csv file with Pandas
raw_data = pd.read_csv('resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv')

#Step 2: We inspect the data and apply relevant processing techniques (removing null values, etc) 
print(raw_data.head())
print(raw_data.info())
print(raw_data.describe())

#Step 3: For simplicity's sake, I've selected only a few columns from the raw data as variables to predict the resale price. `
df = raw_data[['town', 'flat_type','storey_range', 'floor_area_sqm', 'flat_model', 'remaining_lease', 'resale_price']]

