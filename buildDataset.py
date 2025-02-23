import pandas as pd 
import numpy as np 

df = pd.read_csv("Parking_Violations_-_2023_-_Present(1).csv")

def numberOfParkingViolations(minLat, maxLat, minLong, maxLong): 
    filterd = df[(df['LAT'] >= minLat) & (df['LAT'] <= maxLat) 
                 & (df['LONG'] >= minLong) & (df['LONG'] <= maxLong)]
    return len(filterd)

print(numberOfParkingViolations(df["LAT"].min(), df["LAT"].max(), df["LONG"].min(), df["LONG"].max()))
print(len(df))

def numberOfCityComps(minLat, maxLat, minLong, maxLong) -> int: 
    print("gel")


# Column 1, 2 should be long range, lat range from arrZones object respectively, 
def buildDataSet(arrZones):
