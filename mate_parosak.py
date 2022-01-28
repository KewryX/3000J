class Tanulo:
    lista = []
    def __init__(self, tanulokod, nev, micsop, acsop, mnyelv,nem,egyuttlakok,testverszama):
        self.tanulokod = tanulokod
        self.nev = nev
        self.micsop = micsop
        self.acsop = acsop
        self.mnyelv = mnyelv
        self.nem = nem
        self.egyuttlakok = egyuttlakok
        self.testverszama = testverszama
        Tanulo.lista.append(self)


with open("J.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split(";")
        t = Tanulo(int(s[0]),s[1],s[2],s[3],s[4],s[5],int(s[6]),int(s[7]))


#2) Hány fiú tanul az osztályban?
def fiuk(lista):
    
    print("2) Hány fiú tanul az osztályban?")
    x = 0
    for e in lista:
        if e.nem == "F":
            x += 1

#4) Hány olyan diák van, akiknek több mint 1 testvére van!
def tobb_mint_1_testver(lista):
    print("4) Hány olyan diák van, akiknek több mint 1 testvére van!")
    x = 0
    for e in lista:
        if e.testverszam > 1:
            x +=1

#6) Hány olyan diák van, akiknek több mint 2 testvére van!
def tobb_mint_1_testver(lista):
    print("6) Hány olyan diák van, akiknek több mint 2 testvére van!")
    x = 0
    for e in lista:
        if e.testverszam > 2:
            x +=1

#8) Hány olyan diák van, akik a 2. idegen nyelvként a németet tanulják!
def masodik_nyelv_nemet(lista):
    print("8) Hány olyan diák van, akik a 2. idegen nyelvként a németet tanulják!")
    x = 0
    for e in lista:
        if e.mnyelv == "német":
            x +=1


