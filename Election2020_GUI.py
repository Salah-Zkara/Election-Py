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




def randomPass():
	
	def randomString():
		letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		return ''.join(random.choice(letters) for i in range(4))
	def randomNum():
		return ''.join(str(random.randint(0,9)) for i in range(4))
	return randomString()+'@'+randomNum()


def Inscription():
	def Inscription_(Lname,Fname):
		Lname=Lname.upper()
		Fname=Fname.upper()
		result = Query_DB("SELECT * FROM personnes")
		for line in result:
			if (line[0]==Lname) and (line[1]==Fname):
				return False
		return True
	def click():
		Lname=textentry1.get().upper()
		Fname=textentry2.get().upper()
		if(Inscription_(Lname,Fname)==False) :
			tkinter.messagebox.showinfo("ALERT!!","vous etes deja inscrit!")
			window2.destroy()
		else:
			i=int(Query_DB("SELECT COUNT(*) FROM personnes")[0][0])+1
			if(i<10) :
				code='E00'+str(i)
			elif(i<100):
				code='E0'+str(i)
			else:
				code='E'+str(i)
			paswd=randomPass()
			stm = f"INSERT INTO personnes VALUES('{Lname}','{Fname}','{code}','{str(md5(paswd.encode()).hexdigest())}','OK')"
			Inser_DB(stm)
			
			window4= Tk()
			window4.geometry("250x100")
			window4.title("INFO!!")
			window4.resizable(0,0)
			window4.configure(background=background_color)
			Label(window4,text="inscription réussie",bg=background_color).pack()
			output= Text(window4,width=25,height=10,wrap=WORD,background=background_color)
			output.pack()
			m="Login: "+code+"\nPassword: "+paswd
			output.insert(END,m)
			window2.destroy()
			window4.iconbitmap('./.resources/Team-Male.ico')
			window4.mainloop()
	window2 =Tk()
	window2.title("Inscription")
	window2.configure(background="#32a6a8")
	window2.geometry("270x180")
	window2.resizable(0, 0)
	window2.iconbitmap('./.resources/Team-Male.ico')
	Label(window2,text="Nom:",bg=background_color).place(x=10,y=10)
	textentry1= Entry(window2,bg="white",width=38)
	textentry1.place(x=10,y=30)
	Label(window2,text="Prenom:",bg=background_color).place(x=10,y=60)
	textentry2= Entry(window2,bg="white",width=38)
	textentry2.place(x=10,y=80)
	Button(window2,font="none 9 italic",fg="white",bg="black",text="Sign Up",command=click).place(x=190,y=120)
	window2.mainloop()

def Liste_Candidat():
	F=Query_DB("SELECT * FROM candidats")
	i=1
	R=""
	for line in F:
		R+=line[0]+" -->  "+line[1]+" "+line[2]+'\n'
		i+=1
	#R+='C'+str(i)+" -->  blanc\n"
	tkinter.messagebox.showinfo("Liste des candidats",R)
	return i

def Statistiques():
	D = DB_Dic()


	n=Query_DB("SELECT SUM(POINTS) FROM stats")[0][0]
	if(n==0) :
		n=1
	A = Query_DB("SELECT * FROM candidats")
	i=1
	R=""
	for a in A:
		R+=a[1]+" "+a[2]+"  --> "+str(D['C'+str(i)])+" votes "+str(D['C'+str(i)]*100/n)+"%"+'\n'
		i+=1
	tkinter.messagebox.showinfo("Statistiques",R)


