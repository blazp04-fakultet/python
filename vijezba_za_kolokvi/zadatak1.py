# Napisati program koji broji broj slova u tekstu koristeci rječnike.
# Ključevi rječnika su slova, a vrijednosti broj ponavljanja.

# Provjeriti pojavljuju li se u tekstu engleski znakovi (x, y, w) ili brojevi.

# Iz rječnika dohvatiti uređene parove slova i broj ponavljanja te iterirati kroz for petlju i ispisati.

import re

def provjera_xyz(text):
    pattern = r'[xyz]'
    return bool(re.search(pattern, text))


# text: str = "Convert text to speech online for free with our AI voice generator. Create natural AI voices instantly in any language - perfect for video creators, developers, and businesses."
text:str = "Ja sam mali blaz"
slova: dict = {}
for s in text:
    if  s in slova:
        slova[s] += 1
    else:
        slova[s] = 1


if(provjera_xyz(text)):
    print("Rijec ima slovo x,y ili z")
else:
    print(slova.items())

        
