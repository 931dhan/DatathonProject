import pandas as pd 
import numpy as np


df = pd.read_csv("SYRCityline_Requests_(2021-Present)(1).csv")


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

print(df[df["Minutes_to_Acknowledge"] >= 10])

