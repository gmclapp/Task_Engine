import json
import os
import sys
import time
import sanitize_inputs as si

version = "0.0.4"

class Tee(object):
    '''This  class is used to send duplicate messages to a log file.'''
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            #f.flush()#if you want the output to be visible immediately
    def flush(self):
        for f in self.files:
            f.flush()

class taskobj():
    def __init__(self, serial_number, name, program_number = None,
                 date_assigned = "Unknown",date_due = "TBD",
                 time_assigned = 0, time_due = 1700, hours_to_complete = 40,
                 description = None, notes = None, task_type = None,
                 assigned_by = None, turn_in_to = None, status = "Active",
                 children_complete = False, complete = False, date_completed = None,
                 customer_facing = False, top_5_task = False, customer_request = False, severity = 0, priority = 0):

        self.Attributes = {
            "Serial number": serial_number,
            "Name": name,
            "Program number": program_number,
            "Date assigned": date_assigned,
            "Date_due": date_due,
            "Time assigned": time_assigned,
            "Time due": time_due,
            "Hours to complete": hours_to_complete,
            "Description": description,
            "Notes": notes,
            "Task type": task_type,
            "Assigned by": assigned_by,
            "Turn in to": turn_in_to,
            "Status": status,
            "Children": [],
            "Children complete": children_complete,
            "Complete": complete,
            "Parents": {},
            "Date completed": date_completed,
            "Customer facing": customer_facing,
            "Top 5": top_5_task,
            "Customer request": customer_request,
            "Severity": severity,
            "Priority": priority
            }

    def tprint(self):
        '''This method prints a task and it's attributes to the console
        as well as to the log file.'''
        
        print("Serial number:",self.Attributes["Serial number"])
        print("Name:", self.Attributes["Name"])
        print("Program number:", self.Attributes["Program number"])
        
    def calc_priority(self):
        pass
    def add_child(self, child):
        pass
    def add_parent(self, parent):
        pass
    def delete_child(self, child):
        pass
    def delete_parent(self, parent):
        pass
    def save_task(self):
        pass
    def load_task(self):
        pass
    def archive_task(self):
        pass

def load_config():
    print("Version", version)
    #Create config file if it does not exist
    #Notify user if config file is corrupted. They can chose to overwrite it.

with open("Task_Engine.log", 'a') as log:
    #This opens the log file in append mode. opening in this way ensures that if an unexpected closure happens, the log is presserved.
    original = sys.stdout
    #This line preserves the ability to print to stdout without logging.
    sys.stdout = Tee(sys.stdout, log)
    #This line overwrites sys.stdout with both the original stdout and the log object so that the default print command will print to both.
    load_config()

    task_list = [] #This needs to load all existing tasks.
    
    while(True):
        print("With a timestamp!",time.strftime("%d%B%Y, %H:%M:%S UTC",time.gmtime()))
        print("What would you like to do?",
              "(0) Quit",
              "(1) New task",
              "(2) Edit existing task",sep = '\n')
        key = input(">>>")
        if key == '1':
            max_sn = 0
            for task in task_list:
                if task.Attributes["Serial number"] > max_sn:
                    max_sn = task.Attributes["Serial number"]
                else:
                    pass
            new_sn = max_sn + 1
            print("New task")
            task_name = input("Enter task name\n>>>")
            print("Is this task associated with a program?")
            ans = input("(y/n)>>>")
            if ans == 'y' or ans == 'Y':
                prog_num = input("Enter program number\n>>>")
            elif ans == 'n' or ans == 'N':
                prog_num = None
            new_task = taskobj(new_sn, task_name, prog_num)
            task_list.append(new_task)
            task_list[-1].tprint()
                       
        elif key == '2':
            pass
        elif key == '0':
            break
        else:
            print("Invalid entry")

