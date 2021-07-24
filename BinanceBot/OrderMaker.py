import pyautogui
import time
import MarketDataFetcher

def gen_orders(
	token='BTCUSD_PERP',
	size=1,
	sizeAccleration=1,
	delta=150,
	accleration=10,
	stepsize='1%',
	count=5,
	direction='		',
	roundoff=1
	):
	''' 
	generates list of orders which is then executed via gui bot
	markPrice: 	current price of commodity ,
	delta:	 	delta for buy and sell margin ,
	direction: 	strandard long=call, short=put ,
	count: 		amount of orders to be generated ,
	stepPercent: sliding window step ,
	accleration : accleration in % for step stepsize.,
	sizeAccleration : sizeAccleration integer for order size,
	roundoff	: rounds off to nth place
	mardelRatio : margin to delta ratio
	trigPrice: 	is slghtly away from mark price in the long/short direction when price reached, 
				executs order with delta mergin.,
	'''
	markPrice=round(MarketDataFetcher.get_mark_price(token),roundoff)
	print({'markPrice':markPrice,'roundoff':roundoff})
	
	if delta!='default' and '%' in str(delta):
		delta=(markPrice/100)*int(delta[0:-1])
	if stepsize!='default' and '%' in str(stepsize):
		stepsize=(markPrice/100)*int(stepsize[0:-1])


	delta=round(float(delta),roundoff)
	stepsize=round(float(stepsize),roundoff)
	sizeAccleration=float(sizeAccleration)
	count=int(count)
	# print(delta,stepsize)

	adaptiveStep=round(stepsize*(accleration/100),3)
	orderlist=[]
	for i in range(count):
		if direction=='short':
			sigma=round(stepsize*(i+1),roundoff)
			marketSpread=f'{round((sigma/markPrice)*100,1)}%'
			stepsize+=adaptiveStep
			trigPrice=round(markPrice+sigma,roundoff)
			orderlist.append(
				{'trigPrice':f"{trigPrice:<3}",'takeProfit':trigPrice-delta,'stepDeltaRatio':f'{round(stepsize,2):<4}|{delta}',\
				'Spread':f'{marketSpread}|{sigma:4}','direction':direction,'size':size+(sizeAccleration*i)}
			)

		if direction=='long':
			sigma=round(stepsize*(i+1),roundoff)
			marketSpread=f'{round((-sigma/markPrice)*100,1)}%'
			stepsize+=adaptiveStep
			trigPrice=round(markPrice-sigma,roundoff)
			orderlist.append(
				{'trigPrice':f"{trigPrice:<3}",'takeProfit':trigPrice+delta,'stepDeltaRatio':f'{round(stepsize,2):<4}|{delta}',\
				'Spread':f'{marketSpread}|{sigma:4}','direction':direction,'size':size+(sizeAccleration*i)}
			)

	return orderlist


def orders_exec(orderlist,mode):
	'''requirements: binance future screen in view | TP/SL ticked | post only mode (good) '''
	[print(o) for o in orderlist]
	if mode=='demo': print("!!! DEMO MODE !!!") ; return
	priceInputField=(1115,225)
	for x in orderlist:
		pyautogui.click(priceInputField,clicks=3)
		pyautogui.write(str(x['trigPrice']))
		pyautogui.press('tab')
		# pyautogui.press('tab')
		pyautogui.write(str(x['size']))
		pyautogui.press('tab')
		pyautogui.write(str(x['takeProfit']))
		if x['direction']=='short':
			pyautogui.click(x=1189, y=572)
		if x['direction']=='long':
			pyautogui.click(x=1064, y=572)
		time.sleep(1)

def position_prober():
	time.sleep(2)
	r=pyautogui.position()
	print(r)


if __name__ == '__main__':
	import BinanceFuturesOrderGUI as GUIAPP
	import time


	# pyautogui.moveTo(x=1064, y=468)
	# position_prober()

	# ords=gen_orders(**GUIAPP.BTC_LONG)
	# print(GUIAPP.BTC_SHORT)
	ords=gen_orders(**GUIAPP.ETH_SHORT)
	[print(o) for o in ords]
	# pyautogui.press('tab',presses=2,interval=0.25)		
	pyautogui.moveTo(x=1189, y=468)
	# UNIT_TEST_CHECK_ORDERS
	# ords=gen_orders(**GUIAPP.BNB_LONG)
	# [print(o) for o in ords]
	# ords=gen_orders(**GUIAPP.BNB_SHORT)
	# [print(o) for o in ords]



	
	RULES= '''
	#TRADING RULES 
	#---STEP SIZE 1.5X DELTA
	#---STEP SIZE ~1% of current price
	#---DELTA ~1% of current price
		>>> if market is 66%red in last 10 candles then buy and viceversa for sell
		>>> close all python generated orders before placing new python order
	'''
