import tkinter as tk
from tkinter import filedialog

root = tk.Tk(className="合并EXCEL")
root.geometry('600x400')


def get_file_name():
    # root.withdraw()
    file_path = filedialog.askopenfilename()
    t.insert('insert', file_path)


def get_file_name2():
    # root.withdraw()
    file_path = filedialog.askopenfilename()
    t2.insert('insert', file_path)


b = tk.Button(root, text='数据源文件', width=10, height=2, command=get_file_name)
b.pack()


t = tk.Text(root, height=3)
t.pack()


b2 = tk.Button(root, text='整理到', width=10, height=2, command=get_file_name2)
b2.pack()

t2 = tk.Text(root, height=3)
t2.pack()


root.mainloop()
