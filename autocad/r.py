from pyautocad import Autocad, APoint
import math
import numpy as np

# Create connection with autoCAD
# When there is a running CAD program, it will establish a connection with it, and always connect with the active CAD window
# When not, a new CAD program will be started
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)  # Get the connected CAD file name

"""---------------------------------------------------------------------------------"""
# Layer related operations
# New layer
new_layer = acad.ActiveDocument.Layers.Add("HIT_Layer")
# Set a layer as the current layer
acad.ActiveDocument.ActiveLayer = new_layer
# Set layer color
new_layer.color = 1
# Set the layer line type
new_layer.LineType = "ACAD_ISO02W100"
# Set the layer line width
new_layer.LineWeight = 0.1
# Set layer status
new_layer.LayerOn = True  # TRUE: The layer is open; FALSE: The layer is closed
new_layer.Lock = False  # TRUE: The layer is locked; FALSE: The layer is not locked
# Specify the layer name
print(new_layer.Name)
# Specify the layer of the primitive
circle = acad.model.AddCircle(APoint(0, 0), 200)
circle.Layer = "HIT_Layer1"

# Create layers in batch
color_list = [1, 2, 3]
layers_name = ["HIT_Layer_1", "HIT_Layer_2", "HIT_Layer_3"]
try:
    len(color_list) == len(layers_name)
except:
    print("The number of layer color numbers does not match the number of layers")
layers_obj = [acad.ActiveDocument.Layers.Add(i) for i in layers_name]
for j in range(len(layers_obj)):
    layers_obj[j].color = color_list[j]
"""---------------------------------------------------------------------------------"""
# General drawing operations (copy, move, zoom...)
# Copy the given object at the same location
circle1 = acad.model.AddCircle(APoint(200, 200), 200)
circle2 = circle1.Copy()
# Move the primitive object from the source to the target
circle2.Move(APoint(0, 0), APoint(100, 0))
# Create a mirror image copy of the plane object around the axis
# RetVal = object.Mirror(Point1, Point2)
circle2.Mirror(APoint(0, 0), APoint(100, 0))
# Delete the specified object or a group of saved layer settings
circle1.Delete()
# Get the intersection point of the object and other objects in the graph
# RetVal = object.IntersectWith(IntersectObject, ExtendOption)
# ExtendOption: This option specifies whether there is no, single or two objects in the two objects to get the intersection point
# 0 = acExtendNone Neither object extends
# 1 = acExtendThisEntity extends the basic object.
# 2 = acExtendOtherEntity extends the object passed as a parameter.
# 3 = acExtendBoth extends two objects
line1 = acad.model.AddLine(APoint(1000, 0), APoint(1500, 500))
line2 = acad.model.AddLine(APoint(1000, 500), APoint(1500, 0))
point = line1.IntersectWith(line2, 0)
print(point)
# Rotate the primitive object around a point
# object.Rotate(BasePoint, RotationAngle)
base_point = APoint(0, 0)
rotate_angle = math.pi/4
line1.Rotate(base_point, rotate_angle)
# Specify the line width of individual primitives or the default line width of graphics
print(line1.Lineweight)
# Specify the line type of the primitive
print(line1.LineType)
# Create a new object offset by a specified distance from an existing object
# circle1.OffSet(-10.0)
"""---------------------------------------------------------------------------------"""
# Form creation
# RetVal = object.AddTable(InsertionPoint, NumRows, NumColumns, RowHeight, ColWidth)
table = acad.model.AddTable(APoint(0, 0), 5, 5, 100, 200)
# Set the text value of the specified row and column
# object.SetText(row, col, pStr)
table.SetText(3, 2, "List")
# Set the text height of the specified line type
# object.SetTextHeight(rowTypes, TextHeight)
table.SetTextHeight(3, 50)
# Set the text rotation angle of rows and columns
# object.SetTextRotation(row, col, TextRotation)
table.SetTextRotation(3, 2, math.pi/2)
# Set the row and column index of the cell in the sub-selection set
# object.SetSubSelection(rowMin, rowMax, colMin, colMax)
# Set the row height of the specified row index in the table
# object.SetRowHeight(row, Height)
table.SetRowHeight(1, 500)
# Set the column width of the column where the specified column index in the table is located
# object.SetColumnWidth(col, Width)
table.SetColumnWidth(1, 500)
"""---------------------------------------------------------------------------------"""
# Block related operations
# Create block
grip = APoint(20, 0)
blockObj = acad.ActiveDocument.Blocks.Add(grip, "HIT_Block")
# You can use block_obj.Add...() to add objects to the block
# Insert graphic file or named block defined in current graphic
# RetVal = object.InsertBlock(InsertionPoint, Name, Xscale, Yscale, ZScale, Rotation [, Password])
# Name: The name of the inserted AutoCAD drawing file or block name. If it is a file name, it must include the .dwg extension and any path information for AutoCAD to find the file
"""---------------------------------------------------------------------------------"""
# Create selection set
try:
    acad.ActiveDocument.SelectionSets.Item("SS1").Delete()
