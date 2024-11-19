import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import ctypes
import json
from tkcalendar import Calendar
from datetime import date
from .base2format import txt_to_csv
from .tester import MyWindow


class FileWindow:
    def __init__(self, master, opening, callback) -> None:
        self.root = master
        self.opening = opening
        self.callback = callback

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 600  
        window_height = 450
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/3) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.minsize(window_width, window_height)

        self.csvName = ''
        self.root.title("New File")
        self.filename = ''
        self.root.config(background = "white") 
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        self.browseFiles()
        self.riderTypeSelect()
        self.riderNames()
        self.riderWeight()
        self.styleSelect()
        self.dateSelect()
        self.finishInput()
        self.root.mainloop()
            

    def showRiderOptions(self):

        selection = self.riderType.get()

        for widget in self.nameFrame.winfo_children():
            widget.destroy()

        if selection == "Exist":
            self.riderNames()
            
        else:
            self.newName()

    def browseFiles(self) -> None:
        self.topFrame = ttk.Frame(self.root)
        self.nameFrame = ttk.Frame(self.root)
        self.bottomFrame = ttk.Frame(self.root)
        topFrame = ttk.Frame(self.topFrame)
        openFiles = ttk.Button(topFrame, text="Open File Explorer", command=self.getFile)
        self.filenameLabel = tk.Label(topFrame, text="Filename: ")
        openFiles.grid(columnspan= 2, rowspan=1, column=0, row=0)
        self.filenameLabel.grid(column=0, row= 1, columnspan=2)
        topFrame.pack()
        self.topFrame.pack()
        self.nameFrame.pack()
        self.bottomFrame.pack()
    
    def riderTypeSelect(self) -> None:
        riderSelectFrame = ttk.Frame(self.topFrame)
        self.riderType = tk.StringVar(value= "Exist")
        existingRiderButton = ttk.Radiobutton(riderSelectFrame, text= "Existing Rider", value= "Exist", variable= self.riderType, command= self.showRiderOptions)
        newRiderButton = ttk.Radiobutton(riderSelectFrame, text= "New Rider", value = "New", variable= self.riderType, command= self.showRiderOptions)
        existingRiderButton.grid(column=0, row=1)
        newRiderButton.grid(column=1, row=1)
        riderSelectFrame.pack()

    
    def getFile(self) -> None:
        self.filename = filedialog.askopenfilename(initialdir = "D:/", title = "Select a File", filetypes = (("Text files",
                                                            "*.txt*"), ("all files","*.*")))
        if self.filename != '': 
            self.finishButton.config(state= "active")
            self.filenameLabel.config(text= "Filename: " + self.filename)
   
    def riderNames(self) -> None:
        nameFrame = ttk.Frame(self.nameFrame)
        with open(Path(__file__).parent / 'rider_info.json', 'r') as file:
            self.data = json.load(file)
        names = self.data["names"]
        self.nameCombobox = ttk.Combobox(nameFrame, values= names, state= "readonly")
        self.nameCombobox.set("Select Rider Name")
        self.nameCombobox.bind("<<ComboboxSelected>>", self.updateWeightEntry)
        nameLabel = ttk.Label(nameFrame, text= "Rider Name")
        nameLabel.grid(column=0, row=0)
        self.nameCombobox.grid(column=1, row=0)
        nameFrame.pack()
        
    def updateWeightEntry(self, event):
        if self.nameCombobox.get() != ('' or "Select Rider Name"):
            self.entry_var.set(str(self.data[self.nameCombobox.get()]["weight"]))

    def riderWeight(self) -> None:
        weightFrame = ttk.Frame(self.bottomFrame)
        self.entry_var = tk.StringVar()
        self.weightEntry = ttk.Entry(weightFrame, textvariable=self.entry_var)
        weightLabel = ttk.Label(weightFrame, text= "Rider Weight")
        weightLabel.grid(column=0, row=0)
        self.weightEntry.grid(column=1, row=0)
        weightFrame.pack()

    def styleSelect(self) -> None:
        styleFrame = ttk.Frame(self.bottomFrame)
        self.styleSelected = tk.StringVar()
        engRadio = ttk.Radiobutton(styleFrame, text= "English", value= 'E', variable= self.styleSelected)
        westRadio = ttk.Radiobutton(styleFrame, text= "Western", value= 'W', variable= self.styleSelected)
        engRadio.grid(row=0)
        westRadio.grid(row=0, column=1)
        styleFrame.pack()
        
    def newName(self) -> None:
        nameFrame = ttk.Frame(self.nameFrame)
        self.nameEntry = ttk.Entry(nameFrame)
        nameLabel = ttk.Label(nameFrame, text= "Rider Name:")
        nameLabel.grid(column=0, row=0)
        self.nameEntry.grid(column=1, row=0)
        nameFrame.pack()

    def dateSelect(self) -> None:
        dateFrame = ttk.Frame(self.bottomFrame)
        self.month = ttk.Combobox(dateFrame, values= ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], state= "readonly")
        self.day = ttk.Combobox(dateFrame, values= list(range(1, 32)), state= "readonly")
        seperator = tk.Label(dateFrame, text= " - ")
        self.month.set("Month")
        self.day.set("Day")
        self.month.grid(row=0, column=0)
        self.day.grid(row=0,column=2)
        seperator.grid(row=0,column=1)

        # self.cal = Calendar(dateFrame, selectmode='day', year=date.today().year, month=date.today().month, day=date.today().day)
        # self.cal.pack()
        #print(self.selectedDate)
        dateFrame.pack()

    def finishInput(self) -> None:
        self.finishButton = ttk.Button(self.root, text="Process Data", command= self.finishCommand)
        if self.filename == '': self.finishButton.config(state= "disabled")
        self.finishButton.pack()

    def finishCommand(self) -> None:
        weight = self.weightEntry.get()
        style = self.styleSelected.get()

        date = self.month.get() + self.day.get() + "-24"
        # date = self.cal.get_date()
        # date = date.replace("/", "")
        #print(date[2:])
        # if len(date) == 4:
        #     date = '0' + date[:1] + '0' + date[1:]
        # elif len(date) == 5 and (date[:2] == '10' or date[:2] == '11' or date[:2] == '12'): # or '11' or '12'):
        #     date = date[:2] + '0' + date[2:]
        # else:
        #     date = '0' + date
        if self.riderType.get() == "Exist":
            name = self.nameCombobox.get()
            #print([name, weight, style, date])

            if self.data[name]["weight"] != weight:
                self.data[name]["weight"] = weight
            self.data[name]["date"].append(date)
            self.data[name]["style"].append(style)

        elif self.riderType.get() == "New":
            name = self.nameEntry.get()
            self.data["names"].append(name)
            self.data["names"].sort()
            self.data[name] = {}
            self.data[name]["weight"] = weight
            self.data[name]["date"] = [date]
            self.data[name]["style"] = [style]
            self.data[name]["session"] = [os.path.splitext(os.path.basename(self.filename))[0]]

        #print(self.data)
        jsonData = json.dumps(self.data, indent=4)
        with open(Path(__file__).parent / 'rider_info.json', "w") as outfile:
            outfile.write(jsonData)

        if not os.path.exists(Path(__file__).parent.parent.parent / 'Data Files'):
            os.makedirs(Path(__file__).parent.parent.parent / 'Data Files')
        csvName = (name + "_" + date + "_" + style + ".csv")
        self.csvName = Path(__file__).parent.parent.parent / 'Data Files' / csvName
        #os.makedirs(self.csvName)
        txt_to_csv(self.filename, self.csvName)
        # self.opening.deiconify()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.callback(self.csvName)
        #MyWindow(self.root, self.csvName)
        
    # def getFileName(self):
    #     return self.csvName

    # def run(self):
    #     self.root.mainloop()
    #     return(self.csvName)

if __name__ == "__main__":
    app = FileWindow(tk.Tk(), tk.Tk())
