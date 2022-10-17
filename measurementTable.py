from tkinter.ttk import Treeview

import pandas as pd
from tkinter import *


class measurementTable:
    data_frame = pd.DataFrame()

    def __init__(self, file_names: list):
        self.file_names = file_names
        self.data_frame.insert(0,"File Names", file_names)

    def add_column(self, column_name):
        self.data_frame[column_name] = ''

    def pandas_table_to_display(self):
        print(self.data_frame)
