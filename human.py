from tkinter import Tk, Canvas, ARC, SE, W

class Human() :
    def __init__ (self, canvas):
        self.canvas = canvas
        
    def display(self):
        self.__drawHead()
        self.__drawBody()
        self.__TEXT()
        
    def __drawHead(self) :
        self.canvas.create_oval(20, 400, 80, 460, width=2)
        self.canvas.create_arc(30, 420, 70, 450, start=0, extent=-180, style=ARC, outline="red", width=3)
        self.canvas.create_oval(35, 421, 43, 429, width=0, fill="blue")
        self.canvas.create_oval(65, 420, 57, 428, width=0, fill="blue")
    def __drawBody(self) :
        self.canvas.create_line(50, 460, 50, 550, width=2)
        
        self.canvas.create_line(100, 600, 50, 550, width=2)
        self.canvas.create_line(0, 600, 50, 550, width=2) 
        
        self.canvas.create_line(100, 520, 50, 480, width=2)
        self.canvas.create_line(0, 520, 50, 480, width=2)

    def __TEXT(self) : 
        self.canvas.create_text(50, 370, 
              text="Боба",
              justify=CENTER, font="Verdana 14")
