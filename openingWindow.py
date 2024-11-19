import tkinter as tk
from tkinter import ttk
from . import newFile
from .tester import MyWindow
from os import startfile
import webbrowser
import urllib.parse



class MyApp:
    def __init__(self, root):
        self.root = root

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 200
        window_width = 800  
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/3) - (window_height/2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
         
        self.root.title("Main Window")
        self.root.minsize(window_width, window_height)
        buttonFont = tk.font.Font(size=25)
        lowbuttonFont = tk.font.Font(size=12)
        self.filename = None
        self.secondaryPane = tk.Toplevel()
        self.secondaryPane.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", self.show_modal_popup)
        self.secondaryPane.protocol("WM_DELETE_WINDOW", self.closedWindow)

        # Create a button to open the second window
        topframe = tk.Frame(root)
        topframe.pack(expand = True)
        botframe = tk.Frame(root)
        botframe.pack()
        self.open_button = tk.Button(topframe, text="Open File", command=self.openFile, font = buttonFont)
        self.open_button.grid(column=1, row=0)

        self.new_button = tk.Button(topframe, text= "New File", command= self.new_file, font= buttonFont)
        self.new_button.grid(column=2, row=0)

        #self.guiTutorial = tk.Button(botframe, text = "Watch the GUI tutorial", font = lowbuttonFont) #, command= lambda: self.showTutorial("C:/Capstone Code/WindowCode/Soil Pre-Lab.pdf"))
        #self.deviceTutorial = tk.Button(botframe, text = "Watch the device setup tutorial", font = lowbuttonFont)#, command= lambda: self.showTutorial("C:/Capstone Code/WindowCode/SetupTutorial.mp4")
        #self.useTutorial = tk.Button(botframe, text = "Watch the device use tutorial", font = lowbuttonFont)#, command= lambda: self.showTutorial("C:/Capstone Code/WindowCode/UseTutorial.mp4"), 
        #self.guiTutorial.grid(column=1, row=0)
        #self.deviceTutorial.grid(column=2, row=0)
        #self.useTutorial.grid(column=3, row=0)
        self.openTutorials = tk.Button(botframe, text = "Open Tutorials in Google Drive", font = lowbuttonFont, command = lambda: webbrowser.open('https://drive.google.com/drive/folders/1Py9WgIonaDRoLzOLRUtEgT8R2gFH7dVK?usp=sharing'))
        self.openTutorials.grid(column=1, row=0, columnspan=3)
        self.close_button = tk.Button(botframe,text= "Close Application", command=self.closeProgram, font = lowbuttonFont)
        self.close_button.grid(column=4, row=0)

    def openURL(self):
        url = 'https://drive.google.com/drive/folders/1Py9WgIonaDRoLzOLRUtEgT8R2gFH7dVK?'
        params = {'usp': 'sharing'}
        print(url + urllib.parse.urlencode(params))

    def closeProgram(self):
        # Close the main window
        self.show_modal_popup()
        # Create a new Toplevel window
        # Add widgets or perform other actions in the second window

    def new_file(self):
        self.root.withdraw()
        self.secondaryPane.deiconify()
        newFile.FileWindow(self.secondaryPane, self.root, self.newFileCall)
        
       
    def newFileCall(self, filename):
        if filename != None:
            MyWindow(self.secondaryPane, filename)

    def openFile(self):
        self.getFile()
        if self.filename != '':
            self.root.withdraw()
            self.secondaryPane.deiconify()
            MyWindow(self.secondaryPane, self.filename)


    def showTutorial(self, identity):
        startfile(identity)


    # def openNewFile(self, file):
    #     self.root.withdraw()
    #     self.secondaryPane.deiconify()
    #     MyWindow(self.secondaryPane, file)

    def getFile(self) -> None:
        self.filename = tk.filedialog.askopenfilename(initialdir = "/Capstone Code/DataFiles", title = "Select a File", filetypes = (("Text files",
                                                            "*.csv*"), ("all files","*.*")))
    def show_modal_popup(self):
    # Create a new top-level window (modal dialog)
        if tk.messagebox.askokcancel("Quit", "Do you want to close the program?"):
            self.root.destroy()


    def closedWindow(self):
        if tk.messagebox.askokcancel("Quit", "Do you want to go back to the home screen?"):
            self.secondaryPane.withdraw()
            for widget in self.secondaryPane.winfo_children():
                widget.destroy()
            self.root.deiconify()



if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
