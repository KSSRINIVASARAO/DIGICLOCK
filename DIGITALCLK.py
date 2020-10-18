from tkinter import *
import time
root=Tk()
root.title("DIGITAL_CLOCK")
root.geometry("1350x700+0+0")
root.config(bg="snow2")

def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    #print(h,m,s)
    if int(h)>12 and int(m)>0:
        lbl_noon.config(text="PM")
        
    if int(h)>12:
        h=str((int(h)-12))
        print(h)

    
        
    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200,clock)

lbl_hr=Label(root,text="12",font=("STENCIL",50,"bold"),bg="indian red",fg="White")
lbl_hr.place(x=350,y=200,width=150,height=150)

lbl_hr1=Label(root,text="HOUR",font=("STENCIL",20,"bold"),bg="indian red",fg="White")
lbl_hr1.place(x=350,y=360,width=150,height=50)

lbl_min=Label(root,text="60",font=("STENCIL",50,"bold"),bg="salmon",fg="White")
lbl_min.place(x=520,y=200,width=150,height=150)

lbl_min1=Label(root,text="MINUTES",font=("STENCIL",20,"bold"),bg="salmon",fg="White")
lbl_min1.place(x=520,y=360,width=150,height=50)

lbl_sec=Label(root,text="60",font=("STENCIL",50,"bold"),bg="ivory3")
lbl_sec.place(x=690,y=200,width=150,height=150)

lbl_sec1=Label(root,text="SECOND",font=("STENCIL",20,"bold"),bg="ivory3",fg="White")
lbl_sec1.place(x=690,y=360,width=150,height=50)

lbl_noon=Label(root,text="AM",font=("STENCIL",50,"bold"),bg="medium orchid",fg="White")
lbl_noon.place(x=860,y=200,width=150,height=150)

lbl_noon1=Label(root,text="NOON",font=("STENCIL",20,"bold"),bg="medium orchid",fg="White")
lbl_noon1.place(x=860,y=360,width=150,height=50)

clock()
root.mainloop()
    
