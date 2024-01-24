import tkinter as tk
from tkinter import messagebox

def on_entry_click(event):
    if entry.get() == "Enter your task here":
        entry.delete(0, "end")
        entry.insert(0, '')
        entry.config(fg='black')

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, "Enter your task here")
        entry.config(fg='grey')

def add_task():
    task = entry.get()
    if task and task != "Enter your task here":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        entry.insert(0, "Enter your task here")
        entry.config(fg='grey')
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    listbox.delete(0, tk.END)

# Create the main window with Soft Mint Green background color
root = tk.Tk()
root.title("MY TASK")
root.configure(bg="#C4FFC4")  # Soft Mint Green color

# Create and configure the task entry widget with Light Gray background and black border
entry = tk.Entry(root, width=80, fg='grey', bd=2, relief=tk.SOLID, bg="#F0F0F0")  # Light Gray color
entry.insert(0, "Enter your task here")
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(pady=70)

# Create and configure the add button with Sky Blue color
add_button = tk.Button(root, text="Update Task", command=add_task, bg="#87CEEB")  # Sky Blue color
add_button.pack(side=tk.LEFT, padx=10)

# Create and configure the remove button with Light Coral color
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#F08080")  # Light Coral color
remove_button.pack(side=tk.LEFT, padx=10)

# Create and configure the clear button with Light Salmon background color
clear_button = tk.Button(root, text="Clear All", command=clear_tasks, bg="#FFA07A")  # Light Salmon color
clear_button.pack(side=tk.LEFT, padx=5, pady=10)

# Create and configure the to-do list (listbox) with Soft Mint Green background color and black border
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=80, height=20, bg="#C4FFC4", bd=2, relief=tk.SOLID)  # Soft Mint Green color
listbox.pack(pady=20)

# Start the main event loop
root.mainloop()
