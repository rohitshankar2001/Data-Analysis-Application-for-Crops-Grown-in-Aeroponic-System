import math
from tkinter import *
from tkinter import simpledialog, scrolledtext
from tkinter.ttk import *
from PIL import ImageTk, Image

from Windows import startWindow
from tkinter import messagebox
from pointPlacer import pointPlacer

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
        __root.geometry("%dx%d" % (1200,600))

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
        canvas.config(width=1250,height=750)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack()
        #image = ImageTk.PhotoImage(Image.open(image_dir), master=canvas)
        image = Image.open(image_dir)
        resized_image = image.resize((750,750), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image,master=canvas)
        canvas.create_image(0, 0, anchor=NW, image=new_image)
        # End of Image
        canvas.old_coords = None

        self.__add_column_buttons(__root,canvas)
        #self.get_mouse_coordinates(canvas)
        self.__build_menu_bar_gui(__root,canvas)
        self.add_reference(__root)
        __root.mainloop()

    def create_new_column(self, __root,canvas):
        new_column_name = simpledialog.askstring(title="NEW COLUMN", prompt="Enter Name of Column",parent=__root)
        startWindow.StartWindow.measure_table.add_column(new_column_name)
        startWindow.StartWindow.measure_table.pandas_table_to_display()
        self.__add_column_buttons(__root,canvas)

    def __place_measurement_points(self, __root, canvas, column_name):
        messagebox.showinfo("Make Measurement", "Click at ends of measurement", parent=__root)
        pp = pointPlacer(__root, canvas, column_name,self.window_name)
        pp.clear()
        pp.draw()

    def __add_column_buttons(self, __root,canvas):
        columns = startWindow.StartWindow.measure_table.data_frame.columns
        for i in range(1, len(columns)):
            column_button = Button(canvas, text=columns[i], width=40)
            column_button.config(command=lambda column_button=column_button: self.__place_measurement_points(__root,canvas,column_button["text"]))
            column_button.place(x=800, y=30 * i)

    def __build_menu_bar_gui(self, __root,canvas):
        menu_bar = Menu(__root, tearoff=False)
        file_menu = Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="File", menu=file_menu)
        import_buttons = lambda: self.create_new_column(__root,canvas)

        file_menu.add_command(label="Create New Column", command=import_buttons)

        __root.config(menu=menu_bar)








