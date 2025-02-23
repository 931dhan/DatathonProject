import pandas as pd 
import numpy as np 

df = pd.read_csv("Parking_Violations_-_2023_-_Present(1).csv")

def numberOfParkingViolations(minLat, maxLat, minLong, maxLong): 
    filterd = df[(df['LAT'] >= minLat) & (df['LAT'] <= maxLat) 
                 & (df['LONG'] >= minLong) & (df['LONG'] <= maxLong)]
    print(filterd)

numberOfParkingViolations(df["LAT"].min(), df["LAT"].max(), df["LONG"].min(), df["LONG"].max())


def numberOfCityComps(minLat, maxLat, minLong, maxLong) -> int: 
    print("gel")

 