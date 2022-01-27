from cmath import tan


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
    
for t in Tanulo.lista:
    print(t.nev)
    
print(len(Tanulo.lista))