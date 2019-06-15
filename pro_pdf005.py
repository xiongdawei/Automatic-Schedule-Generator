from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.colors import CMYKColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle,Frame,ListFlowable, ListItem
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

Style = getSampleStyleSheet()
bt = Style['Normal']
bt.fontsize = 14
bt.fristLineIndent = 32
bt.leading = 20

ct = Style['Normal']
ct.fontSize = 12
ct.alignment = 1

ct.textColor = colors.red
t = Paragraph('hello',bt)
pdf = SimpleDocTemplate('ppff.pdf')
pdf.build([t])



"""
d = Drawing(200,200)
s = String(50,50,'victor is a good man', textAncher = 'middle')
d.add(s)
renderPDF.drawToFile(d,'simple.pdf')

story = []
table_style = [
    ('FONTNAME', (0, 0), (-1, -1), 'msyh'),
    ('FONTSIZE', (0, 0), (2, 0), 8),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('ALIGN', (0, 0), (2, 0), 'CENTER'),
    ('ALIGN', (0, 1), (2, 8), 'LEFT'),
    ('VALIGN', (0, 0), (2, 8), 'MIDDLE'),
    ('SPAN', (0, 3), (0, 4)),
    ('SPAN', (0, 5), (0, 6)),
    ('SPAN', (0, 7), (0, 8)),
    ('BACKGROUND', (0, 0), (2, 0), colors.lightslategray),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),
    ('GRID', (0, 0), (-1, -1), 0.1, colors.slategray),
]
table_data = [['Year', 'Month', 'Day'],
                  ['2017', '3', '12'],
                  ['2017', '4', '13'],
                  ['2017', '5', '14'],
                  ['2017', '6', '15'],
                  ['2018', '7', '16'],
                  ['2018', '8', '17'],
                  ['2018', '9', '18'],
                  ['2018', '10', '19'],
                  ]

table_table = Table(table_data, colWidths=[42, 38, 147])
story.append(table_table)
story.append(Spacer(240,10))
doc = SimpleDocTemplate('davidxiong/Desktop/' +'test'+'.pdf',pagesize=[10,20], topMargin = 15, bottomMargin = 15)
"""
