import math
import string
import random

from tkinter import Tk
from tkinter import *
from Windows import startWindow


class pointPlacer:
    def __init__(self,root, canvas, column_name, window_name, is_scaled):
        self.canvas = canvas
        self.__root = root
        self.column_name = column_name
        self.window_name = window_name
        self.num_clicks = 0
        self.is_scaled = is_scaled

    def draw(self):
        # Drawing function from: https://www.tutorialspoint.com/how-to-draw-a-line-following-mouse-coordinates-with-tkinter
        def draw_line(e):
            x, y = e.x, e.y
            self.num_clicks += 1
            if self.canvas.old_coords:
                x1, y1 = self.canvas.old_coords
                line = self.canvas.create_line(x, y, x1, y1, width=5, tag=self.column_name.replace(" ", ""))
            self.canvas.old_coords = x, y
            if self.num_clicks > 1:
                if self.column_name == "Reference Length":
                    self.add_to_measurement_table(self.calculate_distance(x, y, x1, y1))
                elif self.is_scaled:
                    reference_scale = startWindow.StartWindow.measure_table.get_reference_value(self.window_name)
                    if reference_scale is None:
                        reference_scale = 1
                    self.add_to_measurement_table(self.calculate_distance(x, y, x1, y1)/reference_scale)
                else:
                    self.add_to_measurement_table(self.calculate_distance(x, y, x1, y1))
                startWindow.StartWindow.measure_table.pandas_table_to_display(startWindow.StartWindow.tree)
                self.__root.unbind('<ButtonPress-1>')
                self.canvas.old_coords = None
        self.__root.bind('<ButtonPress-1>', draw_line)

    def clear(self):
        self.canvas.delete(self.column_name.replace(" ", ""))

    def calculate_distance(self, x1 , y1 , x2 , y2):
        first_coordinate = [x1,y1]
        second_coordinate = [x2,y2]
        return math.dist(first_coordinate,second_coordinate)

    def add_to_measurement_table(self, value):
        startWindow.StartWindow.measure_table.add_row_value(self.window_name, self.column_name, value)


