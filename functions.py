#class, function
class iden:
    def __init__(iden, kelompok, shift):
        iden.kelompok = kelompok
        iden.shift = shift
    def identitas(iden):
        print(f"Kelompok = {iden.kelompok}\nShift = {iden.shift}")

class nama:
    def __init__(nama, nama1,nama2,nama3,nama4):
        nama.nama1 = nama1
        nama.nama2 = nama2
        nama.nama3 = nama3
        nama.nama4 = nama4
    def anggota(nama):
        print(f"Anggota 1 = {nama.nama1}\nAnggota 2 = {nama.nama2}\nAnggota 3 = {nama.nama3}\nAnggota 4 = {nama.nama4}")


class Ac:
    def __init__(self, suhu,iden):
        self.suhu = suhu
    def ubah(suhu):
        print(f"Suhu ruangan berhasil diubah ke {suhu}°C")




