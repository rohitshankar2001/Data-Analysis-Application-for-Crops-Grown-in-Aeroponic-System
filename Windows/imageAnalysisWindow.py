from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import *
from PIL import ImageTk, Image

from Windows import startWindow
from tkinter import messagebox
from Components.pointPlacer import pointPlacer
from Components.areaPlacer import areaPlacer

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

        # Gives scrollbar to canvas. Made for larger images. From stackoverflow post: https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
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
        canvas.config(width=1250, height=750)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack()
        #image = ImageTk.PhotoImage(Image.open(image_dir), master=canvas)
        image = Image.open(image_dir)
        self.resized_image = image.resize((750, 750), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(self.resized_image, master=canvas)
        canvas.create_image(0, 0, anchor=NW, image=new_image)
        # End of Image
        canvas.old_coords = None

        self.__add_column_buttons(__root, canvas)
        self.build_menu_bar_gui(__root, canvas)
        __root.mainloop()

    def create_new_length_column(self, __root, canvas):
        new_column_name = simpledialog.askstring(title="NEW COLUMN", prompt="Enter Name of Length Column",parent=__root)
        if new_column_name is not None:
            new_column_name = new_column_name + " Length"
            startWindow.StartWindow.measure_table.add_column(new_column_name)
            startWindow.StartWindow.measure_table.pandas_table_to_display(startWindow.StartWindow.tree)
            self.__add_column_buttons(__root, canvas)

    def create_new_area_column(self, __root, canvas):
        new_column_name = simpledialog.askstring(title="NEW COLUMN", prompt="Enter Name of Area Column",parent=__root)
        if new_column_name is not None:
            new_column_name = new_column_name + " Area"
            startWindow.StartWindow.measure_table.add_column(new_column_name)
            startWindow.StartWindow.measure_table.pandas_table_to_display(startWindow.StartWindow.tree)
            self.__add_column_buttons(__root, canvas)

    def __add_column_buttons(self, __root,canvas):
        columns = startWindow.StartWindow.measure_table.data_frame.columns
        for i in range(1, len(columns)):
            column_button = Button(canvas, text=columns[i], width=40)
            if columns[i][-6:] == "Length":
                column_button.config(command=lambda column_button=column_button: self.__place_measurement_points(__root,canvas,column_button["text"]))
            elif columns[i][-4:] == "Area":
                column_button.config(command=lambda column_button=column_button: self.__place_area_points(__root,canvas,column_button["text"]))

            column_button.place(x=800, y=30 * i)

    def __place_measurement_points(self, __root, canvas, column_name):
        is_scaled = True
        if column_name == "Reference Length":
            messagebox.showinfo("Make Measurement", "Right Click at ends of measurement", parent=__root)
        else:
            is_scaled = messagebox.askyesno("Question", "Do you want value scaled with reference", parent=__root)
            print(is_scaled)

        for b in canvas.winfo_children():
            b.configure(state="disabled")

        pp = pointPlacer(__root, canvas, column_name, self.window_name, is_scaled)
        pp.clear()
        pp.draw()

    def __place_area_points(self, __root, canvas, column_name):
        ap = areaPlacer(__root,canvas,column_name,self.window_name, False, self.resized_image)
        #print(ap.get_color_of_pixel(0,0))
        #print(ap.compare_colors([7,4,3],[17,6,2],30))
        #print(ap.compare_pixels_around_selection(20,30))
        ap.mouse_selection()

    def build_menu_bar_gui(self, __root,canvas):
        menu_bar = Menu(__root, tearoff=False)
        file_menu = Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="File", menu=file_menu)

        import_buttons_length = lambda: self.create_new_length_column(__root, canvas)
        file_menu.add_command(label="Create New Length Column", command=import_buttons_length)

        import_buttons_area = lambda: self.create_new_area_column(__root, canvas)
        file_menu.add_command(label="Create New Area Column", command=import_buttons_area)
        __root.config(menu=menu_bar)






