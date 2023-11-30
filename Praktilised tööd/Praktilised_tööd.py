from math import *


for x in range(10):
    R=float(input("{0}.R: ".format(x+1)))
    if R>0:
        S=pi*R**2
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))

while True: 
    R=float(input("{0}.R: ".format(x+1)))
    if R>0:
        S=pi*R**2
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))
    if x==10:
        break

x=0
while x<10:
    x+=1
    R=float(input("{0}.R: ".format(x+1)))
    if R>0:
        S=pi*R**2
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))
#10 S
x=0
while x<10:
    x+=1
    R=float(input("{0}.R: ".format(x+1)))
    if R>0:
        S=pi*R**2
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))

#10 практических заданий по теме Циклы
from math import *
#1
t=0
for x in range(15):
    A=float(input("Sisesta A: "))
    if A.is_intenger(): # 5.0; 6 = True; 2.45 = False
        t+1
print(t)

#2
summa=0
A=int(input("Sisesta A: "))
for x in range(1,A+1,1):
    summa+=x
print("Summa: {0}".format(summa))

#3
summa=1
for x in range(8):
    A = float(input(f"Sisestage number {x + 1}: "))
    if A > 0:
        summa *= A
print(f"Positiivsete arvude korrutis: {summa}")

#4
