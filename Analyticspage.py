import tkinter as tk

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DatabaseHelper import *

class Analytics:
    def __init__(self):
        self.temp_root = tk.Toplevel()
        self.add_bar_graph("Train Number")
        #self.add_line_graph("Total passengers")

    def get_total_no_of_passengers(self):
        query = """ 
        Select TRAIN_ID, No_of_passengers 
        from railway.Passenger
        order by TRAIN_ID
        """
        result = DatabaseHelper.get_all_data(query)

        df1 = DataFrame(result[1:], columns=result[0]).groupby("TRAIN_ID").sum()
        return df1

    def get_train_name(self):
        query = """ Select TrainId, IsConfirmed
                    from railway.Ticket
                    order by TrainId
                """
        result = DatabaseHelper.get_all_data(query)

        df = DataFrame(result[1:], columns=result[0]).groupby("TrainId").sum()
        return df

    def add_bar_graph(self, title):
        df1 = self.get_total_no_of_passengers()

        figure1 = plt.Figure(figsize=(7, 5), dpi=100)
        ax1 = figure1.subplots()

        bar1 = FigureCanvasTkAgg(figure1, self.temp_root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1.plot(kind='bar', legend=True, ax=ax1, fontsize=10)
        ax1.set_title(title)
    #
    # def add_line_graph(self, title):
    #     df2 = self.get_train_name()
    #
    #     figure2 = plt.Figure(figsize=(7, 4), dpi=100)
    #     ax2 = figure2.subplots()
    #
    #     line2 = FigureCanvasTkAgg(figure2, self.temp_root)
    #     line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #     df2.plot(kind='line', legend=True, ax=ax2, color='red', marker='o', fontsize=10)
    #     ax2.set_title(title)
