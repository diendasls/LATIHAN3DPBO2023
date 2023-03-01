from Mahasiswa import Mahasiswa

# class ProgramStudi sebagai COMPOSITE CLASS dari Mahasiswa
class ProgramStudi(Mahasiswa):

    def __init__(self) :
    # constructor
        self.nama_prodi = ""
        self.kode = ""
        self.course = ""

    # setter & getter

    # NAMA PRODI
    def setNamaProdi(self, nama_prodi):
        self.nama_prodi = nama_prodi # set nilai atribut nama_prodi
    
    def getNamaProdi(self):
        return self.nama_prodi # mengembalikan nilai atribut nama_prodi

    # KODE
    def setKode(self, kode):
        self.kode = kode # set nilai atribut kode

    def getKode(self):
        return self.kode # mengembalikan nilai atribut kode

    # COURSE
    def setCourse(self, course):
        self.course = course # set nilai atribut course

    def getCourse(self):
        return self.course # mengembalikan nilai atribut course
    
