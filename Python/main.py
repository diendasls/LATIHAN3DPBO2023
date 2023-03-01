#import 
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from ProgramStudi import ProgramStudi
from Course import Course

# instansiasi
mhs = Mahasiswa()
dsn = Dosen()
prd = ProgramStudi()
crs = Course()

# mengeset isi atribut mahasiswa
mhs.setNik("123456")
mhs.setAsalUniversitas("X1 University")
mhs.setEmailEdu("gyulie@x1.edu")
mhs.setNama("Wira")
mhs.setJenisKelamin("Laki-laki")
mhs.setNim("173")
mhs.setFakultas("Teknik")
mhs.setProdi("Teknik Elektro")

# set isi atribut ProgramStudi
prd.setNamaProdi["Teknik Elektro", "Teknik Informatika", "Teknik Kimia", "Sastra Inggris"]
prd.setKode["A1", "A2", "A3", "B1"]


# set isi atribut Course
prd.setCourse["Fisika Dasar", "Algoritma dan Pemrograman Dasar", "Kimia Dasar", "Linguistik"]

# # mengeset isi atribut dosen
# dsn.setNik("123456")
# dsn.setAsalUniversitas("X1 University")
# dsn.setEmailEdu("gyulie@x1.edu")
# dsn.setNama("Wira")
# dsn.setJenisKelamin("Laki-laki")
# dsn.setNip("173")
# dsn.setFakultas("Teknik")
# dsn.setPendTerakhir("Teknik Elektro")
# dsn.setKeahlian("Teknik Elektro")

# output
print("----- DATA MAHASISWA -----")

print("NIK           : " + int(mhs.getNik()))
print("ASAL UNIV     : " + str(mhs.getAsalUniversitas()))
print("EMAIL EDU     : " + str(mhs.getEmailEdu()))
print("NAMA          : " + str(mhs.getNama()))
print("JENIS KELAMIN : " + str(mhs.getJenisKelamin()))
print("NIM           : " + str(mhs.getNim()))
print("FAKULTAS      : " + str(mhs.getFakultas()))
print("PRODI         : " + str(mhs.getProdi()))

print("----- PRODI -----")
print("PRODI    : " + str(prd.getNamaProdi()))
print("KODE     : " + str(prd.getKode()))

# print("----- DATA DOSEN -----")

# print("NIK           : " + int(dsn.getNik()))
# print("ASAL UNIV     : " + str(dsn.getAsalUniversitas()))
# print("EMAIL EDU     : " + str(dsn.getEmailEdu()))
# print("NAMA          : " + str(dsn.getNama()))
# print("JENIS KELAMIN : " + str(dsn.getJenisKelamin()))
# print("NIP           : " + str(dsn.getNip()))
# print("FAKULTAS      : " + str(dsn.getFakultas()))
# print("PEND. TERAKHIR: " + str(dsn.getPendTerakhir()))
# print("KEAHLIAN      : " + str(dsn.getKeahlian()))
