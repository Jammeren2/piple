from tkinter import Tk, Canvas, ARC, SE, W
from grid import Grid
from human import Human

root = Tk()
canvas = Canvas (root,width=800,height=600)
canvas.pack()

grid = Grid(canvas)
grid.display()

p1 = Human(canvas)
p1.display()

root.mainloop()









'''
canvas.create_line( 100, 110, 100,300,)#туловище

canvas.create_line( 150, 450, 100,300,)# ножки
canvas.create_line( 50, 450, 100,300,)


canvas.create_line( 100, 150, 200,200,)# ручки
canvas.create_line( 100, 150, 0,200,)

canvas.create_oval(50, 10, 150, 110, width=2)
'''





root.mainloop ()