def Vote():
	radio_var=StringVar()
	def click1():
		code=textentry1.get().upper()
		paswd=str(md5(textentry2.get().upper().encode()).hexdigest())
		window3.destroy()
		F=Query_DB("SELECT * FROM personnes")
		u=0
		for line in F:
			l = list(line)
			if(l[-3]==code) and (l[-2]==paswd) :
				u=1
				tkinter.messagebox.showinfo("INFO","Bienvenue "+l[1]+" "+l[0])
				if(l[-1]!='OK') :
					tkinter.messagebox.showinfo("ALERT!!","vous avez deja voté!!! ")
					return False
				l[-1]='NO'
				def click2():
					window5.destroy()		
					D = DB_Dic()
					choice=v.get()
					if choice in D:
						D[choice]+=1
						stm = f"UPDATE stats SET POINTS = '{D[choice]}' WHERE CODE = '{choice}'"
						Inser_DB(stm)
						tkinter.messagebox.showinfo("ALERT!!","Merci pour votre vote!")
						stm = f"UPDATE personnes SET STATUS='NO' WHERE LOGIN='{l[2]}'"
						Inser_DB(stm)
					else:
						tkinter.messagebox.showinfo("ALERT!!","Contact your administrator to clear results!")

		if(u==0) :
			tkinter.messagebox.showinfo("ALERT!!","code ou mot de passe incorrecte!")
			return False
		n=Liste_Candidat()
		window5 = Tk()
		window5.resizable(0, 0)
		window5.title("Vote")
		window5.iconbitmap('./.resources/vote.ico')
		window5.configure(background=background_color)
		#window5.geometry("225x200")
		Label(window5,text="veuillez votez pour votre candidat",bg=background_color).pack()
		values={}
		for i in range(1,n):
			C='C'+str(i)
			values[C]=C

		v = StringVar(window5, "1") 
		for (text, value) in values.items(): 
		    Radiobutton(window5,bg=background_color, text = text, variable = v, value = value).pack(side = TOP, ipady = 5) 
		Button(window5,font="none 9 italic",fg="white",bg="black",text="VOTE",command=click2).pack()
		window5.mainloop()

	window3 = Tk()
	window3.resizable(0, 0)
	window3.title("Login")
	window3.iconbitmap('./.resources/Team-Male.ico')
	window3.configure(background=background_color)
	window3.geometry("225x150")
	Label(window3,text="Saisir votre code(E...):",bg=background_color).place(x=20,y=10)
	textentry1= Entry(window3,bg="white",width=30)
	textentry1.place(x=20,y=30)
	Label(window3,text="Password:",bg=background_color).place(x=20,y=60)
	textentry2= Entry(window3,show='*',bg="white",width=30)
	textentry2.place(x=20,y=80)
	Button(window3,font="none 9 italic",fg="white",bg="black",text="Submit",command=click1).place(x=90,y=120)
	window3.mainloop()

	
def Dic_candidat():
	c=[]
	C=Query_DB("SELECT * FROM candidats")
	i=1
	for line in C:
		i+=1
		c.append(line[0])
	D={}
	for e in c:
		D[e]=0
	return D




def Dic_candidat_DB(D = Dic_candidat()):
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
	Dic_candidat_DB()
	Inser_DB("UPDATE personnes SET STATUS='OK'")
	tkinter.messagebox.showinfo("ALERT!!","Les résultats sont mis à zéro.\ntous les membres puissent voter à nouveau!!")


def prcp_gui(background_color):
	window.resizable(0, 0)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Inscription",command=Inscription).place(x=20,y=170)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Liste codes --> candidat",command=Liste_Candidat).place(x=420,y=170)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Voter",command=Vote).place(x=20,y=220)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Statistiques",command=Statistiques).place(x=420,y=225)
	Button(window,font=button_font,fg="white",bg=button_color,width=20,text="Clear Result",command=clear_).place(x=220,y=280)

background_color="#32a6a8"
button_color="#576161"
button_font="none 12 bold"
window = Tk()
window.geometry("653x350")
window.title("Election 2020 by ZKARA(©)")
window.configure(background=background_color)
window.iconbitmap('./.resources/vote.ico')
imge=Image.open("./.resources/Team Male.png")
photo=ImageTk.PhotoImage(imge)
lab=Label(image=photo,bg=background_color)
lab.place(x=272,y=20)
prcp_gui(background_color)
DB_Dic()
window.mainloop()
