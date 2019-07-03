#==========Bibliotecas===========#
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase


#==========Janela===========#
jan = Tk()
jan.title('Login System - Acess Panel')
jan.geometry('600x300')
jan.configure(background='white')
jan.resizable(width='false', height='false')
jan.attributes('-alpha', 0.9)
jan.iconbitmap(default='logoIcon.ico')

#==========Upload Image===========#
logo = PhotoImage(file='login.png')
logo2 = PhotoImage(file='login3.png')

#==========Widgets===========#
LeftFrame = Frame(jan, width='200', height='300', bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width='395', height='300', bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)

logoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
logoLabel.place(x=40, y=20)

logo2Label = Label(LeftFrame, image=logo2, bg='MIDNIGHTBLUE')
logo2Label.place(x=40, y=170)

#==========Login===========#
UserLabel = Label(RightFrame, text='Username: ',font=('Century Gothic', 20),bg='MIDNIGHTBLUE',fg='white')
UserLabel.place(x=20, y=81)

UserEntry = ttk.Entry(RightFrame, width=31)
UserEntry.place(x=164, y=96)

#==========Password==========#
PassLabel = Label(RightFrame, text='Password: ',font=('Century Gothic', 20),bg='MIDNIGHTBLUE',fg='white')
PassLabel.place(x=22, y=133)

PassEntry = ttk.Entry(RightFrame,width=32,show='*')
PassEntry.place(x=158, y=146)

#==========Button==========#
loginButton = ttk.Button(RightFrame,text='Login', width=25)
loginButton.place(x=25, y=200)

def Register():
    #removendo widgets de login
    loginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #alinhando novas posições para tela cadastro
    UserLabel.place(x=18, y=90)
    UserEntry.place(x=162, y=103)

    PassLabel.place(x=18, y=130)
    PassEntry.place(x=156, y=142)
    
    #inserindo widgets de cadastro
    NomeLabel = Label(RightFrame,text='Name:',font=('Century Gothic', 20),bg='MIDNIGHTBLUE',fg='white')
    NomeLabel.place(x=20, y=10)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=116, y=24)

    EmailLabel = Label(RightFrame,text='E-mail:',font=('Century Gothic', 20),bg='MIDNIGHTBLUE',fg='white')
    EmailLabel.place(x=20, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=116, y=63)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        DataBase.cursor.execute("""
        INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
        """,(Name,Email,User,Pass))
        DataBase.conn.commit()
        messagebox.showinfo(title='Register Info', message='Registro Efetuado Com Sucesso!')

    Register = ttk.Button(RightFrame, text='Register', width=25, command=RegisterToDataBase)
    Register.place(x=25, y=200)
    
    #Removendo tela de cadastro

    def BackToLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Back.place(x=5000)
        Register.place(x=5000)
        #Posicionado Botões anteriores
        RegisterButton.place(x=195, y=200)
        loginButton.place(x=25, y=200)
        

    Back = ttk.Button(RightFrame, text='Back',width=25, command=BackToLogin)
    Back.place(x=195, y=200)

    

RegisterButton = ttk.Button(RightFrame,text='Register', width=25, command=Register)
RegisterButton.place(x=195, y=200)

#==========Init===========#
jan.mainloop()
