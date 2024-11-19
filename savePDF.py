import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.units import inch

class GenerateReport:
    def __init__(self, filename, image, stats, notes):
        doc = SimpleDocTemplate(filename + ".pdf", pagesize= letter)
        img = Image(image)
        img.drawHeight = 4 * inch
        img.drawWidth = 6 * inch
        img.hAlign = 'CENTER'
        self.genInnerTables(stats)
        paragraph = Paragraph(notes)
        self.items = []
        self.items.append(img)
        self.items.append(self.add_legend())
        self.items.append(Spacer(1, 72))
        self.items.append(self.bigTable)
        self.items.append(Spacer(1, 12))
        self.items.append(paragraph)
        doc.build(self.items)
        # doc.showPage()
        # doc.save()

    def add_legend(self):
        legend_items = [
            ("Left Withers", colors.blueviolet, "Right Withers", colors.pink),
            ("Left Shoulders", colors.royalblue, "Right Shoulders", colors.paleturquoise),
            ("Left Spine", colors.forestgreen, "Right Spine", colors.gold),
            ("Left Thoracic", colors.dimgray, "Right Thoracic", colors.firebrick)
        ]
        self.items.append(self.create_legend(legend_items))

    def create_legend(self, legend_items):
        from reportlab.platypus import Flowable

        class LegendFlowable(Flowable):
            def __init__(self, legend_items):
                Flowable.__init__(self)
                self.legend_items = legend_items

            def draw(self):
                canvas = self.canv
                x = -0.5 * inch
                y = self.height - 0.5 * inch
                
                for i, (left_name, left_color, right_name, right_color) in enumerate(self.legend_items):
                    # Draw left line
                    canvas.setFillColor(left_color)
                    canvas.rect(x + i * 2 * inch, y, 0.2 * inch, 0.2 * inch, fill=1)
                    canvas.setFillColor(colors.black)
                    canvas.drawString(x + 0.3 * inch + i * 2 * inch, y, left_name)
                    
                    # Draw right line below left line
                    canvas.setFillColor(right_color)
                    canvas.rect(x + i * 2 * inch, y - 0.3 * inch, 0.2 * inch, 0.2 * inch, fill=1)
                    canvas.setFillColor(colors.black)
                    canvas.drawString(x + 0.3 * inch + i * 2 * inch, y - 0.3 * inch, right_name)

        return LegendFlowable(legend_items)
    

    def genInnerTables(self, stats):
        self.innerTables = []
        for i in range (8):
            topRow = []
            botRow = []
            topRow.append(f"Average: {stats[i][0]:.1f}")
            botRow.append(f"Range: {stats[i][1]:.1f}")
            topRow.append(f"Max: {stats[i][3]:.1f} at {stats[i][5]} sec")
            botRow.append(f"Min: {stats[i][2]:.1f} at {stats[i][4]} sec")
            tableData = [topRow, botRow]
            self.innerTables.append(Table(tableData))
        self.genTable(self.innerTables)

    def genTable(self, innerTables):
        data = [
            ['', 'Left', 'Right'], 
            ['Withers', innerTables[7], innerTables[6]],
            ['Shoulders', innerTables[5], innerTables[4]],
            ['Spine', innerTables[3], innerTables[2]],
            ['Thoracic', innerTables[1], innerTables[0]]
                ]
        self.bigTable = Table(data)