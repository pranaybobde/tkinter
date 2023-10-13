from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymongo
from pymongo import MongoClient
from upload_page import *

cli=pymongo.MongoClient("mongodb://localhost:27017/")
print(cli)
db=cli['Tkinter']
mycol=db['Data Entry']

root = Tk()

root.title("Data Entry Form")
root.geometry("640x480")
# root.minsize(640,480)
# root.maxsize(640,480)
root.grid_propagate(0)




def exit_program():
    root.destroy()

def enter():
    
    acccepted = accept_var.get()
    if acccepted == "Accepted":
    
        first_name = first_name_entry.get()
        middle_name = middle_name_entry.get()
        last_name = last_name_entry.get()
        if first_name and last_name and middle_name:
            
            age = age_spinbox.get()
            if age.isdigit():
                
                title = title_combo_box.get()
                if title in title_dict:            
    
                    Nationality = nationality_combobox.get()
                    if Nationality in nationality_dict:
                        
                        company_name = company_name_entry.get()
                        Designation = designation_entry.get()
                        
                        
                        check = messagebox.askyesno(message = "Are you sure you want to submit")
                        if check:
                            print("First Name:",first_name)
                            print("Middle Name:",middle_name)
                            print("Last Name:",last_name)
                            print("Age:",age)
                            print("Title:",title)
                            print("Nationality:",Nationality)
                            print("Comapany Name:",company_name)
                            print("Designation",Designation)
                            print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                            mydict={'First_Name':first_name, 'Middle_Name':middle_name, 'Last_Name':last_name,'Age':age,'Title':title, 'Nationality':Nationality,'Company_Name':company_name, 'Designation':Designation}
                            mycol.insert_one(mydict) 
                            messagebox.showinfo(title = "Done", message = "Details are recorded sucessfully")
                            upload_img()
                    else:
                        messagebox.showwarning(title = "Error", message = "Please select nationality from the combobox")
                else:
                    messagebox.showwarning(title = "Error", message = "Please select title from the combobox")
            else:
                messagebox.showerror(title = "Error", message = "Please select your age through spinbox")
        else:
            messagebox.showwarning(title ="Error", message = "First, Middle and Last Name are mandatory")
    else:
        messagebox.showwarning(title = "Error", message = " Please accept the Terms and Conditions")
        
def reset():
    first_name_entry.delete(0, END)
    middle_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    age_spinbox.delete(0, END)
    title_combo_box.current(0)
    nationality_combobox.current(0)
    company_name_entry.delete(0, END)
    designation_entry.delete(0, END)
    terms_checkbutton.deselect()
        
        
        
title_dict = ["Mr.", "Mrs.", "Ms.", "Don't want to specific"]    
nationality_dict =["Asia", "Europe", "South America", "Africa", "Antarctica", "North America", "Australia"]



    
frame = Frame(root)
frame.pack()

# User Information
user_info_frame = LabelFrame(frame, text = " User Information")
user_info_frame.grid(row = 0, column = 0, padx = 20, pady = 10)

first_name_label = Label(user_info_frame, text = "First Name")
first_name_label.grid(row = 0, column = 0)

first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)

middle_name_label = Label(user_info_frame, text = "Middle Name")
middle_name_label.grid(row = 0, column = 1)

middle_name_entry = Entry(user_info_frame)
middle_name_entry.grid(row = 1, column = 1)

last_name_label = Label(user_info_frame, text = "Last Name")
last_name_label.grid(row = 0, column = 2, padx = 10)

last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row = 1, column = 2)

age_label = Label(user_info_frame, text = "Age")
age_label.grid(row = 2, column = 0)

age_spinbox = Spinbox(user_info_frame, from_= 16, to = "infinity")
age_spinbox.grid(row = 3, column = 0)

title_label = Label(user_info_frame, text = "Title")
title_label.grid(row = 2, column = 1)

title_combo_box = ttk.Combobox(user_info_frame, values = title_dict)
title_combo_box.grid(row = 3 , column = 1)

nationality_label = Label(user_info_frame, text = " Nationality")
nationality_label.grid(row = 2, column = 2)


nationality_combobox = ttk.Combobox(user_info_frame, values = nationality_dict)
nationality_combobox.grid(row = 3 , column = 2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# Compayny Information
comapany_info_frame = LabelFrame(frame, text = "Company Information")
comapany_info_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)

company_name_label = Label(comapany_info_frame, text = "Company Name")
company_name_label.grid(row = 0, column = 0)

company_name_entry = Entry(comapany_info_frame)
company_name_entry.grid(row = 1, column = 0)

designation_label = Label(comapany_info_frame, text = "Designation")
designation_label.grid(row = 0, column = 1)

designation_entry = Entry(comapany_info_frame)
designation_entry.grid(row = 1, column = 1)

for widget in comapany_info_frame.winfo_children():
    widget.grid_configure(padx = 15, pady = 5)
    
reset_button = Button(comapany_info_frame, text = "Reset", fg = "blue", borderwidth = 4, relief  = RAISED, command = reset)
reset_button.grid(row = 1, column = 2, padx = 50)

# Terms & Conditions
terms_frame = LabelFrame(frame, text = "Terms and Conditions")
terms_frame.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)

accept_var = StringVar(value = "Not Accepted")

terms_checkbutton = Checkbutton(terms_frame, text = "I accept all the Terms and Conditions", onvalue = "Accepted", offvalue = "Not Accepted", variable = accept_var) 
terms_checkbutton.grid(row = 0, column = 0)

# Enter button
enter_button = Button(frame, text = "Enter", fg = "green", font = "Arial 15 bold", borderwidth = 4, relief  = RAISED, command = enter)
enter_button.grid(row = 4, column = 0, sticky = "news", padx = 20, pady = 20)

exit_button = Button(frame, text = "Exit", fg = "red", font = "Arial 15 bold", borderwidth = 4, relief  = RAISED, command = exit_program)
exit_button.grid(row = 5, column = 0, sticky = "news", padx = 20) 

root.mainloop()