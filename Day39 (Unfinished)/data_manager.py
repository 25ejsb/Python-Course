import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.API_ENDPOINT = "https://api.sheety.co/3b701a28dd0c113a99632a3f2190f381/flightDeals/prices"
    
    def getSheetData(self):
        return requests.get(self.API_ENDPOINT).json()