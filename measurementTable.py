from tkinter.ttk import Treeview

import pandas as pd
from tkinter import *


class measurementTable:
    data_frame = pd.DataFrame()

    def __init__(self):
        print("init")

    def add_images(self, file_names: list):
        self.data_frame.insert(0,"File Names", file_names)

    def add_column(self, column_name):
        self.data_frame[column_name] = ''

    def add_row_value(self, row_name, column_name, value):
        i = self.data_frame[self.data_frame['File Names']==row_name].index.values
        self.data_frame._set_value(i[0], column_name, value)

    def pandas_table_to_display(self):
        print(self.data_frame)
