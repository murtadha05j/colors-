import csv
import math as pi
from pyautocad import Autocad, APoint, aDouble, math

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

def draw(x,y,w,h):


    a=0
    b=0
    ox=750/900*w+x
    oy= 488.3/2270*h+y
    for n in range(12):
        l0 = acad.model.AddLine(APoint(ox-a,oy  + 6*b), APoint(ox- a, oy+1631.6/2270*h - b))
        l0 = acad.model.AddLine(APoint(ox- a, oy+1631.6/2270*h - b), APoint(460/900*w + a, oy+1631.6/2270*h - b))
        l0 = acad.model.AddLine(APoint(460/900*w + a, oy+1631.6/2270*h - b),APoint(460/900*w  + a, 1841.6/2270*h))
        acad.model.AddSpline(aDouble(460/900*w  + a, 1841.6/2270*h, 0, 534.5/900*w+a , 1149.9/2270*h , 0, ox-a,oy +b*6, 0), APoint(0, 0),APoint(0, 0))
        a+=(12/290)*w*0.5*0.5
        b+=(57.5/1631.66)*h*0.2*0.5




draw(0,0,900,2270)