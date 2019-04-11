from random import randint
a=randint(0, 9)
x=input("saisir un chiffre compris entre 0 et 9")
if int(a)==int(x):
   print ("bravo,vous avez gagné")
else:
   print ("desolé , c'est raté")  
