#!/bin/python3
# coding: utf-8
a=4
b=1
modulo=503
couple = []
listex_gen =[]
listey_gen =[]
caracteres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
print (caracteres)
nbre_carac=len(caracteres)


def euclide_etendu(e, phi_n, val) :
	d = 1
	temp = (e*d)%phi_n
	while(temp != val):
		d = d+1
		temp = (e*d)%phi_n
	return d

for x in range (1, modulo-1):
	for y in range (1, modulo-1):
		partie_gauche= (y**2)%modulo
		partie_droite= ((x**3)+(a*x)+b)%modulo		
		
		if(partie_gauche == partie_droite):
			listex_gen.append(x)
			listey_gen.append(y)
			#print (x,y)
			#print(listex)
			#print(listey)
for x,y in zip (listex_gen,listey_gen):
	temp= (x,y)
	couple.append(temp)
print(couple)
print(len(couple))
""" ordre_avant=2*modulo
ordre_choisi=2*modulo

for i in range(len(couple)):
	listex =[]
	listey =[]
	points=[]
	gen= (couple[i])
	print(gen)
	x1=gen[0]
	#print(x1)
	y1=gen[1]
	# print(y1)
	
	listex.append(x1)
	listey.append(y1)
	# print(listex)
	# print(listey)

	val=((3*x1**2)+a)%modulo
	e=(2*y1)%modulo

	lambda3 = euclide_etendu(e, modulo, val)
	# print(lambda3)

	x3=((lambda3**2)-2*x1)%modulo
	y3=(lambda3*(x1-x3)-y1)%modulo

	# print("x3",x3)
	# print("y3", y3)
	listex.append(x3)
	listey.append(y3)
	
	# print(listex)
	# print(listey)
	tempo=0
	# Calculer tous les autres alpha
	if x3 == x1:
		tempo=1
	while tempo!=1:
		x2=x3
		y2=y3
		val1=(y2-y1)%modulo
		e1=(x2-x1)%modulo
		lambda1 = euclide_etendu(e1, modulo, val1)
		x3=((lambda1**2)-x1-x2)%modulo
		y3=(lambda1*(x1-x3)-y1)%modulo
		# print("x3",x3)
		# print("y3", y3)
		if x3 == x1:
			listex.append(x3)
			listey.append(y3)
			tempo=1
		else:
			listex.append(x3)
			listey.append(y3)
			#x2=x3
			#y2=y3

	# print(listex)
	# print(listey)
	for x,y in zip (listex,listey):
		temp= (x,y)
		points.append(temp)
	# print points
	
	#Ordre 
	ordre = len(points)
	print(ordre)
	print('----------')
	#Meilleur ordre en fonction du nombre de caractere
	if((ordre>nbre_carac) and (ordre<ordre_avant) and (ordre<ordre_choisi) ):
		print(ordre)
		ordre_choisi=ordre
		#Meilleur generateur en focntion de l'ordre
		generateur=points[i]
	ordre_avant=ordre
	print(ordre_avant)
#ordre  choisi en fontion de tous les ordres
print(ordre_choisi)
#le generateur choisi
print(generateur)

							# Alpha + Alpha avec le meilleur generateur
listex=[]
listey=[]

#Affectation de x1 et y1 avec le generateur
x1=generateur[0]
print(x1)
y1=generateur[1]
print(y1)
listex.append(x1)
listey.append(y1)
val=((3*x1**2)+a)%modulo
phi_n=37
e=2*y1%modulo

#calcul de lamba, x3 et y3

lambda3 = euclide_etendu(e, modulo, val)
# print(lambda3)

x3=((lambda3**2)-2*x1)%modulo
y3=(lambda3*(x1-x3)-y1)%modulo

print("x3",x3)
print("y3", y3)

listex.append(x3)
listey.append(y3)
print(listex)
print(listey)

					# 2Alpha + Alpha avec le meilleur generateur

tempo=0
# Calculer tous les autres alpha
while tempo!=1:
	x2=x3
	y2=y3
	val1=(y2-y1)%modulo
	e1=(x2-x1)%modulo
	lambda1 = euclide_etendu(e1, modulo, val1)
	x3=((lambda1**2)-x1-x2)%modulo
	y3=(lambda1*(x1-x3)-y1)%modulo
	print("x3",x3)
	print("y3", y3)
	if x3 == x1:
		listex.append(x3)
		listey.append(y3)
		tempo=1
	else:
		listex.append(x3)
		listey.append(y3)
		#x2=x3
		#y2=y3

# print(listex)
# print(listey)
couple=[]
for x,y in zip (listex,listey):
	temp= (x,y)
	couple.append(temp)
print(couple)


#Cryptage
def chiffrer(m):
	k=7
	key_private=73
	message = m
	print("Message a chiffrer", message)
	y1=couple[(k-1)%ordre_choisi]
	print(y1)
	y2=couple.index(message)+((k-1)+(key_private-1))
	y2=couple[y2%ordre_choisi]
	print("message chiffre", y1,y2)
	return (y1,y2)

#DeCryptage
def dechiffrer():
	dec = (couple.index(y2)-(key_private-1)+couple.index(y1))%ordre_choisi
	print("message dechiffre:", couple[dec])
	return couple[dec]

#Cryptage chaine de caractere
print("cryptage caractere")
message2 = "salut"
message_chiffrer = []
message_dechiffrer = []
for char in message2:
	print (char)
	x=caracteres.index(char)
	print(x)
	nombre=couple[x]
	print(nombre)
	
	message_chiffrer.append(chiffrer(nombre))
	

print(message_chiffrer)

#nombre = couple.index(message)
#print(nombre)
#print(caracteres[nombre]) """








		

				
