from tkinter import *
from tkinter import filedialog, scrolledtext
import os


class StartWindow:
    __root = Tk()

    def __init__(self, window_name="DefaultName"):
        self.__window_name = window_name
        self.__imported_images_table = scrolledtext.ScrolledText()

        self.__root.title(self.__window_name)
        self.__root.geometry("800x600")
        self.__root.update()

        self.__build_menu_bar_gui()
        self.__build_labels_gui()
        self.__build_image_table_gui()
        self.__root.mainloop()

    def __build_menu_bar_gui(self):
        menu_bar = Menu(self.__root, tearoff=False)
        file_menu = Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="File", menu=file_menu)

        import_images_command = lambda: self.__import_images()
        file_menu.add_command(label="Import Image Folder", command=import_images_command)

        self.__root.config(menu=menu_bar)

    def __import_images(self):
        image_folder = filedialog.askdirectory()
        for image in os.listdir(image_folder):
            b = Button(text=image, width=15, height=2)
            self.__imported_images_table.window_create("end", window=b)
            self.__imported_images_table.insert("end", "\n")

    def __build_image_table_gui(self):
        self.__imported_images_table = scrolledtext.ScrolledText(self.__root, width=15,
                                                                 height=self.__root.winfo_height())
        self.__imported_images_table.grid_propagate(True)
        self.__imported_images_table.configure(state="disabled")
        self.__imported_images_table.pack(side="left", pady=65, padx=10)

    # def __build_length_table_gui(self):
    def __build_labels_gui(self):
        Label(self.__root, text="Imported Images").place(x=25, y=20)
        Label(self.__root, text="File -> Import Images -> Select FOLDER which contains images").place(relx=0.5, rely=0.5, anchor="center")
    def get_window_name(self):
        return self.__window_name

    def set_window_name(self, new_window_name):
        self.__window_name = new_window_name
