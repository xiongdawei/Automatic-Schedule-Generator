from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('xinwei','STXINWEI.TTF'))
from pagetemp import MyPageTemp

from reportlab.platypus import BaseDocTemplate,Paragraph,PageTemplate,FrameBreak
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

class MyPDFdoc():
    def __init__(self,filename):
        self.mypage = MyPageTemp()
        self.filename = filename
        self.height = 12*inch
        self.width = 9*inch
        self.doc = BaseDocTemplate(self.filename, pagesize = (9*inch,12*inch))
        self.doc.addPageTemplates(self.mypage)
        self.styles = getSampleStyleSheet()
        self.styleT = self.styles['Title']
        self.styleT.fontName = 20


