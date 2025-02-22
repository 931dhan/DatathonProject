import pandas as pd
import numpy as np

# Determine the overlap in the range of Longitude values between the Cityline dataset
def detLongBounds() -> list:
    print("")

# Determine the overlap in the range of Latitude values between the Cityline dataset
def detLatBounds() -> list:
    print("")


# x axis is the number of cityline complaints, y axis is the number of parking violations 
# Given a num of horizontal and vertical divisions, determine the cubic meters of each area by performing conversioin of lat and long to meters. 
# Returns list of objects, each object includes lat, long ranges.
def zones(minLong, maxLong, minLad, maxLad,numOfHorizontalDivs: int, numOfVerticalDivs: int) -> (int):
    y_distance = maxLad - minLad
    x_distance = maxLong - minLong
    
    zoneWidth = (x_distance / numOfVerticalDivs)
    zoneHeight = (y_distance / numOfHorizontalDivs)
    
    arrayOfLongs = np.arange(minLong, maxLong, zoneWidth)
    arrayOfLats = np.arange(minLong, maxLong, zoneHeight)

    arrZones = []

    for longi in arrayOfLongs: 
        
        for lati in arrayOfLats: 
            zoneDimensions = {
                "longRange" : [longi, longi + zoneWidth],
                "latRange" : [lati, lati + zoneHeight]
            }
            arrZones += zoneDimensions
            
            print(zoneDimensions)




zones(10, 100, 10, 100, 7, 7)
