#Python 120


#Muuttuja tallennetaan tietokoneen muistiin.
#Siihen voidaan viitata
"""
muuttujaA = 1234
muuttujaB = 5678

print(id(muuttujaA))
print(id(muuttujaB))

muuttujaA = 1111

muuttujaC = muuttujaA

muuttujaA = 2222

print(muuttujaC)
print(id(muuttujaA))
print(id(muuttujaC))

muuttujaA = [1,2,3,4]
muuttujaB = muuttujaA

muuttujaA[0] = 111
muuttujaB[1] = 222
print(muuttujaA)
print(muuttujaB)
"""
# listan kopiointi

listaA = [1, 2, 3, 4]

listaB = []
for elementti in listaA:
    listaB.append(elementti)

# lista menee viittauksena funktion parametriksi

def funktio(lista:list):
	lista.append(1234)

def funktio2(lista:list) -> list:
	uusi = lista[:]
	uusi.append(1111)
	return uusi
	
funktio(listaA)
print(listaA)

tulos = funktio2(listaA)
print(tulos) 


#Tehtävä 120-1: Tee funktio, joka palauttaa parametrina annetun listan arvot kerrottuna kahdella.

def kertaakaksi(lista:list) -> list:
    uusi = []
    for elementti in lista:
        uusi.append(elementti*2)
    return uusi

lista = [1,2,3,4]
print(kertaakaksi(lista))



#Tehtävä 120-2: Tee funktio, joka poistaa parametrina annetun listan pienimmän arvon.
def poistapienin(lista:list):
    lista.remove(min(lista))

lista = [1,2,3,4]
poistapienin(lista)
print(lista)

#Tehtävä 120-3: Tee funktio, joka kääntää 3x3 matriisin.
#1 2 3		1 4 7
#4 5 6  --> 	2 5 8
#7 8 9		3 6 9

#Tehtävä 120-4: Tee ohjelma, jolla lasketaan risti-nolla...

