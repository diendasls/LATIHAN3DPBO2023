from Mahasiswa import Mahasiswa

# class Course sebagai COMPOSITE CLASS dari Mahasiswa
class Course(Mahasiswa):

    def __init__(self) :
    # constructor
        self.nama_matakuliah = ""

    # setter & getter

    # NAMA MATA KULIAH
    def setNamaProdi(self, nama_matakuliah):
        self.nama_matakuliah = nama_matakuliah # set nilai atribut nama_matakuliah
    
    def getNamaProdi(self):
        return self.nama_matakuliah # mengembalikan nilai atribut nama_matakuliah
