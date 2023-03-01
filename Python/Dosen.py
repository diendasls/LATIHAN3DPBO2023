from SivitasAkademik import SivitasAkademik

# class Dosen sebagai child (subclass) dari SivitasAkademik (derived class 3)
class Dosen(SivitasAkademik):

    def __init__(self) :
    # constructor
        self.nip = ""
        self.fakultas = ""
        self.pend_terakhir = ""
        self.keahlian = ""
        

    # setter & getter

    # NIP
    def setNip(self, nip):
        self.nip = nip # set nilai atribut nip
    
    def getNip(self):
        return self.nip # mengembalikan nilai atribut nip

    # FAKULTAS
    def setFakultas(self, fakultas):
        self.fakultas = fakultas # set nilai atribut fakultas

    def getFakultas(self):
        return self.fakultas # mengembalikan nilai atribut fakultas

    # PENDIDIKAN TERAKHIR
    def setPendTerakhir(self, pend_terakhir):
        self.pend_terakhir = pend_terakhir # set nilai atribut pend_terakhir

    def getPendTerakhir(self):
        return self.pend_terakhir # mengembalikan nilai atribut pend_terakhir
    
    # KEAHLIAN
    def setKeahlian(self, keahlian):
        self.keahlian = keahlian # set nilai atribut keahlian

    def getKeahlian(self):
        return self.keahlian # mengembalikan nilai atribut keahlian
    
