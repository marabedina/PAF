import matplotlib.pyplot as plt
import numpy as np
def jed_pravca(x1,y1,x2,y2):
    k=(y2-y1)/(x2-x1)
    l=y1-k*x1
    print("y={}x+{}".format(k,l))
x1=float(input("x1:"))
y1=float(input("y1:"))
x2=float(input("x2:"))
y2=float(input("y2:"))
jed_pravca(x1,y1,x2,y2)
plt.xlabel('x')
plt.ylabel('y')
k=(y2-y1)/(x2-x1)
l=y1-k*x1
x_vr=np.linspace(x1,x2)
y_vr=k*x_vr+1
plt.plot(x_vr,y_vr)
plt.plot([x1,x2],[y1,y2], 'o')
opcija=input("odaberite ocete spremiti graf kao pdf ili ga prikazati na ekranu(pdf/ekkran)")
if opcija=='ekran':
    plt.show()
elif opcija=='pdf':
    datoteka=input("ime datoteke:")+'.pdf'
    plt.savefig(datoteka)