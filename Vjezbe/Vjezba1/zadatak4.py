def jed_pravca(x1,y1,x2,y2):
    k=(y2-y1)/(x2-x1)
    l=y1-k*x1
    print("y={}x+{}".format(k,l))
x1=float(input("x1:"))
y1=float(input("y1:"))
x2=float(input("x2:"))
y2=float(input("y2:"))
jed_pravca(x1,y1,x2,y2)