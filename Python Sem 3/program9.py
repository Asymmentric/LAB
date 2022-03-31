from tkinter import *
import random

window = Tk()
window.title("Program 9")
window.geometry("300x200")

errMsg = StringVar()

l1 = Label(window,text= "Program 9")
l1.grid(row=0)

l2= Label(window,text="Enter the student no.")
l2.grid(row=1,column=0)
student=Entry(window,width=25)
student.grid(row=1,column=1)

l3=Label(window,text="Enter the program no.")
l3.grid(row=2,column=0)
program=Entry(window,width=25)
program.grid(row=2,column=1)

def randAssign():
    studentNo = student.get()
    programNo = program.get()
    detail=" "
    if studentNo.isnumeric() and programNo.isnumeric():
        studentNo = int(studentNo)
        programNo = int(programNo)
        for s in range(1,studentNo +1):
            detail +="student" + str(s)+","+"Program"+str(random.randint(1,programNo))+"\n"
        print(detail)
        file=open("studentProgram.csv","w")
        file.write(detail)
        file.close()
        errMsg.set("studentProgram.csv file has been created")
    else:
        errMsg.set("Not valid input")
assign = Button(window,width=10,text="Assign",command=randAssign)
assign.grid(row=3)
msg=Label(window,textvariable=errMsg)
msg.grid(row=4,column=0)
window.mainloop()
