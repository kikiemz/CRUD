import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_os = os.name
    match sistem_os:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
        

    print("CONTOH SEDERHANA PROGRAM CRUD")
    print("DATABASE PERPUSTAKAAN")
    print("\n"+"="*100+"\n")

    CRUD.init_console()

    while True:
        match sistem_os:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        

        print("CONTOH SEDERHANA PROGRAM CRUD")
        print("DATABASE PERPUSTAKAAN")
        print("\n"+"="*100+"\n")

        print("1.Baca Judul Buku")
        print("2.Buat Judul Buku")
        print("3.Update Buku")
        print("4.Hapus Buku\n")

        pilihan_menu = input("Pilih Menu yang di inginkan: ")

        match pilihan_menu:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": print("4.Hapus Buku")

        lanjut = input("Apakah ingin ke menu utama (y/n): ")
        if lanjut != "y":
            break