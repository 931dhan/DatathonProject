import pandas as pd 
import numpy as np 

df = pd.read_csv("Parking_Violations_-_2023_-_Present(1).csv")

def numberOfParkingViolations(minLat, maxLat, minLong, maxLong): 
    filterd = df[(df['LAT'] >= minLat) & (df['LAT'] <= maxLat) 
                 & (df['LONG'] >= minLong) & (df['LONG'] <= maxLong)]
    return len(filterd)

print(numberOfParkingViolations(df["LAT"].min(), df["LAT"].max(), df["LONG"].min(), df["LONG"].max()))
print(len(df))

df2 = pd.read_csv("SYRCityline_Requests_(2021-Present)(1).csv")

def numberOfCityComps(minLat, maxLat, minLong, maxLong) -> int: 
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)]   
    print(filterd)

numberOfCityComps(df2["Lat"].min(), df2["Lat"].max(), df2["Lng"].min(), df2["Lng"].max())


# Column 1, 2 should be long range, lat range from arrZones object respectively, 
def buildDataSet(arrZones):
