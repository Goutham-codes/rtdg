'''
File : gui.py
Function : creates a graphical user interface and
generate data based on user input.
Authors : Gouthaman,Aditya,kalaiyarasu
'''


# import statements
from tkinter import (Tk, Frame, Button, StringVar, filedialog, messagebox,
                     Label, Scrollbar, Entry)
from tkinter import ttk
import tkinter as tk
from rtdg import all_func
import csv
import json


# root widget
root = Tk()
root.title('RTDG')
root.geometry('860x720')
root.resizable(False, False)
root.configure(bg="black")


# var
rows_var = StringVar()
field_var = StringVar()
domain_var = StringVar()
subdomain_var = StringVar()
delete_var = StringVar()

filename = ""
filelabel = ""
treecount = 0


# frames
header_frame = Frame(root, width=860, height=120, bg='black')
header_frame.grid(rowspan=1, row=0)

main_frame = Frame(root, width=860, height=500, bg='black')
main_frame.grid(rowspan=3, row=1)

main_frame_1 = Frame(main_frame, width=730, height=340,
                     bd=1, relief="ridge", bg='black')
main_frame_1.grid(row=0)

main_frame_2 = Frame(main_frame, width=730, height=70, bg='black')
main_frame_2.grid(row=1)

main_frame_3 = Frame(main_frame, width=730, height=70, bg='black')
main_frame_3.grid(row=2)

bottom_frame = Frame(root, width=730, height=100, bg='black')
bottom_frame.grid(rowspan=1, row=4, padx=6)


# callback and other functions
def closeapp():
    # exit the application
    response = messagebox.askquestion("Exit Application", "Are you sure bro?")
    if response == 'yes':
        root.destroy()


def insertdata():
    # insert data into the treeview
    global treecount
    if field_entry.get() == "" or len(field_entry.get()) > 20:
        messagebox.showwarning('Invalid input', 'Check the input fields!')
        return
    if not(domain_var.get() in all_func) or domain_var.get() == "":
        messagebox.showwarning('Invalid input', 'Check the input fields!')
        return
    if subdomain_var == "":
        messagebox.showwarning('Invalid input', 'Check the input fields!')
        return
    if not subdomain_var.get() in all_func[domain_var.get()]:
        messagebox.showwarning('Invalid input', 'Check the input fields!')
        return
    domain_type = str(domain_var.get())+" - "+str(subdomain_var.get())
    tree.insert(parent='', index='end', iid=treecount, values=(
        treecount, field_entry.get(), domain_type))
    treecount += 1
    clearselection()


def deletedata():
    # delete data from treeview
    try:
        tree.delete(int(delete_entry.get()))
    except Exception:
        messagebox.showwarning("Invalid Input", "Enter a valid Id to remove!")
        pass
    delete_var.set('')


def clearselection():
    field_var.set('')
    domain_var.set('')
    subdomain_var.set('')


def clearallselection():
    field_var.set('')
    domain_var.set('')
    subdomain_var.set('')
    delete_var.set('')
    rows_var.set('')
    filelabel.destroy()
    for child in tree.get_children():
        tree.delete(child)


def choosedomain(event):
    # select a domain from the combobox1 and set values to combobox2
    subdomain_var.set('')
    domain_selected = domain_choosen.get()
    subdomain_tuple = []
    for subdomain in all_func[domain_selected]:
        subdomain_tuple.append(subdomain)
    subdomain_choosen['values'] = tuple(subdomain_tuple)


def openfile():
    # open the file and stores the name globally
    global filename
    global filelabel
    filename = filedialog.asksaveasfilename(title='select a file', filetypes=(
        ('csv files', '*.csv'), ('json files', '*.json')))
    if filelabel != "":
        filelabel.destroy()
    filelabel = Label(bottom_frame, text=filename.split(
        '/')[-1], font=('comicsans', 10), fg='white', bg='black')
    filelabel.place(relx=0.48, rely=0.3)


def checkfields():
    # checks the user entered data for errors
    try:
        x = int(rows_var.get())
    except Exception:
        messagebox.showwarning("Invalid Input", "Check the input fields!")
        return False
    if x == "" or x < 1 or x > 1000:
        messagebox.showwarning("Invalid Input", "Check the input fields!")
        return False
    if filename == "":
        messagebox.showwarning("File not selected", "Please select a file!")
        return False
    if len(tree.get_children()) == 0:
        messagebox.showwarning("Add Fields", "Please add fields to proceed!")
        return False

    return True


def getdata():
    # returns data enetered by user
    rows = int(rows_var.get())
    domains = []
    fieldnames = []
    for child in tree.get_children():
        domains.append(list(tree.item(child)["values"][-1].split(" - ")))
        fieldnames.append(tree.item(child)["values"][-2])
    return rows, domains, fieldnames


