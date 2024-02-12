from tkinter import *
root=Tk()
##creating text box

textbox=Text(root,width=40,height=13,wrap=WORD)
textbox.grid(row=0,column=0)

##scrollbar

scroll=Scrollbar(root,orient=VERTICAL,command=textbox.yview)
scroll.grid(row=0,column=1,sticky=N+S)
textbox.configure(yscrollcommand=scroll.set)

root.geometry("200x300")
root.title("scroll bar ")
root.mainloop()

## menu

from tkinter import *
root=Tk()
root.title("menu example")
root.geometry("400x400")

##create  main  menu in root
menu_bar=Menu(root)
root.config(menu=menu_bar)##here menubar is set as menu of root window

#create file menu

file_menu=Menu(menu_bar)
menu_bar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label='new')
file_menu.add_command(label="open")
file_menu.add_command(label="exit",command=root.destroy)

#create editmenu

edit_menu=Menu(menu_bar)
menu_bar.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_command(label="cut")
edit_menu.add_command(label="copy")
edit_menu.add_command(label="paste")

root.mainloop()


##listbox

import tkinter as tk
root=tk.Tk()
root.title("list box")

##createw list box

list_box=tk.Listbox(root,selectmode=tk.SINGLE)
list_box.pack()
items=["fruits","veg","diary","grocery"]
for item in items:
    list_box.insert(tk.END,item)
root.mainloop()