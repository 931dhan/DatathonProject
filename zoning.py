import pandas as pd
import numpy as np

df = pd.read_csv("SYRCityline_Requests_(2021-Present)(1).csv")
df2 = pd.read_csv("Parking_Violations_-_2023_-_Present(1).csv")

# Determine the overlap in the range of Longitude values between the Cityline dataset
def detLongBounds() -> list:
    minLongCity = df['Lng'].min()
    minLongPV = df2['LONG'].min()
    maxLongCity = df['Lng'].max()
    maxLongPV = df2['LONG'].max()
    
    long_list = [max(minLongCity, minLongPV), min(maxLongCity, maxLongPV)]

    return long_list

# Determine the overlap in the range of Latitude values between the Cityline dataset
def detLatBounds() -> list:
    minLatCity = df['Lat'].min()
    minLatPV = df2['LAT'].min()
    maxLatCity = df['Lat'].max()
    maxLatPV = df2['LAT'].max()

    lat_list = [max(minLatCity, minLatPV), min(maxLatCity, maxLatPV)]

    return lat_list



# x axis is the number of cityline complaints, y axis is the number of parking violations 
# Given a num of horizontal and vertical divisions, determine the cubic meters of each area by performing conversioin of lat and long to meters. 
# Returns list of objects, each object includes lat, long ranges.
def zones(minLong, maxLong, minLad, maxLad,numOfHorizontalDivs: int, numOfVerticalDivs: int) -> (list[object]):
    y_distance = maxLad - minLad
    x_distance = maxLong - minLong
    
    zoneWidth = (x_distance / numOfVerticalDivs)
    zoneHeight = (y_distance / numOfHorizontalDivs) 
    
    print(zoneWidth)
    print(zoneHeight)
    
    arrayOfLongs = np.arange(minLong, maxLong, zoneWidth)
    arrayOfLats = np.arange(minLad, maxLad, zoneHeight)

    arrZones = []

    for longi in arrayOfLongs: 
        
        for lati in arrayOfLats: 
            zoneDimensions = {
                "longRange" : [longi, longi + zoneWidth],
                "latRange" : [lati, lati + zoneHeight]
            }
            arrZones.append(zoneDimensions)
            

    return arrZones
    
