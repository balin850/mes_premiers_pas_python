import random
n=random.randint(0,100)

#La ligne ci-dessous est à commenter si on veut jouer à ce jeu passionant
print (n)

try:
	j=int(input("entrer un nombre compris entre 0 et 100 : "))
	liste = []
	liste.append (j)

	while j != n :
		if j > n :
			j=int(input("entrer un nombre plus petit  que " + str(j) + " : "))
			liste.append(j)
		else :
			j=int(input("entrer un nombre plus grand que " + str(j) + " : "))
			liste.append(j)

	print ("Bravo vous avez reussi au bout de " + str(len(liste)) + " tentative(s)")
	liste.sort(reverse=True)

	print (liste)

except ValueError:
	print('Vous n\'avez pas saisi un entier')


