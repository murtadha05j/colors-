from pyautocad import Autocad, APoint, aDouble, math

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)


def one(w,h):
  acad.model.AddPolyline(aDouble(0,0,0,w,0,0,w,h,0,0,h,0,0,0,0))

  for i in range(0, 360, 20):
    a = APoint(w/2, h/2)
    b = APoint(w/2, h/2)
    c = APoint(w/2, h/2)
    b.x += math.cos(i * math.pi / 180) * 20
    b.y += math.sin(i * math.pi / 180) * 20
    c.x += math.cos(i * math.pi / 180) * 10
    c.y += math.sin(i * math.pi / 180) * 10
    acad.model.AddLine(a, b)
    acad.model.AddCircle(b, 5)
    acad.model.AddCircle(c, 2.5)


def two():

  a = APoint(0, 0)
  c = acad.model.AddCircle(a, 20)

  for i in range(0, 10):
    c.Copy()
    c.Rotate(APoint(0, 50), i)



def three(w,h):
  acad.model.AddPolyline(aDouble(0, 0, 0, w, 0, 0, w, h, 0, 0, h, 0, 0, 0, 0))
  d=50
  for i in range(0, 360,20):

    a = APoint(w / 2, h / 2)
    b = APoint(w / 2, h / 2)
    c=a

    a.x += math.cos(i * math.pi / 180) * d
    a.y += math.sin(i * math.pi / 180) * d
    b.x += math.cos(-i * math.pi / 180) * 10
    b.y += math.sin(i * math.pi / 180) * 10
    lo = acad.model.AddLine(a, b)
    for g in range(0,360,1):
      c = acad.model.AddCircle(a, 20)
      c.Copy()
      c.Move(a,c)
      c.x+=10
      c.y+=10








three(100,300)