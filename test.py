from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.TEXT1 = Button(self)
        self.TEXT1["text"] = "QUIT"
        self.TEXT1["fg"] = "red"
        self.TEXT1["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
var = Text
l = Label(root, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
l.pack()
app = Application(master=root)
app.mainloop()
root.destroy()