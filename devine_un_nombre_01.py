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
			j=int(input("entrer un nombre plus petit  que {0}".format(j))
			liste.append(j)
		else :
			j=int(input("entrer un nombre plus grand que {0}".format(j))
			liste.append(j)

	print ("Bravo vous avez reussi au bout de {0} tentative(s)".format(len(liste)))
	liste.sort(reverse=True)

	print (liste)

except ValueError:
	print('Vous n\'avez pas saisi un entier')


