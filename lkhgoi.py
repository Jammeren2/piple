from tkinter import Tk, Canvas, ARC, SE, W
from grid import Grid
from human import Human

root = Tk()
canvas = Canvas (root,width=800,height=600)
canvas.pack()

grid = Grid(canvas)
grid.display()

sda = Human(canvas)
sda.display()
root.mainloop()
root.mainloop ()
