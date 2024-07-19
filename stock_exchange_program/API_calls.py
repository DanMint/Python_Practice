import requests

class APICrypto:
    def __init__(self) -> None:
        pass

    @property
    def getTop100(self):
        url = "https://api.coinlore.net/api/tickers/"
        data = self.process_requests(url)
        return [(i["name"], i["id"],i["price_usd"], i["percent_change_1h"], i["percent_change_24h"], i["percent_change_7d"]) for i in data["data"]]

    @property
    def getInfo(self):
        url = "https://api.coinlore.net/api/global/"
        data = self.process_requests(url)
        return [(i["coins_count"], i["active_markets"], i["total_mcap"], i["total_volume"]) for i in data]
    
    def process_requests(self, request):
        try:
            response = requests.get(request)
            response.raise_for_status()
    
            data = response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")  
        except Exception as err:
            print(f"An unexpected error occurred: {err}") 


        return data


class APIStock:
    def __init__(self) -> None:
        self.api_key = "?apikey=YJXO5uQuHs35NpBqPHqTPTzQav9ntoxZ"

    @property
    def stockList(self):
        url = "https://financialmodelingprep.com/api/v3/available-traded/list" + self.api_key
        data = self.process_requests(url)
        return [(i["name"], i["price"], i["exchangeShortName"]) for i in data]
    
    def get_info_on_exchange(self, market):
        url = "https://financialmodelingprep.com/api/v3/symbol/" + market + self.api_key
        data = self.process_requests(url)
        return data
    
    def process_requests(self, request):
        try:
            response = requests.get(request)
            response.raise_for_status()
            data = response.json()
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")  
        except Exception as err:
            print(f"An unexpected error occurred: {err}") 

        return data

