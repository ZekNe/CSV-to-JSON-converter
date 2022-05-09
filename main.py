from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

# Tkinter main window
top = Tk()
top.geometry('1200x600')
top.title("CSV to JSON converter")

# Covertor
def Convert():
    test = csv_text.get("1.0", "end")
    json_text.insert(INSERT, "[\n")
    column_name = ""
    row = []
    
    row = test.split("\n")
    column_name = row[0].split(",")
    row_number = len(row)
    column_number = len(column_name)
    r = 1

    if csv_text.get("2.0") == "":
        messagebox.showerror("Error", "Empty")
        json_text.delete("1.0", END)
        return

    while r <= row_number - 2:

        json_text.insert(INSERT, " {\n")
        i = column_number
        column = row[r].split(",")
        n = 0

        while i > 0:

            try:
                json_text.insert(INSERT, "  ")
                json_text.insert(INSERT, '"')
                json_text.insert(INSERT, column_name[n])
                json_text.insert(INSERT, '"')
                json_text.insert(INSERT, ":")
                json_text.insert(INSERT, '"')
                json_text.insert(INSERT, column[n])
                json_text.insert(INSERT, '"')
                json_text.insert(INSERT, ",\n")

            except IndexError as e:
                messagebox.showerror("Error", "Invalid")
                json_text.delete("1.0", END)
                return

            i -= 1
            n += 1

        r += 1
        json_text.delete("end-1c")
        json_text.delete("end-2c")
        json_text.insert(INSERT, "\n },\n")

    json_text.delete("end-3c")
    json_text.insert(INSERT, "]")

    if json_text.get("end-2c") != "]":
        messagebox.showinfo("Error", "Invalid format!")
        json_text.delete("1.0", END)

# Clear JSON
def ClearJSON():
    json_text.delete("1.0", END)

# Clear CSV
def ClearCSV():
    csv_text.delete("1.0", END)

# Import CSV
def ImportCSV():
    apex = Toplevel(top)
    apex.geometry("300x150")
    apex.title("Import CSV")
    apex.grid_rowconfigure((0,1,2), weight=1)
    apex.grid_columnconfigure(0, weight=1)

    def SubmitAdress():
        csv_file = EA1.get()
        g = open(csv_file, "r").read()
        csv_text.insert(INSERT, g)
        apex.destroy()

    LA1 = Label(apex, text="Enter File Adress", font=("Times New Roman", 15))
    LA1.grid(row = 0, sticky = "s")
    EA1 = Entry(apex, bd = 2)
    EA1.grid(row = 1, ipadx = 50 ,ipady = 3)
    BA1 = Button(apex, text="Submit", command = SubmitAdress, font=("Times New Roman", 15))
    BA1.grid(row = 2, sticky = "n")

# Export JSON
def ExportJSON():
    with open('test.json', 'w') as f:
        f.write(json_text.get("1.0", END))

# grid
top.grid_rowconfigure(0, weight=1)
top.grid_rowconfigure(1, weight=15)
top.grid_rowconfigure(2, weight=5)
top.grid_columnconfigure(0, weight=5)
top.grid_columnconfigure(1, weight=1)
top.grid_columnconfigure(2, weight=5)

# Labels
L1 = Label(top, text="CSV", font=("Times New Roman", 20))
L1.grid(row = 0, column = 0, sticky='n', pady=15)
L2 = Label(top, text="JSON", font=("Times New Roman", 20))
L2.grid(row = 0, column = 2, sticky='n', pady=15)

# TextBox
csv_text = scrolledtext.ScrolledText(top, wrap=NONE, width=50, height=20, font=("Times New Roman", 15), border=2)
csv_text.grid(row = 1, column = 0, sticky='n', padx = 15)
json_text = scrolledtext.ScrolledText(top, wrap=NONE, width=50, height=20, font=("Times New Roman", 15), border=2)
json_text.grid(row = 1, column = 2, sticky='n', padx = 15)

# Buttons
B1 = Button(top, text="Clear CSV", command = ClearCSV, font=("Times New Roman", 20),height=1,width=10)
B1.grid(row = 2, column = 0, sticky='w', padx = 15)
B2 = Button(top, text="Convert", command = Convert, font=("Times New Roman", 20),height=1,width=10)
B2.grid(row = 2, column = 1)
B3 = Button(top, text="Clear JSON", command = ClearJSON, font=("Times New Roman", 20),height=1,width=10)
B3.grid(row = 2, column = 2, sticky='e', padx = 15)
B4 = Button(top, text="Import CSV", command = ImportCSV, font=("Times New Roman", 20),height=1,width=10)
B4.grid(row = 2, column = 0, padx = 15)
B5 = Button(top, text="Export JSON", command = ExportJSON, font=("Times New Roman", 20),height=1,width=10)
B5.grid(row = 2, column = 2, padx = 15)

top.mainloop()