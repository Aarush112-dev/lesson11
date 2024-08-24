from tkinter import *

window = Tk()
window.title("Memorizer")
window.geometry("600x400")

enter = Entry(window,width=40)
enter.pack(side=TOP,padx=10,pady=10)
add = Button(window,text="ADD",width=20,height=2)
add.pack(side=TOP,pady=10,padx=10)

open = Button(window,text="OPEN",width=20,height=2)
open.pack(side=TOP,padx=10,anchor="w")
delete = Button(window,text="DELETE",width=20,height=2)
delete.pack(side="bottom",padx=2,anchor="n")
save = Button(window,text="SAVE",width=20,height=2)
save.pack(side=TOP,anchor="ne")

frame = Frame(window)
scroll = Scrollbar(frame,orient="vertical")
scroll.pack(side=RIGHT,fill=Y)
listbox = Listbox(frame,width=100,yscrollcommand=scroll.set,bg="light grey")
for i in range(1,51):
    listbox.insert(END,"List" + str(i))
listbox.pack(side=LEFT,pady=75)
scroll.config(command=listbox.yview)
frame.pack(side=BOTTOM,padx=125,pady=100)



window.mainloop()