riwayat_tindakan = []

def tambah_rekam_medis(data_pasien):
    id_pasien = input("Masukkan ID pasien yang dicari = ").strip().upper().replace(" ", "")
    if id_pasien in data_pasien:
       diagnosa = input("Masukkan Diagnosa = ")
       #diisi angka pun masih bisa
       tindakan = input("Masukkan Tindakan = ")
       #diisi angka pun masih bisa.
       resep = input("Masukkan Resep = ")

       rekam_medis_baru = {
        "diagnosa": diagnosa,
        "tindakan": tindakan,
        "resep": resep,
       }

       data_pasien[id_pasien].rekam_medis.append(rekam_medis_baru)
       riwayat_tindakan.append(id_pasien)

       print("Rekam medis berhasil ditambahkan")
       print(data_pasien)
    else:
        print("Pasien Tidak Ditemukan!")


def undo_tindakan(data_pasien):
    if not riwayat_tindakan:
        print("Tidak ada tindakan yang bisa dibatalkan!")
        return

    id_pasien = riwayat_tindakan.pop()

    if id_pasien in data_pasien and data_pasien[id_pasien].rekam_medis:
        data_pasien[id_pasien].rekam_medis.pop()
        print(f"Tindakan terakhir pasien {id_pasien} berhasil dibatalkan!")
    else:
        print("Data pasien tidak ditemukan.")


def lihat_rekam_medis(data_pasien):
    id_pasien = input("Masukkan ID Pasien yang dicari = ").strip().upper().replace(" ","")
    if id_pasien in data_pasien:

        lihat_rekam = data_pasien[id_pasien].rekam_medis
        if len(lihat_rekam) == 0:
          print("Belum ada rekam medis!")

        else:
            for item in lihat_rekam:
                print("=====Rekam Medis Pasien=====")
                print("Diagnosa", item["diagnosa"])
                print("Tindakan", item["tindakan"])
                print("Resep", item["resep"])
                
    else:
        print("Pasien Tidak ditemukan!")