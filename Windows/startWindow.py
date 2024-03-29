from tkinter import *
from tkinter import filedialog, scrolledtext
import os
from tkinter.ttk import Treeview

from Components.measurementTable import measurementTable
from Windows.imageAnalysisWindow import imageAnalysisWindow


class StartWindow:
    root = Tk()
    measure_table = measurementTable()
    tree = Treeview(root)

    def __init__(self, window_name="DefaultName"):
        self.__window_name = window_name
        self.__imported_images_table = scrolledtext.ScrolledText()

        self.root.title(self.__window_name)
        self.root.geometry("800x600+0+0")
        self.root.update()
        self.__image_names = []

        self.__build_menu_bar_gui()
        self.__build_labels_gui()
        self.__build_image_table_gui()
        self.root.mainloop()

    def __build_menu_bar_gui(self):
        menu_bar = Menu(self.root, tearoff=False)
        file_menu = Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="File", menu=file_menu)

        import_images_command = lambda: self.__import_images()
        file_menu.add_command(label="Import Image Folder", command=import_images_command)

        export_csv_command = lambda : measurementTable.export_as_csv(self.measure_table)
        file_menu.add_command(label="Save/Export as csv", command=export_csv_command)

        import_csv_command = lambda : measurementTable.import_as_csv(self.measure_table,"output.csv",self.tree)
        file_menu.add_command(label="Load/Import as csv", command=import_csv_command)

        self.root.config(menu=menu_bar)

    @staticmethod
    def __open_analysis_window(file_button, directory):
        i = imageAnalysisWindow(file_button['text'], directory)

    def __import_images(self):
        image_folder = filedialog.askdirectory()
        if image_folder != '':
            for image in os.listdir(image_folder):
                if image not in self.__image_names:
                    self.__image_names.append(image)
                    file_button = Button(text=image, width=15, height=2)
                    file_button.config(command=lambda file_button=file_button: self.__open_analysis_window(file_button, image_folder))
                    self.__imported_images_table.window_create("end", window=file_button)
                    self.__imported_images_table.insert("end", "\n")
            self.__build_length_table_gui(self.tree)

    def __build_image_table_gui(self):
        self.__imported_images_table = scrolledtext.ScrolledText(self.root, width=15, height=self.root.winfo_height())
        self.__imported_images_table.grid_propagate(True)
        self.__imported_images_table.configure(state="disabled")
        self.__imported_images_table.pack(side="left", pady=65, padx=10)

    def __build_labels_gui(self):
        Label(self.root, text="Imported Images").place(x=25, y=20)
        Label(self.root, text="File -> Import Images -> Select FOLDER which contains images").place(relx=0.5, rely=0.75, anchor="s")

    def __build_length_table_gui(self, tree):
        print(self.__image_names)

        self.measure_table.add_images(self.__image_names)
        self.measure_table.add_column("Reference Length")
        self.measure_table.pandas_table_to_display(tree)


