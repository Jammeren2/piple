from tkinter import Tk, Canvas, ARC, SE, W
from grid import Grid
from human import Human

root = Tk()
canvas = Canvas (root,width=800,height=600)
canvas.pack()

grid = Grid(canvas)
grid.display()

p1 = Human(canvas, 200, 450, 'БОБА')
p1.display()

p2 = Human(canvas, 0, 450, 'БИБА')
p2.display()


p3 = Human(canvas, 400, 450, 'ДВА')
p3.display()

p4 = Human(canvas, 600, 450, 'ДРУГА')
p4.display()




root.mainloop()
