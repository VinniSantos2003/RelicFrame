import requests
import json

class apiClient:
    def __init__(self):
        pass
    
    def requestOrder(url: str) -> json:
        #Receives a url as a parameter an then get something from the API
        warframeMarketApi = requests.get(url)
        OrderData = json.load(warframeMarketApi.text)
        return OrderData
    
    def getCheapestOrder(data : json):
        print(data["data"][len(data["data"]-1)])

    def getDucatValue(data : json):
        pass
    