# pendaftaran.py

pendaftaran_list = []

def daftar_organisasi(nama, organisasi):
    pendaftaran_list.append({"nama": nama, "organisasi": organisasi})
    print(f"{nama} berhasil mendaftar ke {organisasi}.")

def tampilkan_pendaftar():
    print("\n--- Daftar Pendaftar ---")
    if not pendaftaran_list:
        print("Belum ada pendaftar.")
    else:
        for idx, p in enumerate(pendaftaran_list, 1):
            print(f"{idx}. {p['nama']} - {p['organisasi']}")
