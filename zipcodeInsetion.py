import pandas as pd
import requests

station = pd.read_csv("station.csv")


def getZipCode(lat, long):
    response = requests.get(
        f'https://maps.googleapis.com/maps/api/geocode/json?latlng={str(lat)},{str(long)}&key=AIzaSyBMmksnGsbnDR4g93iglqrq7qBZCdenv88')

    resp_payload = response.json()
    zip = resp_payload["results"][0]["address_components"][-1]["long_name"]


def getZipCode2(row):
    lat = row["lat"]
    long = row["long"]
    response = requests.get(
        f'https://maps.googleapis.com/maps/api/geocode/json?latlng={str(lat)},{str(long)}&key=AIzaSyBMmksnGsbnDR4g93iglqrq7qBZCdenv88')
    resp_payload = response.json()
    zip = resp_payload["results"][0]["address_components"][-1]["long_name"]
    return zip


def computeZips():
    station["zip_code"] = station.apply(getZipCode2, axis=1)
    '''for index, row in station.iterrows():
        station.iloc[index]['zip_code'] = getZipCode(
            row["lat"], row["long"])'''
    print(station)


computeZips()
station.to_csv(r'./station_with_zip.csv')
