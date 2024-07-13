import os
import sys
import datetime
from dotenv import load_dotenv
from ebaysdk.finding import Connection
from psycopg2 import connect

load_dotenv()
API_KEY = os.getenv('api_key')


class Ebay_24(object):
    def __init__(self, API_KEY,st):
        self.st = st
        self.api_key = API_KEY

    def fetch(self):
        try:
            api = Connection(appid=self.api_key, config_file=None,siteid="EBAY-US")
            response = api.execute('findItemsAdvanced', {'keywords': st})

            for item in response.reply.searchResult.item:
                print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")
                print(f"Country: {item.country}")
                print(f"URL: {item.viewItemURL}")
               # print(f"Condition: {item.condition.conditionDisplayName}")
                print(f"Buy it now available: {item.listingInfo.buyItNowAvailable}\n")
                try:
                    print(f"Watchers: {item.listingInfo.watchCount}\n")
                except AttributeError:
                    pass

        except ConnectionError as e:
            print(f"Connection Error: {e}")
            if hasattr(e, 'response') and hasattr(e.response, 'dict'):
                print(f"Response Dict: {e.response.dict()}")

    def parse(self):
        # Implement parsing logic if needed
        pass


if __name__ == '__main__':
    st = sys.argv[1]
    e = Ebay_24(API_KEY,st)
    e.fetch()
    e.parse()
    connect()


