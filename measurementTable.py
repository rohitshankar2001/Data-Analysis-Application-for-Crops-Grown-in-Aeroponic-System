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

    def get_reference_value(self, row_name):
        i = self.data_frame[self.data_frame['File Names']==row_name].index.values
        return self.data_frame.loc[i[0],"Reference Length"]

    def pandas_table_to_display(self, tree):
        tree.pack()
        tree.delete(*tree.get_children())
        cols = list(self.data_frame.columns)

        # Function to convert dataframe to tree view tkinter: https://stackoverflow.com/questions/57829917/how-to-display-pandas-dataframe-properly-using-tkinter
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')
        for index, row in self.data_frame.iterrows():
            tree.insert("",0,text=index,values=list(row))

        print(self.data_frame)

    def export_as_csv(self,tree):
        self.data_frame.to_csv()
