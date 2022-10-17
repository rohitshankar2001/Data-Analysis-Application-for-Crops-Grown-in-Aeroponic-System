import pandas as pd
from tkinter import *


class measurementTable:
    data_frame = pd.DataFrame()

    def __init__(self, table_rows, table_columns):
        self.table_rows = table_rows;
        self.table_columns = table_columns;

    def add_column(self, column_name):
        self.data_frame[column_name] = ''

    def __pandas_table_to_display(self):
        for i in range(0, 1):
            print("Display in table")
