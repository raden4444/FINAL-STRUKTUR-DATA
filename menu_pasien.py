data_pasien = {}
import re

class Pasien:
    def __init__(self, id_pasien, nama, usia, keluhan, tingkat_urgensi):
        self.id_pasien = id_pasien
        self.nama = nama
        self.usia = usia
        self.keluhan = keluhan
        self.tingkat_urgensi = tingkat_urgensi
        self.rekam_medis = []

    def tampilkan_data(self):
        print("===== DATA PASIEN =====")
        print("ID      :", self.id_pasien)
        print("Nama    :", self.nama)
        print("Usia    :", self.usia)
        print("Keluhan :", self.keluhan)
        print("Urgensi :", self.tingkat_urgensi)

def tambah_pasien():

    while True:
        id_pasien = (input("Masukkan ID Pasien = ")).strip().upper()
        if id_pasien == "":
           print("ID pasien tidak boleh kosong")
        elif id_pasien in data_pasien:
           print("ID pasien sudah digunakan!")
        elif not re.match(r'^P\d{3}$', id_pasien):
            print("Format ID salah! Harus berupa 'P' diikuti 3 digit angka (Contoh: P001)")
        else:
           break

    while True:      
        Nama = input("Masukkan Nama = ")
        if Nama != "":
            break
        print ("Nama tidak boleh kosong")
    
    while True:
        try:
            Usia = int(input("Masukkan Usia Pasien = "))
            break
        except ValueError:
            print("Usia harus berupa angka")
    
    while True:
        Keluhan = input("Masukkan Keluhan = ")
        if Keluhan != "":
            break
        print("Keluhan harus diisi")
    
    while True:
        tingkat_urgensi = input("Tingkat urgensi (rendah/tinggi )= ").strip().upper().replace(" ","")
        if tingkat_urgensi == "TINGGI" or tingkat_urgensi == "RENDAH":
            break
        else:
            print("Jawaban tidak valid!")
    
    data_pasien[id_pasien] = Pasien(
        id_pasien,
        Nama,
        Usia,
        Keluhan,
        tingkat_urgensi.capitalize()
    )

    print("Pasien berhasil ditambahkan")

def cari_pasien():

    if not data_pasien:
        print("Belum ada data pasien.")
        return

    while True:
        cari = input("Masukkan ID pasien yang dicari = ").strip().upper().replace(" ", "")

        if cari in data_pasien:
            pasien = data_pasien[cari]
            pasien.tampilkan_data()
            break

        else:
            print("Pasien tidak ditemukan, coba lagi.")

def hapus_pasien():
    
    print(data_pasien)
    id_hapus = (input("Masukkan id yang ingin dihapus : ")).strip().upper().replace(" ", "")

    if id_hapus in data_pasien:
      del data_pasien[id_hapus]
      print("Data berhasil dihapus")

    else:
        print("Pasien tidak ditemukan")

def update_pasien():
    id_update = input("Masukkan ID pasien yang ingin diubah = ").strip().upper().replace(" ", "")
    if id_update in data_pasien:
        pasien = data_pasien[id_update]
        print("===== DATA LAMA =====")
        print("Nama     :", pasien.nama)
        print("Usia     :", pasien.usia)
        print("Keluhan  :", pasien.keluhan)
       
    
        print("===== MASUKKAN DATA BARU =====")
        
        while True:
            nama_baru = input("Masukkan Nama Baru = ")
            if nama_baru != "":
                break
            print ("Nama tidak boleh kosong")
            
        while True:
            try:
                usia_baru = int(input("Masukkan Usia Baru = "))
            except ValueError:
                print("Usia harus angka")
                continue
            keluhan_baru = input("Masukkan Keluhan Baru = ")
            break

        pasien.nama = nama_baru
        pasien.usia = usia_baru
        pasien.keluhan = keluhan_baru

        print("Data pasien berhasil diupdate")

        print("DEBUG DATA:")
        print(data_pasien)

    else:
        print("Pasien tidak ditemukan")  
