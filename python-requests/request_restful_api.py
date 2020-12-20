import requests

url = "http://api.open-notify.org/astros.json"

def getDataFromAPI(url, query=""):
    response = requests.get(url)
    data_json = response.json() # This method is convenient when the API returns JSON
    return data_json


if __name__ == "__main__":
    data = getDataFromAPI(url)
    print(data)