import math
from tkinter import Tk
from tkinter import *
from PIL import Image
import threading

class areaPlacer:

    def __init__(self, root, canvas, column_name, window_name, is_scaled, image):
        self.canvas = canvas
        self.__root = root
        self.column_name = column_name
        self.window_name = window_name
        self.is_scaled = is_scaled
        self.image = image

    def get_color_of_pixel(self, pixel_x, pixel_y):
        self.image.convert('RGB')
        r, g, b = self.image.getpixel((pixel_x, pixel_y))
        return [r, g, b]

    def compare_colors(self, color1, color2, offset):
        if math.sqrt(math.pow(color1[0] - color2[0], 2) + math.pow(color1[1] - color2[1], 2) + math.pow(color1[2] - color2[2], 2)) < offset:
            return True
        return False

    def compare_pixels_around_to_color(self, pixel_x, pixel_y, compare_color, offset):
        pixels = []
        colors = []

        pixel_top_left = [pixel_x - 1, pixel_y + 1]
        #pixels.append(pixel_top_left)
        #colors.append(self.get_color_of_pixel(pixel_top_left[0], pixel_top_left[1]))

        pixel_top = [pixel_x, pixel_y + 1]
        pixels.append(pixel_top)
        colors.append(self.get_color_of_pixel(pixel_top[0], pixel_top[1]))

        pixel_top_right = [pixel_x + 1, pixel_y + 1]
        #pixels.append(pixel_top_right)
        #colors.append(self.get_color_of_pixel(pixel_top_right[0], pixel_top_right[1]))

        pixel_right = [pixel_x + 1, pixel_y]
        pixels.append(pixel_right)
        colors.append(self.get_color_of_pixel(pixel_right[0], pixel_right[1]))

        pixel_left = [pixel_x - 1, pixel_y]
        pixels.append(pixel_left)
        colors.append(self.get_color_of_pixel(pixel_left[0], pixel_left[1]))

        pixel_bottom_left = [pixel_x - 1, pixel_y - 1]
        #pixels.append(pixel_bottom_left)
        #colors.append(self.get_color_of_pixel(pixel_bottom_left[0], pixel_bottom_left[1]))

        pixel_bottom = [pixel_x, pixel_y - 1]
        pixels.append(pixel_bottom)
        colors.append(self.get_color_of_pixel(pixel_bottom[0], pixel_bottom[1]))

        pixel_bottom_right = [pixel_x + 1, pixel_y - 1]
        #pixels.append(pixel_bottom_right)
        #colors.append(self.get_color_of_pixel(pixel_bottom_right[0], pixel_bottom_right[1]))

        similar_pixels = []
        for pixel_colors, pixel_location in zip(colors,pixels):
            if self.compare_colors(compare_color, pixel_colors, offset):
                #self.canvas.create_rectangle(pixel_location[0], pixel_location[1], pixel_location[0], pixel_location[1], fill="RED", outline="RED")
                similar_pixels.append([pixel_location[0], pixel_location[1]])
        return similar_pixels

    def compare_pixels_around_selection(self, pixel_x,pixel_y):
        area_pixels = []
        area_pixels += self.compare_pixels_around_to_color(pixel_x,pixel_y,self.get_color_of_pixel(pixel_x,pixel_y), 30)
        print(area_pixels)
        for pixels in area_pixels:
            self.canvas.create_rectangle(pixels[0], pixels[1], pixels[0], pixels[1], fill="RED", outline="RED")
            print(area_pixels)
            for new_vals in self.compare_pixels_around_to_color(pixels[0], pixels[1], self.get_color_of_pixel(pixel_x, pixel_y), 30):
                if new_vals not in area_pixels:
                    area_pixels.append(new_vals)
        # for pixels in area_pixels:
        #     self.canvas.create_rectangle(pixels[0], pixels[1], pixels[0], pixels[1], fill="RED", outline="RED")

    def compare_pixel_thread(self,pixel_x,pixel_y):
        t1 = threading.Thread(target=self.compare_pixels_around_selection, args=[pixel_x, pixel_y])
        t1.start()

    def mouse_selection(self):
        def select_point(e):
            x = self.canvas.canvasx(e.x)
            y = self.canvas.canvasy(e.y)
            self.compare_pixel_thread(x, y)
        self.__root.bind('<ButtonPress-3>', select_point)

