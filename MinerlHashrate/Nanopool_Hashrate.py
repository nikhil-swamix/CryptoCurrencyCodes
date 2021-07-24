
from time import sleep as wait
import json
import datetime
def logbook(data):
	open('LastHashUpdate.txt','a').write(data+'\n')

def api_peek(url):
	import requests
	try:
		response=requests.get(url).text
		return json.loads(response)

	except Exception as e:
		print(e)

def XMR_basic_info():
	while True:
		result=api_peek(Basic+account)
		result['data']['balance']=round(result['data']['balance'],5)
		logbook(str(result['data'])+'\t@'+str(datetime.datetime.now())[:-5])
		print(json.dumps(result,indent=4))
		wait(60)

def XMR_hashrate_averages():
	while True:
		result=api_peek(Average_Hashrate+account)["data"]
		for k,v in result.items():
			result[k]=str(int(v))+' H/s'

		print(json.dumps(result,indent=4))
		wait(60)

def XMR_full_details():
	while True:
		result=api_peek(userStat+account)["data"]
		print('\n')
		print(json.dumps(result,indent=4))
		wait(15)
		
account='4AQRSUjomb8YvgrCbr7NpJa6255CGZzCY5okkTnYcP9R471SBubcAyWYAaAdaAABZS2tpF9w214WGKaJX6t3FouRDLW724d'
Basic='https://api.nanopool.org/v1/xmr/balance_hashrate/'
Average_Hashrate='https://api.nanopool.org/v1/xmr/avghashrate/'
userStat='https://api.nanopool.org/v1/xmr/user/'


XMR_basic_info()
# XMR_hashrate_averages()
# XMR_full_details()



