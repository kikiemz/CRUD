from . import Operasi

def delete_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang akan di hapus")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            print("WARNING !!!\nDATA INI AKAN TERHAPUS   ")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            lanjut = input("Apkah anda benar ingin menghapus? (y/n)\t: ")
            if lanjut == "y":
                Operasi.delete(no_buku)
                break
        else:
            print("nomor tidak valid, silahkan masukan lagi")
    

def update_console():
    read_console()
    while True:
        try:
            print("Silahkan pilih nomor buku yang akan di update")
            no_buku = int(input("Nomor Buku: "))
            data_buku = Operasi.read(index=no_buku)

            if data_buku:
                break
            else:
                print("nomor tidak valid, silahkan masukan lagi")
        except Exception as e:
            print(f"Eror Harap Masukan Nomer yang Valid")

    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while True :
        # data yang ingin diupdate
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":   
                    while True:
                        try:
                            tahun = int(input("Masukan Tahun\t:"))
                            if len(str(tahun)) == 4:
                                break
                            else:
                                print(f"Harap Masukan Tahun 4 angka")
                        except Exception as e:
                            print(f"Harap Masukan Angka {e}")
            case _: print("Nomer yang anda pilih tidak ada")
            
        print("INI DATA BARU ANDA")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        lanjut = input("Apkah ingin lanjut mengedit? (y/n)\t: ")
        if lanjut != "y":
            break

    Operasi.update(no_buku,pk,date_add,tahun,judul,penulis)

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan Tambhakan Buku Yang Di Inginkan")
    penulis = input("Masukan Nama Penulis\t:")
    judul = input("Masukan Judul Buku\t:")
    while True:
        try:
            tahun = int(input("Masukan Tahun\t:"))
            if len(str(tahun)) == 4:
                break
            else:
                print(f"Harap Masukan Tahun 4 angka")
        except Exception as e:
            print(f"Harap Masukan Angka {e}")
    
    Operasi.create(tahun,judul,penulis)
    print("Ini adalah data Buku Terbaru")
    read_console()

def read_console():
    data_file = Operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("\n"+"-"*100)

    # Data
    for index,data in enumerate(data_file, start=1):
        data_pisah = data.split(",")
        pk = data_pisah[0]
        data_add = data_pisah[1]
        penulis = data_pisah[2]
        judul = data_pisah[3]
        tahun = data_pisah[4]
        print(f"{index:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    #Footer
    print("\n"+"="*100)
