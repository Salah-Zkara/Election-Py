import random
from hashlib import md5
import pickle
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import cx_Oracle




def Query_DB(query):
    connection_string = "system/salah2001@localhost/SALZKARA"
    connection = None
    res = None;
    try:
		#create connection
	    connection = cx_Oracle.connect(connection_string)
	    cur = connection.cursor()
	    cur.execute(query)
	    res = cur.fetchall()
    except cx_Oracle.Error as error:
	    print(error)


    finally:
	    # release the connection
	    if connection:
	    	connection.close()
	    return res



def Inser_DB(stm):
	connection_string = "system/salah2001@localhost/SALZKARA"
	connection = None
	res = None
	try:
		#create connection
		connection = cx_Oracle.connect(connection_string)
		cur = connection.cursor()
		cur.execute(stm)
		#cur.execute("commit")
	except cx_Oracle.Error as error:
		print(error)

	finally:
		# release the connection
		if connection:
			connection.commit()
			#print("OK")
			cur.close()
			connection.close()
		return res


def prcp_gui(background_color):
	window.resizable(0, 0)
	state = DISABLED
	#state = None
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Test",command=None,state = state).place(x=20,y=170)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Test",command=None,state = state).place(x=420,y=170)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Test",command=None,state = state).place(x=20,y=220)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Test",command=None,state = state).place(x=420,y=225)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Test",command=None,state = state).place(x=220,y=280)

background_color="#32a6a8"
button_color="#576161"
button_font="none 12 bold"
window = Tk()
window.geometry("653x350")
window.title("Election 2020 Admin Dashboard by ZKARA(©)")
window.configure(background=background_color)
window.iconbitmap('./.resources/vote.ico')
imge=Image.open("./.resources/Team Male.png")
photo=ImageTk.PhotoImage(imge)
lab=Label(image=photo,bg=background_color)
lab.place(x=272,y=20)
prcp_gui(background_color)
window.mainloop()
