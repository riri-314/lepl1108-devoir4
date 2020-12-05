import random as r
import math as m
import matplotlib.pyplot as plt

def pin():
    pi = []
    inside=0
    outside=0
    n=1001
    for i in range(1,n):
        x=r.uniform(-1,1)
        y=r.uniform(-1,1) #uniform mieux que random (via stackoverflow)
        if x**2+y**2<=1:
            inside+=1
        outside+=1
        pin=4*inside/outside
        pi.append(pin)
        #print ('n:',i,' pin:',pin)
    return(pi)
    

def intconf1():
    y1 = []
    y2 = []
    n=1
    for i in pin():
        pipi=1.96*(m.sqrt(abs(i-(i**2)))/m.sqrt(n))
        n+=1
        y1.append(i-pipi)
    return y1

def intconf2():
    y1 = []
    y2 = []
    n=1
    for i in pin():
        pipi=1.96*(m.sqrt(abs(i-(i**2)))/m.sqrt(n))
        n+=1
        y2.append(i+pipi)
    return y2
    
    
def plot():
    xi=pin()
    print(xi)
    plt.suptitle('Estimation de \N{GREEK SMALL LETTER PI} et intervalle de confiance à 95%')
    plt.plot(xi)
    plt.plot([0,1000],[3.14,3.14],'r--')
    plt.plot(intconf1(),'g')
    plt.plot(intconf2(),'g')
    plt.xlabel('\N{LATIN SMALL LETTER N}')
    plt.ylabel('\N{GREEK SMALL LETTER PI}')
    plt.show()
    
print(plot())