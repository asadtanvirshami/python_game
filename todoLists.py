#importing tkinter package for the GUI
from  tkinter import * 
import tkinter.messagebox

#setting up the window
window=Tk()

#title of the window
window.title("Python App Todo List")

#Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()

#to hold items in a listbox
listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetcia")
listbox_task.pack(side = tkinter.LEFT) 

#Scrolldown in case the total list exceeds the size of the given window 
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side = tkinter.RIGHT, fill = tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

#Enter Button Widget
entry_button = Button(window, text="Add Task", width=50)
entry_button.pack(pady=3)

#Delete Button Widget
delete_button = Button(window, text="Delete Task", width=50)
delete_button.pack(pady=3)

#Complete Button Widget
mark_button=Button(window,text="Mark as completed ",width=50,)
mark_button.pack(pady=3)

window.mainloop()

def enterTask():
    task = ""
    def add():
        task = task_entry.get(1.0, "end-1c")
        if task == "":
            tkinter.messagebox.showwarning(title="Warning", message="Please enter the task")
        else:
            listbox_task.insert(END,task)
            root1.destroy()
    root1 = Tk()
    root1.title("Add Task")
    task_entry = Text(root1, width=40, height=4)
    task_entry.pack()
    button_temp=Button(root1,text="Add task",command=add)
    button_temp.pack()