from pyautocad import Autocad, APoint, aDouble
import array # for polyline
import math
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

################
#   line       #
################

#p0=APoint(0,0)
#p1=APoint(1,1)
#line1=acad.model.AddLine(p0,p1)
#line1.Move(p0,APoint(8,8))

################
#   polyline   #
################
#points=aDouble(0,0,0,3,3,4,5,6,7,8,9,3,2,6,8)
#points1=array.array("d",[1,2,4,5,5,6,6,7,7,3,4,5,6,7,7])
#acad.model.AddPolyline(points1)

################
#   point      #
################

#p0=APoint(3,3)
#acad.model.AddPoint(p0)
#acad.doc.SetVariable("PDMODE",65) # the shape of point
#acad.doc.SetVariable("PDSIZE",0.1) # the size of point

################
#  circle&arc  #
################

#acad.model.AddCircle(p0,3.5)
#acad.model.AddArc(p0,2,0,180*math.pi/180) # arc parameter are: start point of arc, radius, start angle, end angle in radian: must convert from radian to degree

################
#   ellipse    #
################
#p0=APoint(2,2)
#p1=APoint(2,4)
#acad.model.AddEllipse(p0,p1,0.5) # parameters: center of ellipse, the largest radius of ellipse, the ratio ( LR/SR)

################
#   text       #
################

#p0=APoint(0,2)
#p1=APoint(0,0)
#acad.model.AddText("hello  world",p0,0.5) # parameter: first point for the start text, the second for high of text

################
#   solid      #
################

#p0=APoint(0,0)
#p1=APoint(4,0)
#p2=APoint(4,4)
#p3=APoint(0,4)
#acad.model.AddSolid(p0,p1,p3,p3)


################
#   copy&move  #
################
#p0=APoint(0,0)
#c=acad.model.AddCircle(p0,2)
#c.Move(APoint(0,0),APoint(0,4))
#c1=c.Copy()
#c1.Move(APoint(0,0),APoint(0,4))


################
# rotate&mirror #
###############

#line=acad.model.AddLine(APoint(0,0),APoint(1,1))
#line.Rotate(APoint(0,0),180*3.14/180)
#line.Mirror(APoint(1, 1), APoint(1, -4))

####################################################################
for i in range(5):
    text = acad.model.AddText('Hi %s!' % i, p1, 2.5)
    acad.model.AddLine(p1, p2)
    acad.model.AddCircle(p1, 10)
    p1.y+= 22
    p2.y+=22