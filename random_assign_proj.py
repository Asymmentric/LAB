import random
from tkinter import *
window=Tk()
window.geometry("600x500")
window.title("Title")
Strvar=StringVar()
Strvar.set(" ")
lb1=Label(window,bg="red",text="PGM-9")
lb1.grid(row=0,column=0,padx=10)
lb1=Label(window,text="Ent. no of pgms")
lbl.grid(row=1,column=0,padx=10)
lbl=Label(window,text="ent no of studs")
lbl.grid(row=2,column=0,pady=20)
inputField1=Entry(window,width=10).grid(row=1,column=1,pady=20)
inputField2=Entry(window,width=10).grid(row=2,column=1,pady=20)
def assign():
  programs=inputField1.get()
  students=inputField2.get()
  if programs.isdigit() and students.isdigit():
    programs=int(programs)
    students=int(students)
    data=""
    for i in range(1,student+1):
      data+="Std "+str(i)+",pgm"+str(random.randrange(1,programs+1)+"\n"
     print(data)
     csvfile=open("std.csv","w")
     csvfile.write(data)
     csvfile.close()
     Strvar.set("CSV file created")
  else:
     Strvar.set("invalid entry')
                
btn=Button(window,text="submit",command=assign)
btn.grid(row=3)
msg=Label(window,textvaribale=Strvar).grid(row=4)
window.mainloop()
