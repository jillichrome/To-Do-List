#!/usr/bin/python

import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.configure(bg = "grey")
root.title("To Do List")
root.geometry("250x300")

tasks = {}

def update_listbox():
    clear_list()
    task_lst = []
    for key in tasks:
    	task_lst.append(key)
    	listbox.insert("end", key)

def clear_list():
    listbox.delete(0, "end")

def add_task():
    task = entry.get()
    deadline = entry_d.get()
    if task == "" or deadline == "":
    	messagebox.showwarning("Attention!", "You must enter a task and a deadline.")
    if task != "" and deadline != "":
    	tasks.update({task:deadline})
    entry.delete(0, "end")
    entry_d.delete(0, "end")
    update_listbox()


def show_deadline():
    task = listbox.get("active")
    deadline = tasks.get(task)
    lb_display["text"] = deadline


def update_deadline():
	task = listbox.get("active")
	new_deadline = entry_d.get()
	tasks[task] = new_deadline
	entry_d.delete(0, "end")


def delete_task():
    task = listbox.get("active")
    if task in tasks: del tasks[task]
    update_listbox()

def delete_all():
    confirmed = messagebox.askyesno("Please confirm", "Are you sure you want to delete all?")
    if confirmed == True:
	    global tasks
	    tasks = {}
	    update_listbox()

lb_task = tkinter.Label(root, text = "Task", bg = "grey", fg = "white")
lb_date = tkinter.Label(root, text = "Deadline", bg = "grey", fg = "white")
lb_display = tkinter.Label(root, text = "", bg = "grey", fg = "white")
entry = tkinter.Entry(root, width = 20, bd = 5)
entry_d = tkinter.Entry(root, width = 20, bd = 5)
b_add = tkinter.Button(root, text = "Add Task", command = add_task)
b_delete = tkinter.Button(root, text = "Delete Task", command = delete_task)
b_deleteall = tkinter.Button(root, text = "Delete All", command = delete_all)
b_deadline = tkinter.Button(root, text = "Show Deadline", command = show_deadline)
b_update = tkinter.Button(root, text = "Update Deadline", command = update_deadline)
b_exit = tkinter.Button(root, text = "Exit", bg = "red", command = root.quit)
listbox = tkinter.Listbox(root)

lb_task.grid(row = 0, column = 0)
lb_date.grid(row = 1, column = 0)
entry_d.grid(row= 1, column = 1)
entry.grid(row = 0, column = 1)
lb_display.grid(row = 2, column = 0, columnspan = 2)
b_add.grid(row = 3, column = 0)
b_delete.grid(row = 4, column = 0)
b_deleteall.grid(row = 5, column = 0)
b_deadline.grid(row = 6, column = 0)
b_update.grid(row = 7, column = 0)
b_exit.grid(row = 8, column = 0)
listbox.grid(row = 3, column = 1, rowspan = 7)
root.mainloop()