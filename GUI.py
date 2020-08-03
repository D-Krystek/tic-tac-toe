import tkinter as tk
from TicTacToe import board 
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = str(board[0][0])
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="left")

        #self.quit = tk.Button(self, text="QUIT", fg="red",
        #                      command=self.master.destroy)
        #self.quit.pack(side="bottom")

        self.hi_there2 = tk.Button(self)
        self.hi_there2["text"] = "-"
        self.hi_there2["command"] = self.say_hi
        self.hi_there2.pack(side="left")

    def say_hi(self):
        #print("hi there, everyone!")
        print(board)
        if(self.hi_there["text"] != 'X'):
            self.hi_there["text"] = 'X'
        else:
            print("You've already played here...")

root = tk.Tk()
app = Application(master=root)
app.mainloop()