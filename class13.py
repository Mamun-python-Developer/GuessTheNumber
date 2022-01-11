from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import filedialog

win = Tk()

win.title("pepole")
win.geometry('600x400')

lbl1 = Label(win, text= 'GUI')
lbl1.place(x=20, y=30)

cbox = ('python', 'c++','java','c')
clist = ('My SQL','SQL','Oracal','Namechap','World','Fog')

cmb = Combobox(win, values=cbox)
cmb.place(x=20, y=90)
# cmb.pack(right)
var1 = IntVar()
# var1.set(1)
rbt1 = Radiobutton(win, text='Male', variable = var1, value = 1)
rbt2 = Radiobutton(win, text='Female', variable = var1, value = 2)
rbt1.place(x=250, y=50)
rbt2.place(x=300, y=50)

cvr1 = IntVar()
cvr2 = IntVar()
cvr3 = IntVar()
# cvr1.set(1)
# cvr2.set(1)

cbtn1 = Checkbutton(win, text='Academic', variable = cvr1)
cbtn2 = Checkbutton(win, text='professional', variable = cvr2)
cbtn3 = Checkbutton(win, text='genarel', variable = cvr3)
cbtn1.place(x=250, y=100)
cbtn2.place(x=350, y=100)
cbtn3.place(x=450, y=100)

lbox = Listbox(win, height=6, selectmode='multiple')
for item in clist:
    lbox.insert(END,item)
    lbox.place(x=450,y=150)
def btnclick():
    lbl1.configure(text='you have clicked')
    messagebox.showwarning('Info','Button press. you can do iit agagin ')
    # messagebox.showerror('Info','Button press. you can do iit agagin ')
    # messagebox.showinfo('Info','Button press. you can do iit agagin ')

def btnclear():
    ans = messagebox.askyesno('Confirm','do you went to clear text')
    if ans==True:
        lbl1.configure(text=' ')

btn = Button(win, text='click me ', command=btnclick)
btnClear = Button(win, text='click me ', command=btnclear)
btn.place(x=30, y=250)
btnClear.place(x=130, y=250)

hi = IntVar()
hi.set(6)

spbox1 = Spinbox(win, from_= 1, to=100, width=5, textvariable='hi')
spbox1.place(x=30, y=200)

spbox2 = Spinbox(win, values=(3,6,9))
spbox2.place(x=130, y=200)

def Openfd():
    fl = filedialog.askopenfilename(filetypes=(('PDF Filrs','*.pdf'),('Word file''*.doc')))
    lbl1.configure(text=fl)


btnofd = Button(win, text='Open File', command=Openfd)
btnofd.place(x=30, y=150)

win.mainloop()