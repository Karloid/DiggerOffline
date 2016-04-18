from tkinter import *  # Importing the Tkinter (tool box) library


class Game:
    def __init__(self):
        self.master = Tk()

        self.CELL_SIZE = 16
        self.WIDTH = self.CELL_SIZE * 60
        self.HEIGHT = self.CELL_SIZE * 30
        self.userX = 15
        self.userY = 15
        self.w = Canvas(self.master, width=self.WIDTH, height=self.HEIGHT)

    def on_click(self, event):
        x = event.x
        y = event.y
        print("mouse click: " + str(x) + " " + str(y))
        self.w.create_rectangle(x, y, x + 10, y + 10, fill="#689F38")

    def on_key_press(self, key):
        print("key " + key.char)

    def draw(self):
        self.i = 10
        self.w.delete("all")
        x = self.userX * self.CELL_SIZE
        y = self.userY * self.CELL_SIZE
        self.w.create_rectangle(x, y, x + self.CELL_SIZE, y + self.CELL_SIZE, fill="#689F38")

    def update(self):
        self.userX = self.userX + 1

    def doLoop(self):
        self.update()
        self.draw()
        self.master.after(int(1000 / 15), self.doLoop)

    def go(self):
        self.master.wm_title("Копатель офлаен")

        self.w.pack()

        self.w.bind_all("<Key>", self.on_key_press)
        self.w.bind("<Button-1>", self.on_click)

        self.doLoop()
        self.master.mainloop()


game = Game()
game.go()
