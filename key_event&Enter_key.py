# import tkinter as tk

# app = tk.Tk()
# app.geometry("200x100")

# def callback(event):
#     # label["text"] = "You pressed Enter"
#     print("pressed Enter ")

# app.bind('<Return>', callback)

# label = tk.Label(app, text="")
# label.pack()

# app.mainloop()


# import tkinter as tk

# class app(tk.Frame):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("300x200")
#         self.label = tk.Label(self.root, text="")
#         self.label.pack()
#         self.root.bind('<Return>', self.callback)
#         self.root.mainloop()


#     def callback(self, event):
#         self.label["text"] = "You pressed {}".format(event.keysym)
    
# app()




from tkinter import *
def keyup(e):
    print ('up', e.char)
def keydown(e):
    print('down', e.char)

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()