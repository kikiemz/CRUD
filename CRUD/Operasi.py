import time
from . import Database
from .Utils import kocok

def update(no_buku,pk,date_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + Database.TEMPLATE["judul"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    panjang_data = len(data_str)

    try: 
        with open(Database.DB_NAME,'r+',encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)

    except Exception as e:
        print(f"Eror dalam update data {e}")


def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = kocok(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["judul"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Muka anda jelek makanya eror : {e}")


def create_first_data():
    penulis = input("Masukan Nama Penulis : ")
    judul = input("Masukan Nama Judul : ")
    while True:
        try:
            tahun = int(input("Masukan Tahun\t:"))
            if len(str(tahun)) == 4:
                break
            else:
                print(f"Harap Masukan Tahun 4 angka")
        except Exception as e:
            print(f"Harap Masukan Angka {e}")

    data = Database.TEMPLATE.copy()

    data["pk"] = kocok(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["judul"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Muka anda jelek makanya eror : {e}")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r") as file:
            konten = file.readlines()
            jumlah_konten = len(konten)
            if "index" in kwargs:
                index_buku = kwargs["index"]
                if index_buku < 0 or index_buku > jumlah_konten:
                    return False
                else:
                    return konten[index_buku]
            else:
                return konten
    except Exception as e:
        print(f"Membaca Database Eror {e}")
        return False
