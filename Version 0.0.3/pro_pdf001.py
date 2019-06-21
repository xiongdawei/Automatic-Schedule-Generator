from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph,Table,TableStyle, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.units import inch




def table_model(data):
    width = 7.2
    colWidths = (width/len(data[0])) * inch
    dis_list = []
    for x in data:
        dis_list.append(x)

    style = [
        ('FONTSIZE', (0, 0), (-1, 0), 15),
        ('BACKGROUND', (0, 0), (-1, 0) ),
        ('BACKGROUND', (0, 1), (-1, 1)),
        ('SPAN', (0, 0), (0, 1)),
        ('SPAN', (1, 0), (2, 0)),
        ('SPAN', (3, 0), (4, 0)),
        ('SPAN', (5, 0), (7, 0)),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LINEBEFORE', (0, 0), (0, -1), 0.1, colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.royalblue),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.red),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]

    component_table = Table(dis_list,colWidths = colWidths, style = style)
    return component_table

Style = getSampleStyleSheet()
n = Style['Normal']

data = [[0,1,2,3,4,5,6,7],
        [00,11,22,33,44,55,66,77],
        [000,111,222,333,444,555,666,777],
        [0000,1111, 2222, 3333, 4444, 5555, 6666, 7777],]

z = table_model(data)
pdf = SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([Paragraph('Title',n),z])


'''
Style = getSampleStyleSheet()
bt = Style['Normal']
bt.fontSize = 14
bt.leading = 20

ct = Style['Normal']
ct.fontSize = 12
ct.leading = 20

ct.textColor = colors.red

t = Paragraph('hello',bt)
pdf = SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([t])
'''


