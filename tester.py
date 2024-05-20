import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from customStats import horseStats
import csv
from newGraphFile import NewFileWindow
from existGraphFile import ExistFileWindow


#import newFile
#from openingWindow import openFile

##def mainWindow():
class MyWindow:
    def __init__(self, master, filename) -> None:
        self.dataX, self.dataY = self.initialData(filename)
        self.root = master
        self.root.title(filename)
        self.graphArea = ttk.Frame(self.root)
        self.legendArea = ttk.Frame(self.root)
        self.zoomArea = ttk.Frame(self.root)
        self.statArea = ttk.Frame(self.root)
        self.configure_root()
        self.setup_areas()
        self.setup_menus()
        self.setup_plot()
        self.changePlot()
        self.setup_checkboxes()
        self.setup_stats()
        self.root.protocol("WM_DELETE_WINDOW", plt.close(self.fig))
        self.root.mainloop()
        

    def configure_root(self) -> None:
        self.root.state('zoomed')
        self.root.minsize(1100, 700)

    def setup_areas(self) -> None:
        # Area setups
        for i in range(10):
            self.root.rowconfigure(i, weight=1)

        for i in range(8):
            self.root.columnconfigure(i, weight=1)

        self.graphArea.grid(column=0, row=0, columnspan=7, rowspan=10, sticky=tk.NSEW)
        self.legendArea.grid(column=7, row=1, rowspan=3, columnspan= 1,sticky=tk.NSEW)
        self.zoomArea.grid(column=7, row=0, rowspan= 1, columnspan= 1, sticky=tk.NSEW)
        self.statArea.grid(column=7, row=4, rowspan=6, columnspan= 1, sticky=tk.NSEW)

        self.graphArea.config(relief='groove')
        self.legendArea.config(relief='sunken')
        self.zoomArea.config(relief='sunken')
        self.statArea.config(relief='sunken')

    def setup_menus(self) -> None:

        # Menu Setups
        self.root.option_add('*tearOff', False)
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file = tk.Menu(self.menubar)
        #self.edit = tk.Menu(self.menubar)
        #self.view = tk.Menu(self.menubar)
        #self.save = tk.Menu(self.menubar)

        #menubar.add_command(menu= save, label= 'Save', command= lambda: print('saved'))
        self.menubar.add_cascade(menu= self.file, label= 'File')
        #self.menubar.add_cascade(menu= self.edit, label= 'Edit')
        #self.menubar.add_cascade(menu= self.view, label= 'View')

        self.file.add_command(label= "New (Existing)", command= lambda: ExistFileWindow())
        self.file.add_command(label= "New (New)", command= lambda: NewFileWindow())
        self.file.add_separator()
        self.file.add_command(label= "Open", command= self.openFile)
        #self.file.add_command(label= "Export Stats") 

