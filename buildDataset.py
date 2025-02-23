import pandas as pd 
import numpy as np 
import zoning


df = pd.read_csv("Parking_Violations_-_2023_-_Present(1).csv")
df2 = pd.read_csv("SYRCityline_Requests_(2021-Present)(1).csv")

def numberOfParkingViolations(minLat, maxLat, minLong, maxLong): 
    filterd = df[(df['LAT'] >= minLat) & (df['LAT'] <= maxLat) 
                 & (df['LONG'] >= minLong) & (df['LONG'] <= maxLong)]
    return len(filterd)

print(numberOfParkingViolations(df["LAT"].min(), df["LAT"].max(), df["LONG"].min(), df["LONG"].max()))
print(len(df))


def numberOfCityComps(minLat, maxLat, minLong, maxLong) -> int: 
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)]   
    return len(filterd)

print(numberOfCityComps(df2["Lat"].min(), df2["Lat"].max(), df2["Lng"].min(), df2["Lng"].max()))
print(len(df2))


# Column 1, 2 should be long range, lat range from arrZones object respectively
# Column 3, 4 will be the number of city complaints and the number of parking violations 

def createArrZones(numOfHorizontalDivs: int, numOfVerticalDivs: int): 
    minLad = zoning.detLatBounds()[0]
    maxLad = zoning.detLatBounds()[1]
    minLong = zoning.detLongBounds()[0]
    maxLong = zoning.detLongBounds()[1]
    return zoning.zones(minLong, maxLong, minLad, maxLad, numOfHorizontalDivs, numOfVerticalDivs)

def buildDataSet(arrZones):
    arrOfRows = []
    for zone in arrZones: 
        row = {
            "latRange" : zone["latRange"], 
            "longRange" : zone["longRange"], 
            "numOfCityComp" : numberOfCityComps(zone["latRange"][0], zone["latRange"][1], zone["longRange"][0], zone["longRange"][1]), 
            "numOfParkingViol" : numberOfParkingViolations(zone["latRange"][0], zone["latRange"][1], zone["longRange"][0], zone["longRange"][1])
        }
        arrOfRows.append(row)

    
    return pd.DataFrame(arrOfRows)


print(buildDataSet(createArrZones(6, 6)))