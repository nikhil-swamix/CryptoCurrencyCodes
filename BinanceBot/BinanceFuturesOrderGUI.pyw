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
	'accleration':0,
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
	'accleration':0,
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
	if input_stepsize.get()!='default':
		orderConfig.update({'stepsize':input_stepsize.get()})

	if input_delta.get()!='default':
		orderConfig.update({'delta':input_delta.get()})

	if input_sizeAccleration.get()!='default':
		orderConfig.update({'sizeAccleration':input_sizeAccleration.get()})

	if input_count.get()!='default':
		orderConfig.update({'count':input_count.get()})

	orders_exec(gen_orders(**orderConfig),mode=mode)

if __name__ == '__main__':
	
	lastrow=0 
	mode='live'
	root = Tk()
	root.title('Binance Command Center')
	# root.grid_columnconfigure(0,weight=1)
	root.maxsize(800,600)
	root.iconbitmap('./images/binance-icon.ico')
	warnings='\n-'.join([
	'- triple streak rule, place order if 3 greens/reds in a row',
	'NEVER exceed hedge ratio 10%',
	'your enemy is fear of loss and greed for gains'])

	warningBox = Label (root,text=warnings,justify='left',wraplength='400')
	warningBox.grid(row=0,columnspan=2,sticky='w')

	#______________________________________________
	frame1 = Frame(root, background="#000")
	frame1.grid(row=1, columnspan=2,sticky='ew',pady=(0))

	labelSetup={'bg':'#000','fg':'#fff','justify':tk.LEFT,'anchor':"w"}

	label_stepsize=Label(frame1,text="stepsize",**labelSetup)
	default_stepsize=StringVar(root,ETH_BASE['stepsize'])
	input_stepsize= Spinbox(frame1,from_=1,to=20,textvariable=default_stepsize)
	label_stepsize.grid(row=0,column=0,sticky='w')
	input_stepsize.grid(row=0,column=1,)

	label_delta=Label(frame1,text="delta",**labelSetup)
	default_delta=StringVar(root,ETH_BASE['delta'])
	input_delta= Spinbox(frame1,from_=1,to=20,textvariable= default_delta )
	label_delta.grid(row=0,column=2,sticky='w')
	input_delta.grid(row=0,column=3)

	label_sizeAccleration=Label(frame1,text="sizeAccl",**labelSetup)
	default_sizeAccleration=StringVar(root,ETH_BASE['sizeAccleration'])
	input_sizeAccleration= Spinbox(frame1,from_=0,to=2,textvariable=default_sizeAccleration)
	label_sizeAccleration.grid(row=1,column=0,sticky='w')
	input_sizeAccleration.grid(row=1,column=1)

	labelcount=Label(frame1,text="count",**labelSetup)
	default_count=StringVar(root,ETH_BASE['count'])
	input_count= Spinbox(frame1,from_=1,to=10,textvariable=default_count)
	labelcount.grid(row=1,column=2,sticky='w')
	input_count.grid(row=1,column=3)
	#______________________________________________


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

	modebtn = Button(root,command=lambda : mode_switcher(), text='MODE :: '+mode ,fg="white", bg="BLUE",)
	modebtn.grid(row=5,column=0,sticky='w')

	root.mainloop()	

	#change 1212