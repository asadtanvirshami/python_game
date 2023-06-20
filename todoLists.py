import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

# Function to remove a task
def remove_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("No Task Selected", "Please select a task to remove.")

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a listbox to display tasks
listbox = tk.Listbox(window, width=50, height=10)
listbox.pack(pady=10)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Connect the listbox with the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create an entry field to add tasks
entry = tk.Entry(window, width=50)
entry.pack(pady=5)

# Create buttons to add and remove tasks
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Run the main window loop
window.mainloop()