# Checkboxes setup
    def setup_checkboxes(self) -> None:

        self.leftWBox = tk.Checkbutton(self.legendArea, text= 'Left Wither', command= lambda: self.toggle_line(0), bg= "DarkOrchid1", padx=35, pady=15, font= tk.font.Font(size=15))
        self.rightWBox = tk.Checkbutton(self.legendArea, text = 'Right Wither', command= lambda: self.toggle_line(1), bg="PaleVioletRed1", padx=35, pady=15, font= tk.font.Font(size=15))
        self.leftShBox = tk.Checkbutton(self.legendArea, text= 'Left Shoulder', command= lambda: self.toggle_line(2), bg= "dodger blue", padx=25, pady=15, font= tk.font.Font(size=15))
        self.rightShBox = tk.Checkbutton(self.legendArea, text= 'Right Shoulder', command= lambda: self.toggle_line(3), bg= "PaleTurquoise1", padx=25, pady=15, font= tk.font.Font(size=15))
        self.leftSpBox = tk.Checkbutton(self.legendArea, text= 'Left Spine', command= lambda: self.toggle_line(4), bg= "lime green", padx=39, pady=15, font= tk.font.Font(size=15))
        self.rightSpBox = tk.Checkbutton(self.legendArea, text= 'Right Spine', command= lambda: self.toggle_line(5), bg= "goldenrod1", padx=39, pady=15, font= tk.font.Font(size=15))
        self.leftTBox = tk.Checkbutton(self.legendArea, text= 'Left Thoracic', command= lambda: self.toggle_line(6), bg="black", fg="snow", padx=26, pady=15, font= tk.font.Font(size=15))
        self.rightTBox = tk.Checkbutton(self.legendArea, text= 'Right Thoracic', command= lambda: self.toggle_line(7), bg= "firebrick1", padx=26, pady=15, font= tk.font.Font(size=15))
        
        self.rightWBox.grid(column= 1, row= 0)
        self.leftWBox.grid(column= 0, row= 0)
        self.rightShBox.grid(column= 1, row = 1)
        self.leftShBox.grid(column= 0, row = 1)
        self.rightSpBox.grid(column= 1, row = 2)
        self.leftSpBox.grid(column= 0, row= 2)
        self.rightTBox.grid(column= 1, row= 3)
        self.leftTBox.grid(column= 0, row= 3)
        

    def toggle_line(self, line_num):
        self.lineList[line_num].set_visible(not self.lineList[line_num].get_visible())
        self.changePlot()


    def setup_plot(self) -> None:
        
        
        self.fig, self.ax = plt.subplots()  # Set the desired figure size
        self.fig.tight_layout()
        # minutes = [value // 60 for value in self.dataX]
        # seconds = [value % 60 for value in self.dataX]
        # timestamp = [f"{x:2.0f}" + ":" + f"{y:2.1f}" for x, y in zip(minutes, seconds)]
        self.ax.set_xlabel("Time (seconds)")
        # self.ax.set_xticks(self.dataX, timestamp)
        # self.ax.xaxis.set_major_locator(plt.MaxNLocator(10))
        self.ax.set_ylabel("Force (pounds)")
        line1, = self.ax.plot([], [], visible=True, color= "blueviolet")
        line2, = self.ax.plot([], [], visible=True, color= "pink")
        line3, = self.ax.plot([], [], visible=True, color= "royalblue")
        line4, = self.ax.plot([], [], visible=True, color= "paleturquoise")
        line5, = self.ax.plot([], [], visible=True, color= "forestgreen")
        line6, = self.ax.plot([], [], visible=True, color= "gold")
        line7, = self.ax.plot([], [], visible=True, color= "black")
        line8, = self.ax.plot([], [], visible=True, color= "firebrick")
        self.lineList = [line1, line2, line3, line4, line5, line6, line7, line8]
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphArea)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Fill the entire window
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.zoomArea)
        self.toolbar.update()
        self.toolbar.pack()

    def changePlot(self):
        for i in range(8):
            if self.lineList[i].get_visible():
                self.lineList[i].set_data(self.dataX, self.dataY[i])
            else:
                self.lineList[i].set_data([], [])

        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

    def openFile(self):
        self.filename = tk.filedialog.askopenfilename(initialdir = "/Capstone Code/DataFiles", title = "Select a File",
                                                       filetypes = (("Text files","*.csv*"), ("all files","*.*")))
        if self.filename != '':
            self.dataX, self.dataY= self.initialData(self.filename)
            self.changePlot()
            self.root.title(self.filename)

    def setup_stats(self):
        
        buttonFrame = ttk.Frame(self.statArea)
        buttonFrame.pack()
        runStatButton = ttk.Button(buttonFrame, text= "Run Stats", command= self.runStats)
        #saveStatsButton = ttk.Button(buttonFrame, text= "Save Stats", command= self.saveStats)
        runStatButton.grid()
        #saveStatsButton.grid(column=1, row= 0)
        self.statsFont = tk.font.Font(size = 12)

        self.withFrame = ttk.Frame(self.statArea)
        self.withFrame.pack()
        ttk.Label(self.withFrame, text= "Withers", font= self.statsFont).grid(column=0, row=0)

        self.sholFrame = ttk.Frame(self.statArea)
        self.sholFrame.pack()
        ttk.Label(self.sholFrame, text= "Shoulders", font= self.statsFont).grid(column=0, row=0)

        self.spinFrame = ttk.Frame(self.statArea)
        self.spinFrame.pack()
        ttk.Label(self.spinFrame, text= "Spine", font= self.statsFont).grid(column=0, row=0)

        self.thorFrame = ttk.Frame(self.statArea)
        self.thorFrame.pack()
        ttk.Label(self.thorFrame, text= "Thoracic", font= self.statsFont).grid(column=0, row=0)


    def runStats(self):
        x_min, x_max = self.ax.get_xbound() 
        if x_min < 3:
            x_min = 3
            #f x_max > 
        timeBound = [x_min, x_max]
        self.statisticalData = horseStats(timeBound, self.dataY).data
        self.generateLabel(self.withFrame, 0)
        self.generateLabel(self.sholFrame, 1)
        self.generateLabel(self.spinFrame, 2)
        self.generateLabel(self.thorFrame, 3)

        #print(timeBound)

    def saveStats(self):
        pass

    def generateLabel(self, master, location):
        # fluxLab = ttk.Label(master, text= f"Flux: {self.statisticalData[location*2][6]}")
        # fluxLab.grid(column=1, row=0)
        leftFrame = ttk.Frame(master)
        leftFrame.grid(column=0, row = 1)
        for widget in leftFrame.winfo_children():
            widget.destroy()
        ttk.Label(leftFrame, text= "Left").grid(column=0, row=0)
        ttk.Label(leftFrame, text=f"Average: {self.statisticalData[location*2][0]:.1f}").grid(column=0, row=1)
        ttk.Label(leftFrame, text=f"Range: {self.statisticalData[location*2][1]:.1f}").grid(column=0, row=2)
        ttk.Label(leftFrame, text=f"Min: {self.statisticalData[location*2][2]:.1f} @ {self.statisticalData[location*2][4]}").grid(column=1, row=1)
        ttk.Label(leftFrame, text=f"Max: {self.statisticalData[location*2][3]:.1f} @ {self.statisticalData[location*2][5]}").grid(column=1, row=2)
        rightFrame = ttk.Frame(master)
        rightFrame.grid(column=1, row = 1)
        for widget in rightFrame.winfo_children():
            widget.destroy()
        ttk.Label(rightFrame, text= "Right").grid(column=0, row=0)
        ttk.Label(rightFrame, text=f"Average: {self.statisticalData[location*2+1][0]:.1f}").grid(column=0, row=1)
        ttk.Label(rightFrame, text=f"Range: {self.statisticalData[location*2+1][1]:.1f}").grid(column=0, row=2)
        ttk.Label(rightFrame, text=f"Min: {self.statisticalData[location*2+1][2]:.1f} @ {self.statisticalData[location*2+1][4]}").grid(column=1, row=1)
        ttk.Label(rightFrame, text=f"Max: {self.statisticalData[location*2+1][3]:.1f} @ {self.statisticalData[location*2+1][5]}").grid(column=1, row=2)


    def initialData(self, path):

        data = []
        data_x = []
        data_y = [[] for _ in range(8)]
        for i in range(8):
            data_y[i] = []



        with open(path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                data.append(row)

        for i, rows in enumerate(data):
            if i > 3:
                data_x.append(float(i-3)*(5/6))
            for k, col in enumerate(data[i]):
                if i>3:
                    if k%10 == 8:
                        num = k//10 
                        data_y[num].append(abs(float(data[i][k])))
        
        return data_x, data_y




if __name__ == "__main__":
    runner = MyWindow(tk.Tk(), "C:/Capstone Code/DataFiles/Test_Data/SESS250_format.csv")