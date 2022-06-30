import json
import os
import sys
import pandas as pd
import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self,master,version,created,modified):
        self.version = version
        self.create_date = created
        self.mod_date = modified

        self.master = master
        self.master.geometry("610x290")
        self.master.title("Task Engine")

        self.current_task = tk.StringVar()
        self.get_tasks()
        
        self.task_frame()
        self.taskFR.grid(column=0,row=0,padx=2,pady=2,sticky='W')
        
    def task_frame(self):
        # Create elements
        self.taskFR = tk.LabelFrame(self.master,
                                    text="Tasks")
        self.task = ttk.Combobox(self.taskFR,
                                 textvariable=self.current_task)
        self.task['values'] = list(self.DF["Name"])
        self.task.bind('<<ComboboxSelected>>',self.task_changed)

        # Place elements
        self.task.grid(column=0,row=0,padx=2,pady=2,sticky='W')
        
    def task_changed(self,event=None):
        print(self.current_task.get())

    def get_tasks(self):
        self.DF = pd.read_csv("Tasks.csv")
        
        
if __name__ == '__main__':
    __version__ = "0.1.0"
    date_created = "30-June-2022"
    last_modified = "30-June-2022"
    root = tk.Tk()
    app = GUI(root,__version__,date_created,last_modified)
    root.mainloop()
    root.destroy()
