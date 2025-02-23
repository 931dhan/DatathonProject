import pandas as pd 
import numpy as np


df = pd.read_csv("ourDatasetWithCategories.csv")


# Checking if dataset is valid
def checkDataset(): 
    print(df.head())
    print(df.tail())


def dfInfo(): 
    # Descriptive stats
    print(df.describe())
    # Column names, associated data types
    print(df.info())
    # Check for any null values     
    print(df.isnull().sum())


print(df.at[3, 'categories'])