except:
    print("Delete selection failed")

slt = acad.ActiveDocument.SelectionSets.Add('SS1')
# Select objects on the screen and add them to the selection set
slt.SelectOnScreen()
print("Please pick up the primitives on the screen and end with Enter")
# You can use the for loop to traverse the objects in the selection set for operation
"""---------------------------------------------------------------------------------"""
# Mark related operations
# Use three points to create angle labels
# RetVal = object.AddDim3PointAngular(AngleVertex, FirstEndPoint, SecondEndPoint, TextPoint)
# AngleVertex: Specify the three-dimensional WCS coordinates of the angle vertex to be measured
angle_vertex = APoint(100, 100)
first_endpoint = APoint(100, 0)
second_endpoint = APoint(0, 100)
text_point = APoint(50, 50)
dim_arc = acad.model.AddDim3PointAngular(angle_vertex, first_endpoint, second_endpoint, text_point)
# Create alignment label object
# RetVal = object.AddDimAligned(ExtLine1Point, ExtLine2Point, TextPosition)
# ExtLine1Point: Only used to enter the 3D WCS coordinates of the first end point of the specified extension line
# ExtLine2Point: Only used to enter the 3D WCS coordinates of the second end of the specified extension line
# TextPosition: Only used to enter the 3D WCS coordinates of the specified text position
ext_line1_point = APoint(100, 0)
ext_line2_point = APoint(0, 100)
text_position = APoint(50, 100)
dim = acad.model.AddDimAligned(ext_line1_point, ext_line2_point, text_position)
# Create arc length label of arc
# RetVal = object.AddDimArc(ArcCenter, FirstEndPoint, SecondEndPoint, ArcPoint)
arc_center = APoint(100, 0)
first_endpoint = APoint(0, 100)
second_endpoint = APoint(100, 0)
arc_point = APoint(0, 0)
arc_dim = acad.model.AddDimArc(arc_center, first_endpoint, second_endpoint, arc_point)
"""---------------------------------------------------------------------------------"""
# Create a 3DFace object given four vertices
# RetVal = object.Add3DFace(Point1, Point2, Point3[, Point4])
point1 = APoint(0, 0)
point2 = APoint(100, 0)
point3 = APoint(100, 100)
point4 = APoint(0, 100)
d_face = acad.model.Add3DFace(point1, point2, point3, point4)
"""---------------------------------------------------------------------------------"""
# Create an arc by specifying the center, radius, starting angle, and ending angle of the arc
# RetVal = object.AddArc(Center, Radius, StartAngle, EndAngle)
# Both the starting angle and the ending angle are expressed in radians
center = APoint(0, 0)
radius = 100
start_angle = math.pi/4
end_angle = math.pi/2
arc = acad.model.AddArc(center, radius, start_angle, end_angle)

"""---------------------------------------------------------------------------------"""

# Create a circle with a given center point and radius
# RetVal = object.AddCircle(Center, Radius)
center = APoint(0, 0)
radius = 150
circle = acad.model.AddCircle(center, radius)

