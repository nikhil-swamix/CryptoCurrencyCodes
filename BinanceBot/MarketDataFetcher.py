from mxproxy import mx
import time
import math
def fetch_index_details(INDEX):
	url='https://www.binance.com/dapi/v1/premiumIndex'
	for i in mx.get_page(url).json():
		if i['symbol']==INDEX: #bcs orign contains many symbols 
			return i

def get_mark_price(INDEX='BTCUSD_PERP'):
	return roundoff(fetch_index_details(INDEX)['markPrice'])

def roundoff(strfloat,precision=1):
	basedigits=len(strfloat.split('.'))
	if basedigits <=2:
		precision=3

	return round(float(strfloat),precision)

def calc_trend(INDEX):
	data=fetch_index_details(INDEX)
	estimate=roundoff(data['estimatedSettlePrice'])
	indexPrice=roundoff(data['indexPrice'])
	markPrice=roundoff(data['markPrice'])
	deltaEI= estimate - indexPrice 
	deltaEM= estimate - markPrice
	directionI = '🔼' if deltaEI > 0 else '🔽'
	directionM = '🔼' if deltaEM > 0 else '🔽'
	print(f"{INDEX}: I:{directionI}\t|\tM:{directionM} INFO: E={estimate:<7} I={indexPrice:<7} M={markPrice:<7}")
	...

if __name__ == '__main__':

	while True:
		print (fetch_index_details("ETHUSD_PERP"))
		time.sleep(1)
# 'altzone', 'asctime', 'clock', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname'

