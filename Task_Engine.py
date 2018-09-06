'''This script allows a burn-down style of task management.'''

__version__ = "0.0.rc6"

import json
import os
import sys
import time
import sanitize_inputs as si

##class Tee(object):
##    '''This  class is used to send duplicate messages to a log file.'''
##    def __init__(self, *files):
##        self.files = files
##    def write(self, obj):
##        for f in self.files:
##            f.write(obj)
##            #f.flush()#if you want the output to be visible immediately
##    def flush(self):
##        for f in self.files:
##            f.flush()

class taskobj():
    def __init__(self, serial_number=None, name=None, program_number = None,
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

        for key, value in self.Attributes.items():
            print(key, ":", value)
        
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
        '''This method saves the task object to a json file. It appends
        the serial number of the task to the file name.'''
        temp = str(self.Attributes["Serial number"])
        filename = "task" + temp + ".TE"
        
        with open(filename, 'w') as f:
            json.dump(self.Attributes, f)
        
    def load_task(self, sn):
        '''This method loads an Attribute dictionary into a task object
        given a filename.'''
        filename = "task" + str(sn)
        with open(filename, 'r') as f:
            self.Attributes = json.load(f)
                      
    def archive_task(self):
        pass

def load_config():
    pass
    #Create config file if it does not exist
    #Notify user if config file is corrupted. They can chose to overwrite it.

def load_tasks(working_directory):
    '''This function checks the working directory for existing tasks and
    loads them into task_list[]. If there are no existing tasks, it creates
    an empty list. In both cases, this function returns task_list[].'''
    tasks = []
    # check the working directory for task files.
    for files in os.listdir(working_directory):
        print(files)
    
    return(tasks)

with open("Task_Engine.log", 'a') as log:
    # This opens the log file in append mode. opening in this way ensures that if an
    # unexpected closure happens, the log is presserved.
##    original = sys.stdout
    # This line preserves the ability to print to stdout without logging.
##    sys.stdout = Tee(sys.stdout, log)
    # This line overwrites sys.stdout with both the original stdout and the log object
    # so that the default print command will print to both.
    
    load_config()
    working_directory = 'C:\\Users\\gmclapp\\Desktop\\Task engine\\Task_Engine'
   
    task_list = load_tasks(working_directory) #This needs to load all existing tasks.
    
    while(True):
        print("With a timestamp!",time.strftime("%d%B%Y, %H:%M:%S UTC",time.gmtime()))
        print("What would you like to do?",
              "(0) Quit",
              "(1) New task",
              "(2) Edit existing task",sep = '\n')
        key = si.get_integer(">>>",3,-1)
        if key == 1:
            max_sn = 0
            for task in task_list:
                if task.Attributes["Serial number"] > max_sn:
                    max_sn = task.Attributes["Serial number"]
                else:
                    pass
            new_sn = max_sn + 1
            print("New task")
            task_name = input("Enter task name\n>>>")
            
            ans = si.get_letter("Is this task associated with a program?\n>>>",
                                ['y','Y','n','N'])
            if ans.lower() == 'y':
                prog_num = input("Enter program number\n>>>")
            elif ans.lower() == 'n':
                prog_num = None
            new_task = taskobj(new_sn, task_name, prog_num)
            task_list.append(new_task)
            task_list[-1].tprint()
                       
        elif key == 2:
            pass
        elif key == 0:
            break
        else:
            print("Invalid entry")