"""---------------------------------------------------------------------------------"""
# Create an ellipse on the XY plane of the WCS given the center point, a point on the major axis and the radius ratio
# RetVal = object.AddEllipse(Center, MajorAxis, RadiusRatio)
# Center: The intersection of the long axis and the short axis
# MajorAxis: Specify the coordinates of the right end of the ellipse
# RadiusRatio: Define the positive value of the ratio of the major axis to the minor axis of the ellipse
center = APoint(0, 0, 0)
maj_Axis = APoint(100, 0, 0)
ellipse = acad.model.AddEllipse(center, maj_Axis, 0.25)

"""---------------------------------------------------------------------------------"""

# Create elliptical arc
EllArcCenter = APoint(50, 10)
majAxis = APoint(5, 0, 0)
EllArcObj = acad.model.AddEllipse(EllArcCenter, majAxis, 0.5)  # Create ellipse
# Intercept the ellipse arc on the ellipse
EllArcObj.startAngle = -90 * (3.14 / 180)
EllArcObj.endAngle = 90 * (3.14 / 180)

"""---------------------------------------------------------------------------------"""
# Create hatch objects
# RetVal = object.AddHatch(PatternType, PatternName, Associativity [, HatchObjectType])
center = APoint(200, 0)
radius = 150
circle1 = acad.model.AddCircle(center, radius)
pattern_type = 0
pattern_name = "ANSI31"
hatch = acad.model.AddHatch(pattern_type, pattern_name, True)
# hatch.AppendOuterLoop(circle1)
"""---------------------------------------------------------------------------------"""
# Create a point object at a given location
# RetVal = object.AddPoint(Point)
# point: Three-element double-precision array
point = np.array([200., 200., 0.])
point = acad.model.AddPoint(point)
"""---------------------------------------------------------------------------------"""
# Draw a straight line (start and end)
# RetVal = object.AddLine(StartPoint, EndPoint)
start_point = APoint(0, 0)
end_point = APoint(100, 100)
line = acad.model.AddLine(start_point, end_point)

"""---------------------------------------------------------------------------------"""
# Draw ordinary polyline
# RetVal = object.AddPolyline(VerticesList)
# VerticesList: At least two points (six elements) are required to form a polyline object. The size of the array must be a multiple of 3
pnts = [APoint(35, 35), APoint(40, 35), APoint(43, 32)]
pnts = np.array([j for i in pnts for j in i])
print(pnts)
pline_obj = acad.model.AddPolyLine(pnts)
pline_obj.Closed = True  # Set polyline closure

pline_obj.ConstantWidth = 0.5  # Set the line width of the polyline
# The second method of setting the line width: object.SetWidth(SegmentIndex, StartWidth, EndWidth)
SegmentIndex = 1    # Segment number of polyline
StartWidth = 10     # Line width at the beginning of the segment
EndWidth = 20       # Line width at the end of the paragraph
pline_obj.color = 1  # Set the line width of the polyline, set the color, you can also assign a value by creating a color object
"""---------------------------------------------------------------------------------"""
# Create a ray passing through two unique points
# RetVal = object.AddRay(Point1, Point2)
point1 = APoint(0, 0)
point2 = APoint(100, 100)
ray = acad.model.AddRay(point1, point2)

"""---------------------------------------------------------------------------------"""
# Create a construction line through two specified points
# RetVal = object.AddXline(Point1, Point2)
point1 = APoint(0, 0)
point2 = APoint(200, 100)
x_line = acad.model.AddXline(point1, point2)
"""---------------------------------------------------------------------------------"""
# Add multiple lines of text
# RetVal = object.model.AddMText(InsertionPoint, Width, Text)
insertion_point = APoint(100, 100)
width = 100
text = """hello world!
hello python"""
m_text = acad.model.AddMText(insertion_point, width, text)
"""---------------------------------------------------------------------------------"""
# Add single line of text
# RetVal = object.model.AddText(TextString, InsertionPoint, Height)
text_string = "hello world!"
Insertion_point = APoint(200, 200)
height = 10
s_text = acad.model.AddText(text_string, Insertion_point, height)
"""---------------------------------------------------------------------------------"""
# Related attributes
print(line.Angle)  # Get straight angle
print(arc.ArcLength)  # Get the arc length of the specified arc
print(circle.Area)  # Get area
m_text.AttachmentPoint = 2  # Set the insertion point of multi-line text

