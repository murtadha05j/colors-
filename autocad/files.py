class music():
    def line(self):
        with open('test.txt') as ff:
            lines = ff.read().splitlines()
            odd = lines[::2]
            even = lines[1::2]
        try:
            counter = 0
            counter1 = 4
            a = 0
            o = 1
            for jj in range(len(odd)):
                line0 = "p%d=acad.model.AddLine(APoint(%s),APoint(%s))" % (counter, odd[jj], even[jj])
                line1 = "p%d=acad.model.AddLine(APoint(%s),APoint(%s))" % (counter + 1, even[jj], odd[jj + o])

                if jj == len(odd) - 2:
                    o -= 1

                print(line0)
                print(line1)

                if jj == 0: # to type p.delete
                    a += 1

                elif jj == a:

                    print("##### light #####")
                    q = "p%d.delete()" % (counter1)
                    v = open("add.txt", "a")
                    v.write(q)
                    v.write("\n")
                    a += 2
                    counter1 += 5

                counter += 2

            olf = open("add.txt", "r")
            for hh in olf:
                print(hh)


        except Exception as ee:
            print(ee)

    ###################################################### polyline

    def polyline(self):
        nl=[]
        v=open("PolylineFile.txt","r")

        r=v.read()
        c0 = "acad.model.AddPolyLine(aDouble(%s))" % (r)
        print(c0)

    def spline(self):
        nl = []
        v = open("PolylineFile.txt", "r")

        r = v.read()
        c0 = "acad.model.AddSpline(aDouble(%s),APoint(0,0),APoint(0,0))" % (r)
        print(c0)
    def equation(self):
        v=open("PolylineFile.txt","w")
        r=v.read()
        c1="acad.model.AddSpline(%s),APoint(0,0),APoint(0,0))" % (r)
music().polyline()