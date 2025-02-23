import pandas as pd 
import numpy as np 

df = pd.read_csv("Parking_Violations_-_2023_-_Present(1).csv")

def numberOfParkingViolations(minLat, maxLat, minLong, maxLong): 
    filterd = df[(df['LAT'] >= minLat) & (df['LAT'] <= maxLat) 
                 & (df['LONG'] >= minLong) & (df['LONG'] <= maxLong)]
    print(filterd)

numberOfParkingViolations(df["LAT"].min(), df["LAT"].max(), df["LONG"].min(), df["LONG"].max())


df2 = pd.read_csv("SYRCityline_Requests_(2021-Present)(1).csv")

def numberOfCityComps(minLat, maxLat, minLong, maxLong) -> int: 
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)]   
    print(filterd)

numberOfCityComps(df2["Lat"].min(), df2["Lat"].max(), df2["Lng"].min(), df2["Lng"].max())

 