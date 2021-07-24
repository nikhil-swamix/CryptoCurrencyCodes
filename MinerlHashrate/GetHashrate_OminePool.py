from bs4 import BeautifulSoup as soup
import requests
import html5lib
import re ,json
# import HITBTC
URL = "https://www.geeksforgeeks.org/data-structures/"
xmr_url="https://xmr.omine.org/"

def get_hashrate(*args):
	json_api		='https://xmr.omine.org:8122/stats_address?address=4AQRSUjomb8YvgrCbr7NpJa6255CGZzCY5okkTnYcP9R471SBubcAyWYAaAdaAABZS2tpF9w214WGKaJX6t3FouRDLW724d'
	# page_raw_html 	= requests.get(xmr_url).content
	# page_soup 		= soup(page_raw_html,'html5lib')
	json_response 	= requests.get(json_api).content
	data_object 	= json.loads(json_response)
	return data_object['stats']['hashrate']

print (get_hashrate())


# print(json_response[])
	
# print(page_soup)
# hash1=page_soup.findAll(re.compile("pan")) 


