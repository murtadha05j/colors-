import csv
from pyautocad import Autocad, APoint,aDouble
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)
from pyautocad import Autocad, APoint,aDouble

import numpy as np
import array # for polyline
import math

#y=100+222




x=0
y=0
w=100
h=100
def a(x,y,w,h):
    p0=APoint(x,y)
    p1=APoint(x+50,y+50)
    re=acad.model.AddPolyline(aDouble(x, y, 0, w + x, y, 0, w + x, h + y, 0, x, h + y, 0, x, y, 0))
    for aa in range(4):
        acad.model.AddLine(p0,p1)
        p0.y+=20
    c=acad.model.AddCircle(APoint(x+50,y+50),30)
    c.Mirror(APoint(130+x,0+y),APoint(130+x,500+y))
for n in range(4):
    a(x,y,w,h)
    y+=100*1.2



