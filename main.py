# main.py

from menu import tampilkan_menu
from organisasi import lihat_daftar_organisasi, informasi_organisasi, organisasi_list
from pendaftaran import daftar_organisasi, tampilkan_pendaftar

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            lihat_daftar_organisasi()
        elif pilihan == '2':
            nama_org = input("Masukkan nama organisasi: ")
            informasi_organisasi(nama_org)
        elif pilihan == '3':
            nama = input("Masukkan nama Anda: ")
            org = input("Masukkan nama organisasi yang ingin didaftar: ")
            if org in organisasi_list:
                daftar_organisasi(nama, org)
            else:
                print("Organisasi tidak ditemukan.")
        elif pilihan == '4':
            tampilkan_pendaftar()
        elif pilihan == '5':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
