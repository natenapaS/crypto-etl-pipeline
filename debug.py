# print("step 1")
# from etl.logger import get_logger
# print("step 2")
# import requests
# print("step 2.1")
# import urllib3
# print("step 2.2")
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# print("step 2.3")
# from etl.extract.coingecko import fetch_prices
# print("step 3")

print("step 1")
from etl.logger import get_logger
print("step 2")
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print("step 3")
from etl.extract.coingecko import fetch_prices
print("step 4")
from etl.transform.cleaner import clean_prices
print("step 5")
from etl.transform.validator import validate_prices
print("step 6")
from etl.load.database import init_db, save_prices
print("step 7 - all imports ok")