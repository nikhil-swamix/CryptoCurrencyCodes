import time,os,tkinter as tk
from tkinter import Tk, Label,Button,Frame,Entry,Spinbox,StringVar
from OrderMaker import gen_orders,orders_exec
import pyautogui
# 
ETH_BASE={
	'token':'ETHUSD_PERP',
	'size':1,
	'sizeAccleration':1,
	'stepsize':10,#Min 6!!!
	'accleration':10,
	'count':5,
	'delta':10,
	'roundoff':0
	}
ETH_SHORT={'direction':'short',	**ETH_BASE}
ETH_LONG={'direction':'long',	**ETH_BASE}

# BNB_BASE={'token':'BNBUSD_PERP','size':1,'count':6,'delta':6,'stepsize':3,'accleration':0,'roundoff':1}
# BNB_SHORT={'direction':'short',	**BNB_BASE}
# BNB_LONG={'direction':'long',  	**BNB_BASE}

BTC_BASE={
	'token':'BTCUSD_PERP',
	'size':1,
	'sizeAccleration':1,
	'stepsize':300,
	'accleration':5,
	'count':6,
	'delta':300,
 	'roundoff':0
 	}
 	
 	
BTC_LONG={'direction':'long',	**BTC_BASE}
BTC_SHORT={'direction':'short',	**BTC_BASE}
# 

'''BUTTON STYLING'''
specialChars='▲▼'
BTN_BASIC={'height':1,'width':12,'font':('monserrat', '20')}
BTN_SHORT_STYLE={'fg':'white','bg':'RED',**BTN_BASIC}
BTN_LONG_STYLE=	{'fg':'white','bg':'GREEN',**BTN_BASIC}

def mode_switcher():
	global mode
	if mode == 'demo':
		mode='live'
	else :
		mode='demo'
	modebtn['text']='MODE :: '+ mode
	print("ORDER EXEC MODE =>",mode)

def order(orderConfig):
	global mode
	if inputStepSize.get()!='default':
		orderConfig.update({'stepsize':inputStepSize.get()})
	if inputDelta.get()!='default':
		orderConfig.update({'delta':inputDelta.get()})

	orders_exec(gen_orders(**orderConfig),mode=mode)

if __name__ == '__main__':
	
	lastrow=0 
	mode='live'
	root = Tk()
	root.title('Binance Command Center')
	# root.grid_columnconfigure(0,weight=1)
	root.maxsize(800,600)
	root.iconbitmap('./images/binance-icon.ico')
	warnings='''Think Twice before putting orders, if market is up:sell::down:buy NEVER exceed hedge ratio 1.5 your enemy is fear of loss and greed for gains'''

	warningBox = Label (root,text=warnings,justify='left',wraplength='400')
	warningBox.grid(row=0,columnspan=2,sticky='w')

	frame1 = Frame(root, background="#000")
	frame1.grid(row=1, columnspan=2,sticky='ew',pady=(0))

	modebtn = Button(root,command=lambda : mode_switcher(), text='MODE :: '+mode ,fg="white", bg="BLUE",)
	modebtn.grid(row=5,column=0,sticky='w')

	labelSetup={'bg':'#000','fg':'#fff'}

	labelStepSize=Label(frame1,text="stepsize",**labelSetup)
	labelStepSize.pack(side='left',padx=(1,0))
	inputStepSize= Spinbox(frame1,from_=4,to=20,textvariable='')
	inputStepSize.pack(side='left')

	labelDelta=Label(frame1,text="delta",**labelSetup)
	labelDelta.pack(side='left',padx=(2,0))
	inputDelta= Spinbox(frame1,from_=4,to=20,textvariable='')
	inputDelta.pack(side='left')


	w = Button(root,command=lambda:order(BTC_LONG)	,text="BTC LONG▲",	**BTN_LONG_STYLE)
	w.grid(row=2,column=0)
	w = Button(root,command=lambda:order(BTC_SHORT)	,text="BTC SHORT▼",	**BTN_SHORT_STYLE)
	w.grid(row=2,column=1)

	# w = Button(root,command=lambda:order(BNB_LONG)	,text="BNB LONG▲",	**BTN_LONG_STYLE)
	# w.grid(row=3,column=0)
	# w = Button(root,command=lambda:order(BNB_SHORT)	,text="BNB SHORT▼",	**BTN_SHORT_STYLE)
	# w.grid(row=3,column=1)
	
	w = Button(root,command=lambda:order(ETH_LONG)	,text="ETH LONG▲",	**BTN_LONG_STYLE)
	w.grid(row=4,column=0)
	w = Button(root,command=lambda:order(ETH_SHORT)	,text="ETH SHORT▼",	**BTN_SHORT_STYLE)
	w.grid(row=4,column=1)


	root.mainloop()	

	#change 1212