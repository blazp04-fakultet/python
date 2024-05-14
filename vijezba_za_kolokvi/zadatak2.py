# Generiraj niz od 5 imena i 5 prezimena i 5 godina te ih konvertiraj ih u uređeni par ime, prezime, godina.

import random

lista_imena:list = ["Blaz", "Ante", "Ana","Ivana","Mila","Slavica","Antonio"]
lista_prezimena:list = ["Peric","Juric","Jakeljic","Bosnjak","Matic","Jurisic","Maric"]

lista_osoba:list = []
uredjeni_par: list = []

for i in range(5):
    indexIme:int = random.randint(0,len(lista_imena))
    indexPrezime:int = random.randint(0,len(lista_prezimena))

    ime:str = lista_imena[indexIme-1]
    prezime:str = lista_prezimena[indexPrezime-1]
    godine:int = random.randint(0,100)

    uredjeni_par.append((ime, prezime, godine))

    osoba:dict = {
        "Ime" : ime,
        "Prezime" : prezime,
        "Godine": godine
    }
    lista_osoba.append(osoba)


print(uredjeni_par)

