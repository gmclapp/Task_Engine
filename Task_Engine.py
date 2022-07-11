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
        self.current_task_proj = tk.StringVar()
        self.current_task_resource = tk.StringVar()
        
        self.get_tasks()
        self.get_projects()
        self.get_resources()
        
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

        self.taskProject = ttk.Combobox(self.taskFR,
                                        textvariable=self.current_task_proj)
        self.taskProject['values'] = list(self.projDF["Name"])
        self.taskProject.bind('<<ComboboxSelected>>',self.taskProj_changed)

        self.taskResource = ttk.Combobox(self.taskFR,
                                         textvariable=self.current_task_resource)
        self.taskResource['values'] = list(self.resourceDF["Name"])
        self.taskResource.bind('<<ComboboxSelected>>',self.taskResource_changed)

        self.applyPB = ttk.Button(self.taskFR,
                                  command=self.apply_changes,
                                  text="Apply")

        # Place elements
        self.task.grid(column=0,row=0,padx=2,pady=2,sticky='W')
        self.taskProject.grid(column=1,row=0,padx=2,pady=2,sticky='W')
        self.taskResource.grid(column=2,row=0,padx=2,pady=2,sticky='W')
        self.applyPB.grid(column=3,row=0,padx=2,pady=2,sticky='W')
        
    def task_changed(self,event=None):
        self.DFcurrent = self.DF.loc[self.DF["Name"] == self.current_task.get()]
        self.refresh_fields()
        
        print(self.DFcurrent.head())
        
    def taskProj_changed(self,event=None):
        self.DFcurrent["Project"] = self.current_task_proj.get()

    def taskResource_changed(self,event=None):
        self.DFcurrent["Resource"] = self.current_task_resource.get()
        
    def get_tasks(self):
        self.DF = pd.read_csv("Tasks.csv")
        
    def get_projects(self):
        self.projDF = pd.read_csv("Projects.csv")

    def get_resources(self):
        self.resourceDF = pd.read_csv("Resources.csv")

    def refresh_fields(self):
        self.current_task_proj.set(self.DFcurrent["Project"])
        
        self.task.configure()
        self.taskProject.configure()

    def apply_changes(self):
##        self.DF.set_index("Serial number")
##        self.DFcurrent.set_index("Serial number")
        
        self.DF.update(self.DFcurrent)
        self.DF.to_csv("Tasks.csv")
##        self.DF.reset_index()
##        self.DFcurrent.reset_index()
        
        print(self.DF.head())
        
if __name__ == '__main__':
    __version__ = "0.1.0"
    date_created = "30-June-2022"
    last_modified = "30-June-2022"
    root = tk.Tk()
    app = GUI(root,__version__,date_created,last_modified)
    root.mainloop()
    root.destroy()
