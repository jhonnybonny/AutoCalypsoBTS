import os
#import sys
import pyautogui
from tkinter import *
from tkinter import ttk



 
def click_button():
    stream = os.popen('sudo gnome-terminal -- ./trx.sh')
    out = stream.read()
 
def click_button2():
    stream2 = os.popen('sudo  gnome-terminal -- ./transceiver.sh')
    out2 = stream2.read()
 
def click_button3():
    stream3 = os.popen('sudo gnome-terminal -- ./nitb.sh')
    out3 = stream3.read()
 
def click_button4():
    stream4 = os.popen('sudo gnome-terminal -- ./osmobts.sh')
    out4 = stream4.read()
    
def click_button5():
    stream5 = os.popen('sudo featherpad /usr/src/CalypsoBTS/openbsc.cfg')
    out5 = stream5.read()
    
def click_button6():
    stream6 = os.popen('sudo featherpad /usr/src/CalypsoBTS/osmo-bts-trx-calypso.cfg')
    out6 = stream6.read()
    
def click_button7():
    stream7 = os.popen('sudo python /usr/src/CalypsoBTS/sub.py')
    out7 = stream7.read()
    pyautogui.alert(out7 , button='Close' , title='SUBSCRIBERS', )

def click_button8():
    stream8 = os.popen('sudo rm /usr/src/CalypsoBTS/hlr.sqlite3 >/dev/null 2>&1 & echo "REMOVED"')
    out8 = stream8.read()
    pyautogui.alert(out8 , button='Back' , title='RM DB', )

def click_button9():
    stream9 = os.popen('cd /usr/src/CalypsoBTS/ && sudo python smS.py 111 SMStestSMS  & echo "SMS SEND!"')
    out9 = stream9.read()
    pyautogui.alert(out9 , button='Ok' , title='SMS', )

def click_button10():
    stream10 = os.popen('sudo  gnome-terminal -- ./console.sh')
    out10 = stream10.read()

def click_button11():
    stream11 = os.popen('sudo featherpad transceiver.sh')
    out11 = stream11.read()

def click_button12():
    stream12 = os.popen('sudo featherpad trx.sh')
    out12 = stream12.read()
    
 
root = Tk()
root.title("Auto CalypsoBTS")
root.geometry("600x350")
root.resizable(False, False)

#ico add
img = PhotoImage(file='ico.png')
root.tk.call('wm', 'iconphoto', root._w, img)


#tab
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='BTS')
tab_control.add(tab2, text='Subscribers')
tab_control.add(tab3, text='Help')

lbl1 = Label(tab1, text='')  
lbl1.grid(column=0, row=0)  

lbl2 = Label(tab2, text='')  
lbl2.grid(column=0, row=0)

lbl3 = Label(tab3, text='\n                                           Simple GUI for CalypsoBTS\n\n                                           Correct application launch sequence:\n                                           Load TXR > Clock > DB > BTS \n\n                                      Test SMS :\n                                       Sends Test SMS from number 111 to all sub. \n\n                                           Subscribers show:\n                                        ID, IMSI, Phone Number\n\n\n\n\n\n\n                                           *Auto CalypsoBTS by CrTh for DragonOS*')  
lbl3.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')


 
btn = Button(tab1, text="Load TRX", background="#B7B7B7", foreground="#000",
             padx="35", pady="10", font="16", command=click_button)
 
btn.place(x=200, y=150 , anchor=CENTER)
 
#btn.pack(side=TOP)
 
btn2 = Button(tab1, text="Clock", background="#40E0D0", foreground="#000",
             padx="50", pady="10", font="16", command=click_button2)
 
btn2.place(x=400, y=150, anchor=CENTER)
 
# btn2.pack()
 
btn3 = Button(tab1, text="DB", background="#B7B7B7", foreground="#000",
             padx="50", pady="10", font="16", command=click_button3)
 
btn3.place(x=200, y=250, anchor=CENTER)
 
# btn3.pack()
 
btn4 = Button(tab1, text="! BTS !", background="#FF0000", foreground="#000",
             padx="50", pady="10", font="16", command=click_button4)
 
btn4.place(x=400, y=250, anchor=CENTER)
 
# btn4.pack()

btn5 = Button(tab1, text="OpenBSC.cfg", background="#00C957", foreground="#000",
             padx="40", pady="10", font="16", command=click_button5)
 
btn5.place(x=200, y=50, anchor=CENTER)
 
# btn5.pack()
btn6 = Button(tab1, text="OsmoBTS.cfg", background="#00C957", foreground="#000",
             padx="40", pady="10", font="16", command=click_button6)
 
btn6.place(x=400, y=50, anchor=CENTER)
 
# btn6.pack()
btn7 = Button(tab2, text="Subscribers", background="#E066FF", foreground="#000",
             padx="40", pady="10", font="16", command=click_button7)
 
btn7.place(x=400, y=50, anchor=CENTER)
 
# btn7.pack()

btn8 = Button(tab2, text="! Remove DB !", background="#1A1A1A", foreground="#FF0000",
             padx="40", pady="10", font="16", command=click_button8)
 
btn8.place(x=200, y=50, anchor=CENTER)


btn9 = Button(tab2, text="Test SMS", background="#FFD700", foreground="#000",
             padx="100", pady="10", font="16", command=click_button9)
 
btn9.place(x=300, y=150, anchor=CENTER)

btn10 = Button(tab2, text="OpenBSC Console", background="#00C957", foreground="#000",
             padx="100", pady="10", font="16", command=click_button10)
 
btn10.place(x=300, y=250, anchor=CENTER)


btn11 = Button(tab1, text="⚙", background="#40E0D0", foreground="#000",
             padx="8", pady="5", font="50", command=click_button11)
 
btn11.place(x=500, y=150, anchor=CENTER)

btn12 = Button(tab1, text="⚙", background="#B7B7B7", foreground="#000",
             padx="8", pady="5", font="50", command=click_button12)
 
btn12.place(x=100, y=150, anchor=CENTER)

 
root.mainloop()
