import socket
from threading import Thread
from tkinter import *




#client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#name=input("Enter Your Name: ")
#ip='127.0.0.1'
#port=5500
#client.connect((ip,port))
#print("Connected with server")

class chat:
    def __init__(self):
        self.window=Tk()
        self.window.withdraw()
        self.login=Toplevel()
        self.login.title("Login Screen")
        self.login.geometry("300x300")
        self.login.configure(bg="white")

        self.header=Label(self.login,text="Please Login to Continue",bg="white",fg="black",font=("Times New Roman",12),bd=1)
        self.header.place(x=80,y=30)

        self.nameLabel=Label(self.login,text="Name",bg="white",fg="black",font=("Times New Roman",12),bd=1)
        self.nameLabel.place(x=50,y=60)
        self.name=Entry(self.login,text="",width=25,bd=2)
        self.name.place(x=95,y=60)

        self.continueButton=Button(self.login,text="Continue",bg="white",fg="black",font=('Times New Roman',15),bd=4,command=lambda:self.continueFunction(self.name.get()))
        self.continueButton.place(x=100,y=100)

        self.window.mainloop()
    
    def continueFunction(self,name):
        self.login.destroy()
        self.name=name

gui=chat()



#def receive():
 #   while True:
  #      try:
   #         message=client.recv(2048).decode('utf-8')
    #        if message=='name':
     #           client.send(name.encode('utf-8'))
      #      else:
       #         print(message)
        #except:
         #   print("Error Occured")
          #  client.close()
           # break

#def write():
 #   while True:
  #      message=name+":"+input('')
   #     client.send(message.encode('utf-8'))





#thread1=Thread(target=receive)
#thread1.start()

#thread2=Thread(target=write)
#thread2.start()