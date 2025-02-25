import pandas as pd 
import numpy as np 
import zoning
import os


df = pd.read_csv("Parking_Violations_-_2023_-_Present(1).csv")
df2 = pd.read_csv("SYRCityline_Requests_(2021-Present)(1).csv")

def numberOfParkingViolations(minLat, maxLat, minLong, maxLong): 
    filterd = df[(df['LAT'] >= minLat) & (df['LAT'] <= maxLat) 
                 & (df['LONG'] >= minLong) & (df['LONG'] <= maxLong)]
    return len(filterd)

def numberOfCityComps(minLat, maxLat, minLong, maxLong) -> int: 
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)]   
    return len(filterd)


def StreetsSidewalksRequests(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)
                & (df2['Agency_Name'] == "Streets, Sidewalks & Transportation")]   
    return len(filterd)

def GarbRecyGraffRequests(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)
                & (df2['Agency_Name'] == "Garbage, Recycling & Graffiti")]   
    return len(filterd)

def HousingPropertyRequests(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)
                & (df2['Agency_Name'] == "Housing & Property Maintenance")]   
    return len(filterd)

def FeedbackToCityRequests(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)
                & (df2['Agency_Name'] == "Feedback to the City")]   
    return len(filterd)

def ParkingVehiclesRequests(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)
                & (df2['Agency_Name'] == "Parking & Vehicles")]   
    return len(filterd)

def GreenSpacesRequests(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)
                & (df2['Agency_Name'] == "Green Spaces, Trees & Public Utilities")]   
    return len(filterd)

def WaterSewageRequests(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)
                & (df2['Agency_Name'] == "Water & Sewage")]   
    return len(filterd)

def AnimalsRequests(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)
                & (df2['Agency_Name'] == "Animals")]   
    return len(filterd)


def aggregateCategories(minLat, maxLat, minLong, maxLong):
    filterd = df2[(df2['Lat'] >= minLat) & (df2['Lat'] <= maxLat)
                & (df2['Lng'] >= minLong) & (df2['Lng'] <= maxLong)]   
    return np.array(filterd["Category"])

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
        minLat = zone["latRange"][0]
        maxLat = zone["latRange"][1]
        minLong = zone["longRange"][0]
        maxLong = zone["longRange"][1]
        row = {
            "latRange" : zone["latRange"], 
            "longRange" : zone["longRange"], 
            "numOfCityComp" : numberOfCityComps(minLat, maxLat, minLong, maxLong), 
            "numOfParkingViol" : numberOfParkingViolations(minLat, maxLat, minLong, maxLong),
            "numOfTransportReq" : StreetsSidewalksRequests(minLat, maxLat, minLong, maxLong),
            "numOfGarbageRecycleGraffitiReq" : GarbRecyGraffRequests(minLat, maxLat, minLong, maxLong),
            "numOfHousingPropertyReq" : HousingPropertyRequests(minLat, maxLat, minLong, maxLong),
            "numOfCityFeedbackReq" : FeedbackToCityRequests(minLat, maxLat, minLong, maxLong),
            "numOfParkingVehiclesReq" : ParkingVehiclesRequests(minLat, maxLat, minLong, maxLong),
            "numOfGreenSpaces" : GreenSpacesRequests(minLat, maxLat, minLong, maxLong),
            "numOfWaterSewageReq" : WaterSewageRequests(minLat, maxLat, minLong, maxLong),
            "numOfAnimalsReq" : AnimalsRequests(minLat, maxLat, minLong, maxLong),
            "categories" : aggregateCategories(minLat,maxLat, minLong, maxLong)
            
        }
        arrOfRows.append(row)

    
    return pd.DataFrame(arrOfRows)



ourDf = buildDataSet(createArrZones(50, 50))
ourDf2 = ourDf[ourDf["numOfParkingViol"] > 1000]
print(ourDf2)


cwd = os.getcwd()
print(cwd)
path = cwd + "/ourDatasetWithCategories.csv"
ourDf2.to_csv(path)

