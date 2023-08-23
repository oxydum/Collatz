# Collatz by JBF aka oxydum

from math import sqrt
import random

Hauteur = 1
H = 1

def collatz(num):
    global Hauteur
    global NbPair
    global NbImpair
    if num == 1:
        return ""
    if num % 2 == 0:
        NbPair = NbPair + 1
        Z = num // 2
        return collatz(Z)
    A = 3 * num + 1
    NbImpair = NbImpair + 1
    if Hauteur < A: Hauteur = A
    return collatz(A)

# Main
for i in range(3,20000,2):
  NbPair = 0
  NbImpair = 0
  c = collatz (i)
  if H < Hauteur : 
    H = Hauteur
    print ("Collatz(" +str(i)+ ")", end=' ')
    print ("Durée:" +str(NbPair+NbImpair)+ " Pair:"+str(NbPair)+""+" Impair:"+str(NbImpair)+"", end=' ')
    print (str(c)+"H:["+str(Hauteur)+"] " )

