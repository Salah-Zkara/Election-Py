import random
from hashlib import md5
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import cx_Oracle

F=open('./.resources/connection.txt','r')
global connection_string
connection_string = F.read()
F.close()

def Query_DB(query):
	connection = None
	res = None
	flag = False
	try:
		#create connection
		connection = cx_Oracle.connect(connection_string)
		cur = connection.cursor()
		cur.execute(query)
		res = cur.fetchall()
		flag = True
	except cx_Oracle.Error as error:
		print(error)
		flag = error


	finally:
		# release the connection
		if connection:
			connection.close()
		return res,flag

def Inser_DB(stm):
	connection = None
	flag = False
	try:
		#create connection
		connection = cx_Oracle.connect(connection_string)
		cur = connection.cursor()
		cur.execute(stm)
		flag = True
	except cx_Oracle.Error as error:
		print(error)
		flag = error

	finally:
		# release the connection
		if connection:
			connection.commit()
			cur.close()
			connection.close()
		return flag

def Add_Elected():
	def Inscription_(Lname,Fname):
		Lname=Lname.upper()
		Fname=Fname.upper()
		result,flag = Query_DB("SELECT * FROM candidats")
		if flag == True:
			for line in result:
				if (line[2]==Lname) and (line[1]==Fname):
					return False
			return True
		else:
			pass
			#tkinter.messagebox.showinfo("ERROR!!",str(flag))
			
	def click():
		Lname=textentry1.get().upper()
		Fname=textentry2.get().upper()
		if(Inscription_(Lname,Fname)==False) :
			tkinter.messagebox.showinfo("ALERT!!","Ce candidat est déjà enregistré!")
			window2.destroy()
		else:
			num,flag = Query_DB("SELECT COUNT(*) FROM candidats")
			if flag == True:
				i = int(num[0][0])+1
				stm = f"INSERT INTO candidats VALUES('C{str(i)}','{Fname}','{Lname}')"
				flag = Inser_DB(stm)
				if flag == True:
					tkinter.messagebox.showinfo("INFO!!","ajouté avec succès")
					clear_()
				else:
					tkinter.messagebox.showinfo("ERROR!!",str(flag))
			else:
				tkinter.messagebox.showinfo("ERROR!!",str(flag))
			window2.destroy()

	window2 =Toplevel()
	window2.title("Ajouter un candidat")
	window2.configure(background="#ebd034")
	window2.geometry("270x180")
	window2.resizable(0, 0)
	window2.iconbitmap('./.resources/Team-Male.ico')
	Label(window2,text="Nom:",bg=background_color).place(x=10,y=10)
	textentry1= Entry(window2,bg="white",width=38)
	textentry1.place(x=10,y=30)
	Label(window2,text="Prenom:",bg=background_color).place(x=10,y=60)
	textentry2= Entry(window2,bg="white",width=38)
	textentry2.place(x=10,y=80)
	Button(window2,font="none 9 italic",fg="white",bg="black",text="Add",command=click).place(x=190,y=120)
	window2.mainloop()


def Liste_Candidat():
	F,flag=Query_DB("SELECT * FROM candidats")
	if flag == True:
		i=1
		R=""
		for line in F:
			R+=line[0]+" -->  "+line[1]+" "+line[2]+'\n'
			i+=1
		tkinter.messagebox.showinfo("Liste des candidats",R)
		return i
	else:
		tkinter.messagebox.showinfo("ERROR!!",str(flag))


def Delete_cand():
	def click():
		i = 0
		j = 0
		for e in D:
			if D[e].get() == 1:
				j += 1
				stm = f"DELETE FROM candidats WHERE code = '{e}' "
				flag = Inser_DB(stm)
				if flag != True:
					i +=1
					tkinter.messagebox.showinfo("ERROR!!",str(flag))
		j = j - i
		tkinter.messagebox.showinfo("ALERT!!",str(j)+" candidats supprimer avec succès")
		clear_()
		window5.destroy()
		
	def sel_all():
		for a in A:
			a.select()
	def dsel_all():
		for a in A:
    			a.deselect()
	
	n=Liste_Candidat()
	window5 = Toplevel()
	window5.resizable(0, 0)
	window5.title("Candidats")
	window5.iconbitmap('./.resources/gear.ico')
	window5.configure(background=background_color)
	Label(window5,text="veuillez selectionnez les candidats a supprimer",bg=background_color).pack()
	D = {}
	A = []

	text,flag = Query_DB("SELECT code FROM candidats")
	if flag == True:
		i = 0
		for a in text:
			t = a[0]
			D[t] = IntVar()
			A.append(Checkbutton(window5,bg=background_color, text = t,variable = D[t],onvalue = 1,offvalue = 0 ))
			A[i].pack(side = TOP, ipady = 5)
			i+=1
	else:
		tkinter.messagebox.showinfo("ERROR!!",str(flag))


	Button(window5,font="none 9 italic",fg="white",bg="black",text="SELECT ALL",command=sel_all).pack(side = 'left',padx = 10)
	Button(window5,font="none 9 italic",fg="white",bg="black",text="DESELECT ALL",command=dsel_all).pack(side = 'right',padx = 10)
	Button(window5,font="none 9 italic",fg="white",bg="black",text="DELETE",command=click).pack(padx=15,pady=15)
	window5.mainloop()


