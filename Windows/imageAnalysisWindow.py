from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


class imageAnalysisWindow:
    window_name = ""
    directory = ""

    def __init__(self, window_name="FILE_NAME", directory=""):
        __root = Tk()

        self.window_name = window_name
        self.directory = directory

        __root.title(window_name)
        __root.geometry("600x600")
        canvas = Canvas(__root, width=1200, height =1200)

        #Gives scrollbar to canvas. Made for larger images. Directly from stackoverflow post: https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
        frame=Frame(__root,width=300,height=300)
        frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
        canvas=Canvas(frame,bg='#FFFFFF',width=1200,height=1200,scrollregion=(0,0,5000,5000))
        hbar=Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=canvas.xview)
        vbar=Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)

        # Opens Image
        image_dir = self.directory + "/" + self.window_name
        print(image_dir)
        canvas.config(width=1200,height=1200)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack()
        image = ImageTk.PhotoImage(Image.open(image_dir), master=canvas)
        canvas.create_image(50, 50, anchor=NW, image=image)
        # End of Image

        __root.mainloop()






