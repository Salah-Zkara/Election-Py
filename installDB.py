from tkinter import *
import tkinter.messagebox
import cx_Oracle
from PIL import ImageTk, Image

F=open('./.resources/connection.txt','r')
global connection_string
connection_string = F.read()
F.close()



def Inser_DB(stm):
	connection = None
	flag = False
	try:
		#create connection
		connection = cx_Oracle.connect(connection_string)
		cur = connection.cursor()
		cur.execute(stm)
		#cur.execute("commit")
		flag = True
	except cx_Oracle.Error as error:
		print(error)
		flag = error

	finally:
		# release the connection
		if connection:
			connection.commit()
			#print("OK")
			cur.close()
			connection.close()
		return flag




def install():
	F = open('./create.sql','r')
	stm = F.readlines()
	L = []
	errors = []
	for s in stm:
		L.append(s.split(';')[0])
	F.close()

	for l in L:
		flag = Inser_DB(l)
		if "table or view does not exist" in str(flag):
			continue

		elif flag != True:
			errors.append(flag)
	if len(errors) == 0 :
		tkinter.messagebox.showinfo("INFO!!","installè avec succès")
	else :
		E = ""
		for e in errors:
			E = E + str(e)
		tkinter.messagebox.showinfo("ERROR!!",str(E))


def prcp_gui(background_color):
	window.resizable(0, 0)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Install",command=install).pack(side = BOTTOM,pady = 40)


background_color="#ebd034"
button_color="#f80000"
button_font="none 12 bold"
window = Tk()
window.geometry("300x250")
window.title("DB Installer by ZKARA(©)")
window.configure(background=background_color)
window.iconbitmap('./.resources/oracle.ico')
imge=Image.open("./.resources/oracle.png")
photo=ImageTk.PhotoImage(imge)
lab=Label(image=photo,bg=background_color)
lab.pack(pady = 20)
prcp_gui(background_color)
window.mainloop()