def Delete_users():
	def click():
		i = 0
		j = 0
		for e in D:
			if D[e].get() == 1:
				j += 1
				stm = f"DELETE FROM personnes WHERE login = '{e}' "
				flag = Inser_DB(stm)
				if flag != True:
					i +=1
					tkinter.messagebox.showinfo("ERROR!!",str(flag))
		j = j - i
		tkinter.messagebox.showinfo("ALERT!!",str(j)+" utilisateurs supprimer avec succès")
		window5.destroy()
		
	def sel_all():
		for a in A:
			a.select()
	def dsel_all():
		for a in A:
    			a.deselect()
	
	window5 = Toplevel()
	window5.resizable(0, 0)
	window5.title("Utilisateurs")
	window5.iconbitmap('./.resources/gear.ico')
	window5.configure(background=background_color)
	Label(window5,text="veuillez selectionnez les utilisateurs a supprimer",bg=background_color).pack()
	D = {}
	A = []

	text,flag = Query_DB("SELECT login FROM personnes")
	if flag == True:
		i = 0
		for a in text:
			t = a[0]
			D[t] = IntVar()
			A.append(Checkbutton(window5,bg=background_color, text = t,variable = D[t],onvalue = 1,offvalue = 0 ))
			A[i].pack(side = TOP, ipady = 5)
			i+=1
	else:
		tkinter.messagebox.showinfo("ERROR!!",str(flag))

	Button(window5,font="none 9 italic",fg="white",bg="black",text="SELECT ALL",command=sel_all).pack(side = 'left',padx = 10)
	Button(window5,font="none 9 italic",fg="white",bg="black",text="DESELECT ALL",command=dsel_all).pack(side = 'right',padx = 10)
	Button(window5,font="none 9 italic",fg="white",bg="black",text="DELETE",command=click).pack(padx=15,pady=15)
	window5.mainloop()


def Dic_candidat():
	c=[]
	C,flag=Query_DB("SELECT * FROM candidats")
	if flag == True:
		i=1
		for line in C:
			i+=1
			c.append(line[0])
		D={}
		for e in c:
			D[e]=0
		return D
	return False


def Dic_candidat_DB(D = Dic_candidat()):
	if D == False:
		return False
	Inser_DB("DELETE FROM stats")
	for e in D:
		stm = f"INSERT INTO stats VALUES('{e}','{D[e]}','NO')"
		Inser_DB(stm)


def DB_Dic():
	A = Query_DB("SELECT CODE,POINTS FROM stats")
	D={}
	for a in A:
		D[a[0]] = a[1]
	return D

def clear_():
	D=Dic_candidat()
	flag = Dic_candidat_DB(D)
	if flag == False:
		tkinter.messagebox.showinfo("ERROR!!","Error!!")
		return False
	Inser_DB("UPDATE personnes SET STATUS='OK'")
	tkinter.messagebox.showinfo("ALERT!!","Les résultats sont mis à zéro.\ntous les membres puissent voter à nouveau!!")


def prcp_gui(background_color):
	window.resizable(0, 0)
	state = DISABLED
	#state = None
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Ajouter un candidat",command=Add_Elected).place(x=20,y=170)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Liste: code --> candidat",command=Liste_Candidat).place(x=420,y=170)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Supprimer les candidats",command=Delete_cand).place(x=20,y=220)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Supprimer les utilisateurs",command=Delete_users).place(x=420,y=225)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Clear Result",command=clear_).place(x=220,y=280)



background_color="#ebd034"
button_color="#f80000"
button_font="none 12 bold"
window = Tk()
window.geometry("653x350")
window.title("Election 2020 Admin Dashboard by ZKARA(©)")
window.configure(background=background_color)
window.iconbitmap('./.resources/gear.ico')
imge=Image.open("./.resources/admin.png")
photo=ImageTk.PhotoImage(imge)
lab=Label(image=photo,bg=background_color)
lab.place(x=272,y=20)
prcp_gui(background_color)
window.mainloop()
