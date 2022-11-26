import math
from tkinter import Tk
from tkinter import *


class pointPlacer:
    def __init__(self,root, canvas, column_name):
        self.canvas = canvas
        self.__root = root
        self.column_name = column_name
        self.num_clicks = 0

    def draw(self):
        # Drawing function from: https://www.tutorialspoint.com/how-to-draw-a-line-following-mouse-coordinates-with-tkinter
        def draw_line(e):
            x, y = e.x, e.y
            self.num_clicks += 1
            if self.canvas.old_coords:
                x1, y1 = self.canvas.old_coords
                self.canvas.create_line(x, y, x1, y1, width=5, tag = "line" + self.column_name)
            self.canvas.old_coords = x, y
            if self.num_clicks > 1:
                self.__root.unbind('<ButtonPress-1>')
                self.canvas.old_coords = None
        self.__root.bind('<ButtonPress-1>', draw_line)

    def clear(self):
        self.canvas.delete("line" + self.column_name)

    def calculate_distnace(self, x1 , y1 , x2 , y2):
        first_coordinate = [x1,y1]
        second_coordinate = [x2,y2]
        return math.dist(first_coordinate,second_coordinate)