def getfileformat():
    # returns the file format
    namecheck = filename.split('/')[-1].split('.')
    if not (len(namecheck) == 2 and namecheck[0].isalnum()):
        return False
    if (namecheck[1].lower() == "csv" or namecheck[1].lower() == "json"):
        return False
    return namecheck[1].lower()


def writecsv(rows, domains, fieldnames):
    # generates and write data to csv file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        for idx in range(rows):
            data = []
            for func in domains:
                val = all_func[func[0]][func[1]]()
                data.append(val)
            writer.writerow(data)


def writejson(rows, domains, fieldnames):
    # generates and write data to json file
    with open(filename, 'w') as file:
        file.write('[')
        for i in range(rows):
            data = {}
            data['id'] = i+1
            for idx, func in enumerate(domains):
                val = all_func[func[0]][func[1]]()
                data[fieldnames[idx]] = val
            json.dump(data, file, indent=4)
            file.write(',')
        file.write(']')


def download():
    # callback function for save buttonF
    if not checkfields():
        return
    rows, domains, fieldnames = getdata()
    fformat = getfileformat()
    if fformat is False:
        return
    elif fformat == 'csv':
        writecsv(rows, domains, fieldnames)
    elif fformat == 'json':
        writejson(rows, domains, fieldnames)
    messagebox.showinfo("Info", "Data has been written successfully!")
    clearallselection()


# treeview
tree_scroll = Scrollbar(main_frame_1)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(main_frame_1, height=10, yscrollcommand=tree_scroll.set)
tree.pack(expand=tk.YES, fill=tk.BOTH)

style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview', background='silver',
                foreground='black', rowheight=35, fieldbackground='silver')
style.map('Treeview', background=[
          ('selected', 'black')], foreground=[('selected', 'white')])

tree_scroll.config(command=tree.yview)

tree['columns'] = ('Id', 'Field', 'Type')
tree.column('#0', width=0, stretch=tk.NO)
tree.column('Id', width=240, minwidth=240, anchor=tk.CENTER, stretch=False)
tree.column('Field', width=240, minwidth=240, anchor=tk.CENTER, stretch=False)
tree.column('Type', width=240, minwidth=240, anchor=tk.CENTER, stretch=False)

tree.heading('#0', text='')
tree.heading('Id', text='Id')
tree.heading('Field', text='Field')
tree.heading('Type', text='Type')


# title
Label(header_frame, text="AZGEDA RTDG", font=('comicsans', 40, 'bold'),
      fg='white', bg='black').place(relx=0.3, rely=0.3)
Button(header_frame, text='x', font=('comicsans', 10), fg='white',
       bg='red', command=closeapp, width=3).place(relx=0.89, rely=0.45)


# main frame 2 widgets
Label(main_frame_2, text='Field Name', font=('comicsans', 10),
      bg='black', fg='white').place(relx=0.02, rely=0.3)

field_entry = Entry(main_frame_2, textvariable=field_var,
                    font=('comicsans', 10))
field_entry.place(relx=0.14, rely=0.33)


# domain choices
domain_tuple = []
for domain in all_func:
    domain_tuple.append(domain)


domain_choosen = ttk.Combobox(main_frame_2, width=15, textvariable=domain_var)
domain_choosen['values'] = domain_tuple
domain_choosen.place(relx=0.38, rely=0.3)
domain_choosen.bind("<<ComboboxSelected>>", choosedomain)

subdomain_choosen = ttk.Combobox(
    main_frame_2, width=15, textvariable=subdomain_var)
subdomain_choosen['values'] = ()
subdomain_choosen.place(relx=0.56, rely=0.3)

add_field_button = Button(main_frame_2, text='Add Field', font=(
    'comicsans', 10), command=insertdata, width=15)
add_field_button.place(relx=0.8, rely=0.3)


# main frame 3 widgets
Label(main_frame_3, text='Delete Field', font=('comicsans', 10),
      bg='black', fg='white').place(relx=0.02, rely=0.3)
delete_entry = Entry(main_frame_3, textvariable=delete_var,
                     font=('comicsans', 10), width=10)
delete_entry.place(relx=0.14, rely=0.33)
delete_button = Button(main_frame_3, text='Delete', font=(
    'comicsans', 10), command=deletedata, width=15)
delete_button.place(relx=0.8, rely=0.3)


# bottom frame
Label(bottom_frame, text='Rows ', font=('comicsans', 10),
      bg='black', fg='white').place(relx=0.04, rely=0.3)
row_entry = Entry(bottom_frame, textvariable=rows_var,
                  font=('comicsans', 10), width=10)
row_entry.place(relx=0.14, rely=0.33)
rows_var.set('100')
choose_file_button = Button(bottom_frame, text='choose file', font=(
    'comicsans', 10), command=openfile)
choose_file_button.place(relx=0.36, rely=0.3)
save_button = Button(bottom_frame, text='Save to file', font=(
    'comicsans', 10), command=download, width=15)
save_button.place(relx=0.8, rely=0.3)


# main loop
root.mainloop()
