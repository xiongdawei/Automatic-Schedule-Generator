from reportlab.platypus import PageTemplate, Frame
from reportlab.lib.units import inch

class MyPageTemp(PageTemplate):
    def __init__(self):
        self.width = 9*inch
        self.hight = 12*inch
        Frame1 = Frame(inch, 10*inch, 4*inch, inch, id='frame1', showBoundary=1)
        Frame2 = Frame(inch, 9*inch, 4*inch, inch, id = 'frame2', showBoundary=1)
        Frame3 = Frame(inch, 5*inch, 4*inch, 4*inch, id = 'frame3', showBoundary=1)
        PageTemplate.__init__(self,'MyTemplate',[Frame1, Frame2, Frame3])



