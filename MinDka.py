#Simulator Minimizacije DKA
import sys
import re

#dohvacanje definicije simulatora
definicija = []
for line in sys.stdin.readlines():
    line = line.strip()
    if(len(line) > 0):
        definicija.append(line)


stanja = definicija[0]
abeceda = definicija[1];
prihvatljivaStanja = definicija[2];
pocetnoStanje = definicija[3];

#obrada definicije
stanja = stanja.split(",")
abeceda = abeceda.split(",")
prihvatljivaStanja = prihvatljivaStanja.split(",")

#funkcije prijelaza

prijelazi = dict()

for line in range(len(definicija)-4):
    prijelaz = definicija[line+4].split("->")
    prviDio = prijelaz[0]
    drugiDio = prijelaz[1]
    prviDio = prviDio.split(",")

    promjena = dict()
    if( prviDio[0] in prijelazi ):
        promjena = prijelazi.get(prviDio[0])
    promjena[prviDio[1]] = drugiDio
    prijelazi[prviDio[0]] = promjena

#dohvat dohvatljivih stanja
dohvatljivaStanja = []
dohvatljivaStanja.append(pocetnoStanje)
petlja = True
brojac = 0

while(petlja):
    promjena = dict()
    if(dohvatljivaStanja[brojac] in prijelazi):
        promjena = prijelazi.get(dohvatljivaStanja[brojac])
        for znak in abeceda:
            if(znak in promjena):
                simbol = promjena.get(znak)
                if(simbol not in dohvatljivaStanja):
                    dohvatljivaStanja.append(simbol)
    brojac+=1
    if(len(dohvatljivaStanja) == brojac):
        petlja = False

dohvatljivaStanja.sort()
    
#trazenje istovjetnosti
def trazenjeIstovjetnosti(stanja,trenutnaStanja,prijelazi):
    listePrijelaza = []
    promjena = dict()

    if(len(stanja) == 1):
        return stanja

    for stanje in stanja:
        lista = []
        if(stanje in prijelazi):
            promjena = prijelazi.get(stanje)
            for znak in abeceda:
                if(znak in promjena):
                    sljedeceStanje = promjena.get(znak)
                    for i in range(len(trenutnaStanja)):
                        kraj = False
                        if(kraj):
                            break
                        for ostalaStanja in trenutnaStanja[i]:
                            if(sljedeceStanje == ostalaStanja):
                                lista.append(i)
                                kraj = True
        
        listePrijelaza.append(lista)

    novaLista = []
    for i in range(len(listePrijelaza)):
        lista = []
        p = True
        for k in range(len(novaLista)):
            if(stanja[i] in novaLista[k]):
                p = False
                break
        if(p):
            lista.append(stanja[i])
        for j in range(i+1,len(listePrijelaza)):
            if(listePrijelaza[i] == listePrijelaza[j]):
                dalje = True
                for k in range(len(novaLista)):
                    if(stanja[j] in novaLista[k]):
                        dalje = False
                        break
                if(dalje):
                    lista.append(stanja[j])
        if(len(lista) != 0):
            novaLista.append(lista)
    return novaLista
                


#dobivanje istovjetnih stanja

#G11 su sva neprihvatljiva stanja,a G12 sva prihvatljiva stanja
G11 = []
G12 = []
for stanje in dohvatljivaStanja:
    if(stanje in prihvatljivaStanja):
        G12.append(stanje)
    else:
        G11.append(stanje)

#spajam G11 i G12 u jednu listu ( G11 i G12 su dalje liste)
trenutnaStanja = []
trenutnaStanja.append(G11)
trenutnaStanja.append(G12)


algoritam = True
while(algoritam):
    sljedecaStanja = []
    for stanja in trenutnaStanja:
        novaStanja = trazenjeIstovjetnosti(stanja,trenutnaStanja,prijelazi)
        if(novaStanja == stanja):
            sljedecaStanja.append(stanja)
        else:
            for i in range(len(novaStanja)):
                sljedecaStanja.append(novaStanja[i])
    if(sljedecaStanja == trenutnaStanja):
        break
    trenutnaStanja = sljedecaStanja
    


#ispis minimiziranog Dka
minUlaznaStanja = []
for i in range(len(sljedecaStanja)):
    stanja = sljedecaStanja[i]
    stanja.sort()
    if(len(stanja) != 0):
        minUlaznaStanja.append(stanja[0])
minUlaznaStanja.sort()
for i in range(len(minUlaznaStanja)):
    if(i+1 != len(minUlaznaStanja)):
        print(minUlaznaStanja[i]+',',end='')
    else:
        print(minUlaznaStanja[i])


for i in range(len(abeceda)):
    if(i+1 != len(abeceda)):
        print(abeceda[i]+',',end='')
    else:
        print(abeceda[i])

ispis = ''
for i in range(len(prihvatljivaStanja)):
    if(prihvatljivaStanja[i] in minUlaznaStanja):
        ispis += prihvatljivaStanja[i]+','
print(ispis[:-1])


if(pocetnoStanje in minUlaznaStanja):
    print(pocetnoStanje)
else:
    for stanja in sljedecaStanja:
        if(pocetnoStanje in stanja):
            print(stanja[0])
            break

    
promjena = dict()
for stanje in minUlaznaStanja:
    if(stanje in prijelazi):
        promjena = prijelazi.get(stanje)
        for znak in abeceda:
            ispis = ''
            ispis += stanje
            if(znak in promjena):
                sljedeceStanje = promjena.get(znak)
                if(sljedeceStanje in minUlaznaStanja):
                    ispis += ','+znak+'->'+sljedeceStanje
                else:
                    for stanja in sljedecaStanja:
                        if(sljedeceStanje in stanja):
                            ispis += ','+znak+'->'+stanja[0]
                            break
                print(ispis)

                
                
    
    
        


