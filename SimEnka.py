#epsilon-NKA simulator
import sys
import re


#dohvacanje definicije simulatora
definicija = []
for line in sys.stdin.readlines():
    line = line.strip()
    if(len(line) > 0):
        definicija.append(line)
    


ulazniNizovi = definicija[0]
stanja = definicija[1]
abeceda = definicija[2]
prihvatljivaStanja = definicija[3]
pocetnoStanje = definicija[4]

#funkcija ispisa
def funkcijaIspisa(stanja):
    ispis = ""
    for i in range(len(stanja)):
        ispis += stanja[i]
        if(i < len(stanja)-1):
            ispis += ","
    ispis += "|"
    return ispis


#obrada definicije
ulazniNizovi = ulazniNizovi.split("|")
stanja = stanja.split(",")
abeceda = abeceda.split(",")
prihvatljivaStanja = prihvatljivaStanja.split(",")


#dohvacanje funkcije prijelaza
prijelazi = dict()

for line in range(len(definicija)-5):
    prijelaz = definicija[line+5].split("->")
    prviDio = prijelaz[0]
    drugiDio = prijelaz[1]
    prviDio = prviDio.split(",")
    drugiDio = drugiDio.split(",")
    
    promjena = dict()
    if( prviDio[0] in prijelazi ):
        promjena = prijelazi.get(prviDio[0])
    promjena[prviDio[1]] = drugiDio
    prijelazi[prviDio[0]] = promjena


#dobivanje novih vrijednosti
def epsilonOkruzenje(stanja,prijelazi):
    epsilon = True
    brojac = 0
    trenutnoStanje = []
    trenutnoStanje = stanja
    while(epsilon):
        if(trenutnoStanje[brojac] != "#"):
            if(trenutnoStanje[brojac] in prijelazi):
                promjena = dict()
                promjena = prijelazi.get(trenutnoStanje[brojac])
                if("$" in promjena):
                    for i in range(len(promjena.get("$"))):
                        if(promjena.get("$")[i] not in trenutnoStanje):
                             trenutnoStanje.append(promjena.get("$")[i])
                        a = set(trenutnoStanje) 
                        if(len(a) != len(trenutnoStanje)):
                           epsilon = False
        if(brojac == len(trenutnoStanje)-1):
            epsilon = False
        brojac = brojac+1
    trenutnoStanje.sort()
    return trenutnoStanje

def znakOkruzenje(stanja,prijelazi,niz):
    prijelaz = True
    brojac = 0
    novaStanja = []
    svaStanja = []
    trenutnoStanje = []
    trenutnoStanje = stanja
    while(prijelaz):
        if(trenutnoStanje[brojac] != "#"):
            if(trenutnoStanje[brojac] in prijelazi):
                promjena = dict()
                promjena = prijelazi.get(trenutnoStanje[brojac])
                if(niz in promjena):
                    for i in range(len(promjena.get(niz))):
                        if(promjena.get(niz)[i] not in novaStanja):
                            novaStanja.append(promjena.get(niz)[i])
                    svaStanja = epsilonOkruzenje(novaStanja,prijelazi)
                else:
                    if("#" not in svaStanja):
                        svaStanja.append("#")
        if(brojac == len(trenutnoStanje)-1):
            prijelaz = False
        brojac = brojac+1
    svaStanja.sort()
    return svaStanja
                                                             
for i in range(len(ulazniNizovi)):
    print(i)
    listaIspisa = []
    niz = ulazniNizovi[i].split(",")
    lista = []
    lista.append(pocetnoStanje)
    trenutnaStanja = epsilonOkruzenje(lista,prijelazi)    
    ispis = ""
    ispis += funkcijaIspisa(trenutnaStanja)
    privremenaStanja = []
    for i in range(len(niz)):
        trenutnaStanja = znakOkruzenje(trenutnaStanja,prijelazi,niz[i])
        if(len(trenutnaStanja) == 0):
            trenutnaStanja.append("#")
        if(len(trenutnaStanja) > 1 and "#" in trenutnaStanja):
            trenutnaStanja.remove("#")
        ispis += funkcijaIspisa(trenutnaStanja)
    ispis = ispis[:-1]
    listaIspisa.append(ispis)

for i in range(len(listaIspisa)):
    print(listaIspisa[i])
            
            
           
        
    

    

    
