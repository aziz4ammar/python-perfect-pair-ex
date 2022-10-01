import numpy as np
def saisir():
    test=False
    while test==False :
        print("donner un entier :)")
        n=int(input())
        test=(6<=n)
    return n

def remplir(T,n):
    for i in range(n):
        test = False
        while test == False:
            T[i] = int(input("T["+str(i)+"]="))
            test = T[i] >= 100
def premier(n):
    s=0
    for i in range(1,n//2 + 1):
        if (n%i==0):
            s+=1
    return s==1
def super(n):
    while len(str(n)) != 1 and premier(n) == True:
        n = n // 10
    return(premier(n))
def afficher(T,n):
    for i in range(n):
        if super(T[i]) == True:
            print(T[i])
n = saisir()
T = np.array([int]*n)
remplir(T,n)
afficher(T,n)
