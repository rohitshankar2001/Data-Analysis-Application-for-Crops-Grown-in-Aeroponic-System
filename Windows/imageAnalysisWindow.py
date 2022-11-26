from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import *
from PIL import ImageTk, Image

from Windows import startWindow


class imageAnalysisWindow:
    window_name = ""
    directory = ""

    def __init__(self, window_name="FILE_NAME", directory=""):
        __root = Toplevel()

        self.window_name = window_name
        self.directory = directory

        __root.title(window_name)
        width = __root.winfo_screenwidth()
        height = __root.winfo_screenheight()
        __root.geometry("%dx%d" % (width - 100, height - 100))

        # Gives scrollbar to canvas. Made for larger images. Directly from stackoverflow post: https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
        frame = Frame(__root,width=300,height=300)
        frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
        canvas = Canvas(frame,bg='#FFFFFF',width=1500,height=1500,scrollregion=(0,0,5000,5000))
        hbar = Scrollbar(frame,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=canvas.xview)
        vbar = Scrollbar(frame,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        # End of Scrollbar

        # Opens Image
        image_dir = self.directory + "/" + self.window_name
        print(image_dir)
        canvas.config(width=1200,height=1200)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack()
        image = ImageTk.PhotoImage(Image.open(image_dir), master=canvas)
        # image = Image.open(image_dir)
        # resized_image = image.resize((1200,1200), Image.ANTIALIAS)
        # new_image= ImageTk.PhotoImage(image,master=canvas)
        canvas.create_image(0, 0, anchor=NW, image=image)
        # End of Image

        self.get_mouse_coordinates(canvas)
        self.__build_menu_bar_gui(__root)
        __root.mainloop()

    def create_new_column(self, __root):
        new_column_name = simpledialog.askstring(title="NEW COLUMN", prompt="Enter Name of Column",parent=__root)
        startWindow.StartWindow.measure_table.add_column(new_column_name)
        startWindow.StartWindow.measure_table.pandas_table_to_display()

    def __build_menu_bar_gui(self, __root):
        menu_bar = Menu(__root, tearoff=False)
        file_menu = Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="File", menu=file_menu)
        import_images_command = lambda: self.create_new_column(__root)

        file_menu.add_command(label="Create New Column", command=import_images_command)
        file_menu.add_command(label="Add to existing Column", command=import_images_command)

        __root.config(menu=menu_bar)

    def get_mouse_coordinates(self, canvas):
        def callback(e):
            abs_coord_x = canvas.canvasx(e.x)
            abs_coord_y = canvas.canvasx(e.y)
            print(str(abs_coord_x) + " " + str(abs_coord_y))
        canvas.bind('<Button 1>', callback)








