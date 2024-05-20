import tkinter as tk
from tkinter import ttk
import newFile
from tester import MyWindow
from VideoPlayer import VideoPlayer


class MyApp:
    def __init__(self, root):
        self.root = root

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 150
        window_width = 600  
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/3) - (window_height/2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
         
        self.root.title("Main Window")
        self.root.minsize(window_width, window_height)
        buttonFont = tk.font.Font(size=25)
        lowbuttonFont = tk.font.Font(size=12)
        self.filename = ''
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

        self.guiTutorial = tk.Button(botframe, text = "Watch the GUI tutorial", command= lambda: self.showTutorial("fish-spinning.mp4"), font = lowbuttonFont)
        self.deviceTutorial = tk.Button(botframe, text = "Watch the device setup tutorial", command= lambda: self.showTutorial("rat-spinning.mp4"), font = lowbuttonFont)
        self.guiTutorial.grid(column=1, row=0)
        self.deviceTutorial.grid(column=2, row=0)
        self.close_button = tk.Button(botframe,text= "Close Application", command=self.closeProgram, font = lowbuttonFont)
        self.close_button.grid(column=3, row=0)

    def closeProgram(self):
        # Close the main window
        self.show_modal_popup()
        # Create a new Toplevel window
        # Add widgets or perform other actions in the second window

    def new_file(self):
        self.root.withdraw()
        self.secondaryPane.deiconify()
        self.newFileWindow = newFile.FileWindow(self.secondaryPane, self.root)
        # if self.newFileWindow.csvName != '':
        #     self.openNewFile(newFile.FileWindow.getFileName())
       
    def openFile(self):
        self.getFile()
        if self.filename != '':
            self.root.withdraw()
            self.secondaryPane.deiconify()
            MyWindow(self.secondaryPane, self.filename)

    def showTutorial(self, identity):
        videoPane = tk.Toplevel(self.root)
        VideoPlayer(videoPane, identity)


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
