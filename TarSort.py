from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from datetime import datetime
from tkinter import ttk


def choose_dir():
    d_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, d_path)


def start_sort():
    c_path = e_path.get()
    if c_path:
        for folder, subfolsers, files in os.walk(c_path):
            for file in files:
                path = os.path.join(folder, file)
#                print(path)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime("%Y-%m-%d")
                date_folder = os.path.join(c_path, date)
                print(date_folder)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo('Sorted ', 'TarSort sorted Successfuly')
        e_path.delete(O, END)
    else:
        messagebox.showarning('Warning', ' Please Choose right folder')


root = Tk()
root.title('TarSort 0.0.1')
root.geometry('500x150')

s = ttk.Style()

s.configure('my.TButton', font=('Helvetica', 15))

frame = Frame(root, bg="#56ADFF", bd=5)
frame.pack(pady=10, padx=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text='Choose Folder', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(
    root, text='Sort', style='my.TButton', command=start_sort)
btn_start.pack(fill=X, padx=10)


root.mainloop()
