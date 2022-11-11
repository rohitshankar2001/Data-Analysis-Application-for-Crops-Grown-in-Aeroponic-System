
from tkinter import *
from tkinter.ttk import *


class imageAnalysisWindow:

    def __init__(self, window_name="FILE_NAME"):

        #self.__root.title(window_name)
        #self.__root.geometry("800x600")
        #self.__root.update()

        __root = Tk()
        __root.withdraw()

        newWindow = Toplevel(__root)
        newWindow.title("New Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        Label(newWindow, text ="This is a new window").pack()


