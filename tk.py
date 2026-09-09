import tkinter as tk

root = tk.Tk()

root.title("Login")

label = tk.Label(root,text="name :")
label.grid(row=0,column=0)

tk.Entry(root).grid(row=0,column=1)


label = tk.Label(root,text="email :")
label.grid(row=1,column=0)

tk.Entry(root).grid(row=1,column=1)


root.mainloop()
