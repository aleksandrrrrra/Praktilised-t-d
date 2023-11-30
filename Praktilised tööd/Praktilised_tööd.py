from math import *
from random import *

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
p=1
for x in range(8):
    A = float(input(f"Sisestage number {x + 1}: "))
    if A > 0:
        p *= A
print(f"Positiivsete arvude korrutis: {p}")

#15
for y in range(10):
    for x in range(10):
        print(x,end=" ")
    print()


#29
for i in range(9):
    for x in range(9):
        if x==0 or i==x:
            print("x", end = " ")
        else:
            print("0", end = " ")
    print()

#4
for number in range(10, 21):
    ruut = number ** 2
    print(f"Numbri ruut {number}: {ruut}")

#5
N = int(input("Sisestage numbrite arv N: "))

negatiivne_summa = 0

for i in range(N):
    number = float(input(f'Sisestage number {i + 1}: '))

    if number < 0:
        negatiivne_summa += number

print(f'Negatiivsete arvude summa: {negatiivne_summa}')

#17
number = 2

for i in range(1, 10):
    tulemus = number * i
    print(f"{number}*{i}={tulemus}")

#16
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i if i == j else 0}", end=" ")
    
    print()

#31
K = int(input("Sisestage kotlettide arv (K): "))
M = int(input("Sisestage panni suurus (M): "))

täis_pannid = K // M
järelejäänud_kotletid = K % M

print(f"Panne täis: {täis_pannid}")
print(f"Kotlet jääb viimasele praepannile: {järelejäänud_kotletid}")

#12
N=randint(2,10)
m=randint(1,10)
summa=m
print("Masinad: ",N)
print("Tunnid: ",m)
for t in range(N-1):
       m=(m/6)*7 
       summa+=m
       print(m)
print("Kokku masinad töötasid:",summa,"tn")

#28
import random
salajane_number = random.randint(1, 100)

katsed = 0
õigesti = False

while not õigesti:
    guess = int(input("Arva ära arv vahemikus 1 kuni 100: "))
    
    katsed += 1
    
    if guess == salajane_number:
        õigesti = True
        print(f"Palju õnne! Sa arvasid numbri ära {salajane_number}, {katsed} katsega.")
    elif guess < salajane_number:
        print("Peidetud arv on suurem.")
    else:
        print("Peidetud arv on väiksem.")
