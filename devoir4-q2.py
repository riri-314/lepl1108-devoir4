import matplotlib.pyplot as plt

def SimpArmy():  
    a = 0
    integral = []
    for i in range(1,2000,2):
        a += 4*((1-(((i-1)*0.001))**2)**(1/2)) + 4*(4*((1-((i*0.001))**2)**(1/2))) + 4*((1-(((i+1)*0.001))**2)**(1/2)) 
        b = 0.001/3.0 * a
        integral.append(b)
        #print(i,"integral",b)
    #print(len(integral))
    print(integral)
    return integral

def BelleDelphine():
    plt.plot(SimpArmy())
    plt.plot([0,1000],[3.14,3.14],'r--')
    plt.xlabel('\N{LATIN SMALL LETTER N}')
    plt.ylabel('\N{GREEK SMALL LETTER PI}')
    plt.suptitle('Estimation de \N{GREEK SMALL LETTER PI} via la méthode d’intégration composite de Simpson')
    plt.show()
    
print(BelleDelphine())