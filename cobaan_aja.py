# latihan Perhitungan
# #fahrienthit to kelvin
# print("Ini Adalah Konversi Suhu Fahrienthit ke Kelvin")
# fahrienthit = float(input("masukan suhu ruangan : "))
# celcius = 5/9 * (fahrienthit - 32)
# kelvin = celcius + 273.15
# print("hasilnya dalam suhu kelvin : ",kelvin)


# #kelvin to fahrienthit
# print("Ini Adalah Konversi Suhu Kelvin ke Fahrienthit")
# kelvin = float(input("masukan suhu ruangan : "))
# celcius = kelvin - 273.15
# fahrienthit = ((9/5) * celcius) + 32
# print("hasilnya dalam suhu kelvin : ",fahrienthit)

# # kurang dari 0 lebih dari 5 lebih dari 8 kurang dari 11
# masukanAngka = float(input('masukan angka : '))
# hasilInput = (masukanAngka >= 0 and masukanAngka <= 5)
# hasilInput2 = (masukanAngka >= 8 and masukanAngka <= 11)

# hasilnya = hasilInput or hasilInput2
# print('jawaban anda benar atau tidak',hasilnya)


# import datetime as dt

# print("Masukan tanggal,bulan,tahun,lahir anda :")
# tanggal = int(input("Masukan Tanggal Lahir Anda : "))
# bulan = int(input("Masukan Bulan Lahir Anda : "))
# tahun = int(input("Masukan Tahun Lahir Anda : "))

# tanggal_lahir = dt.date(tahun,bulan,tanggal)
# print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

# hari_ini = dt.date.today()
# print(f"Hari ini tanggal {hari_ini}")
# umur_hari   = hari_ini - tanggal_lahir
# umur_tahun = umur_hari.days // 365
# umur_bulan_sisa = (umur_hari.days % 365) // 30 

# print(f"Umur anda adalah {umur_tahun} tahun , lebih {umur_bulan_sisa}  bulan")
# print(f"Anda lahir hari {tanggal_lahir:%A}")

# nama = input("siapa nama anda : ")
# if nama=="ucup" : 
#     print("kamu ganteng")
# elif nama=="otong" :
#     print("kamu otong")
# elif nama=="mario" :
#     print("kamu mario")
# else :
#     print("kamu bukan ucup otong atau mario")

# print("Masukan Perjumlahan yang kamu inginkan : ")
# angka1 = float(input("Masukan Angka Satu : "))
# operatror = input("Masukan Operatot +,-,/,x : ")
# angka2 = float(input("Masukan Angka Dua : "))

# if operatror == "+" :
#     hasil_tambah = angka1 + angka2
#     print(f"ini adalah hasil anda {hasil_tambah}")
# elif operatror == "-" :
#     hasil_kurang = angka1 - angka2
#     print(f"ini adalah hasil anda {hasil_kurang}")
# elif operatror == "x" :
#     hasil_kali = angka1 * angka2
#     print(f"ini adalah hasil anda {hasil_kali}")
# elif operatror == "/" :
#     hasil_bagi = angka1 / angka2
#     print(f"ini adalah hasil anda {hasil_bagi}")

#  for loop
# nama = range(21)

# for i in nama:
#     print("i love you")
# while

# angka = 1

# while angka < 10:
#     angka += 1
#     print(f"sugoi")

# continue pass

# nama = range(21)

# for i in nama:
#     print("i love you")
# while

# angka = 1

# while angka < 10:
#     angka += 1
#    continue # akan mengulang ke angka tanpa print yang di bawah
#     print(f"sugoi")

# pass # akan melawati tanpa eksekusi

# sisi = 10
# count = 1
#Latihan Looping Membuat  Segitiga
# for i in range(10):
#     print("*"*count)
#     count += 1

# while

# while True:
#     print("*"*count)
#     count += 1
    
#     if count > sisi:
#         break

# sisi = 10
# count = 1
# # continue

# while True:
#     # ganjil bilangan yang tidak habis dibagi dua
#     if (count%2):
#         print("*"*count)
#         count += 1
#     else:
#         # genap bilangan yang habis dibagi dua
#         count += 1
#         continue

#     if count > sisi:
#         break

# buat ketupat # (Gagal Paham)
# sisi = 10
# count = 1
# spasi = int(sisi/2)

# while True:
#     if (count%2):
#         print(" "*spasi,"+"*count)
#         spasi -= 1
#         count += 1
#     else:
#         count += 1
#         continue
#     if count > sisi:
#         break
# while True:
#     if (count%2): 
#         spasi += 1
#         print(" "*spasi,"+"*count)
#         count -= 1
#     else:
#         count -= 1
#     if count == 0:
#         break

# ------------------LIST-----------#
    

# deep copy dan copy

# angka1 = [1,2]
# angka2 = [3,4]
# gabungan = [angka1,angka2]
# print(gabungan)

# angka3 = gabungan.copy()
# print(f"addres berdeda tetapi addres \ndi list akan tetap sama \n {hex(id(gabungan[0][0]))}")
# print(f"addres berdeda tetapi addres \ndi list akan tetap sama \n {hex(id(angka3[0][0]))}")

# #deepcopy
# from copy import deepcopy

# deep_copy = deepcopy(angka3)
# print(f"addres berdeda tetapi addres \ndi list akan tetap sama \n {hex(id(angka3[0][0]))}")
# print(f"addres berdeda tetapi addres \ndi list akan tetap sama \n {hex(id(deep_copy[0][0]))}")

# import datetime
# import os
# import string
# import random

# """ Ini Adalah Pemograman Sederhana Untuk List Sebuah Mahasiswa"""

# template_mahasiswa = {
#     'nama':'nama',
#     'nim':'nim',
#     'sks_lulus':0,
#     'lahir': datetime.datetime(1111,11,11)
# }

# data_mahasiswa = {}

# while True:
# 	# os.system("cls") # untuk windows
# 	os.system("cls")
# 	print(f"{'SELAMAT DATANG':^20}")
# 	print(f"{'DATA MAHASISWA':^20}")
# 	print("-"*20)
	
# 	mahasiswa = dict.fromkeys(template_mahasiswa.keys())
# 	mahasiswa['nama'] = input("Masukan Nama Anda : ")
# 	mahasiswa['nim'] = int(input("Masukan NIM ANDA : "))
# 	mahasiswa['sks_lulus'] = int(input("Masukan SKS Anda : "))
# 	TANGGAL = int(input("Masukan Tangal Lahir Anda :" ))
# 	BULAN = int(input("Masukan Bulan Lahir Anda : "))
# 	TAHUN = int(input("Masukan Tahun Lahir Anda : "))
# 	mahasiswa['lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)
	
# 	KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
# 	data_mahasiswa.update({KEY:mahasiswa})

# 	# dari tutorial sebelumnya, hilangkan beasiswa
# 	print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
# 	print('-'*60)
	
# 	for mahasiswa in data_mahasiswa:
# 		KEY = mahasiswa
		
# 		NAMA = data_mahasiswa[KEY]['nama']
# 		NIM = data_mahasiswa[KEY]['nim']
# 		SKS = data_mahasiswa[KEY]['sks_lulus']
# 		LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")


# 	print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

# 	print("\n")
# 	is_done = input("Mau tambah lagi bro (y/n)? ")
# 	if is_done == "n":
# 		break
	
# print("\nAkhir dari program, terima kasih")

# def kuadrat(x):
#     hasil = x**5
#     return hasil
# print(kuadrat(5))

# ''' Perhitungan Luas Dan Keliling'''
# import os

# def header():
#     os.system('cls')
#     print(f"{'SELAMAT DATANG DI':^50}")
#     print(f"{'HITUNGAN LUAS DAN KELILING':^50}")

# def input_user():
#     lebar = int(input("Masukan Lebar: "))
#     panjang = int(input("Masukan Panjang: "))
#     return lebar,panjang

# def luas(lebar,panjang):
#     hasil = lebar * panjang
#     return hasil
    
# def keliling(lebar,panjang):
#     hasil = 2*(lebar + panjang)
#     return hasil

# def display_luas(pesan,isi):
#     print(f"Hasil dari perhitungan {pesan} = {isi}")

# def display_keliling(pesan,isi):
#     print(f"Hasil dari perhitungan {pesan} = {isi}")

# while True:
#     header()
#     opsi = int(input("Pilih 1 Untuk Hitung Luas Pilih 2 Untuk Hitung Keliling: "))
#     if opsi == 1:
#         LEBAR,PANJANG = input_user()
#         LUAS = luas(LEBAR,PANJANG)
#         display_luas("Luas", LUAS)
#     elif opsi == 2:
#         LEBAR,PANJANG = input_user()
#         KELILING = keliling(LEBAR,PANJANG)
#         display_keliling("Keliling", KELILING)
#     else: 
#         print(f"Pilh lah angka yang sesaui antara 1/2")
#     lanjut = input("Ketik y Untuk Lanjut Ketik n Untuk Berhenti: ")
#     if lanjut == "n":
#         break
# print(f"Arigato Gosaiamashhhhhh")

# def well(weel:float):
#     hasil = weel**2
#     print(hasil)
# well(5.10)
# import os
# def banner():
#     print("*" * 20 + "*" * 20)
#     print("Ini Adalah Kalkulator Sederhana")

# def tambah():
#     angka1 = int(input("Masukan Angka Pertama : "))
#     angka2 = int(input("Masukan Angka Kedua : "))
#     hasil = angka1 + angka2
#     print(f"Hasilnya {hasil}")

# def kurang():
#     angka1 = int(input("Masukan Angka Pertama : "))
#     angka2 = int(input("Masukan Angka Kedua : "))
#     hasil = angka1 - angka2
#     print(f"Hasilnya {hasil}")

# def bagi():
#     angka1 = int(input("Masukan Angka Pertama : "))
#     angka2 = int(input("Masukan Angka Kedua : "))
#     hasil = angka1 / angka2
#     print(f"Hasilnya {hasil}")

# def kali():
#     angka1 = int(input("Masukan Angka Pertama : "))
#     angka2 = int(input("Masukan Angka Kedua : "))
#     hasil = angka1 * angka2
#     print(f"Hasilnya {hasil}")

# while True:
#     os.system("cls")
#     banner()
#     operator = input("Masukan Perjumlahan Yang Diinginkan : ")
#     if operator == "x":
#         kali()
#     elif operator == "/":
#         bagi()
#     elif operator == "-":
#         kurang()
#     elif operator == "+":
#         tambah()
#     else :
#         print("Anda Harus memasukn x , / , - , +")

#     lanjut = input("Apakah anda ingin lanjut perjumlahan ? y/n: ")
#     if lanjut == "n":
#         break
    
# print("Arigato")

# def pangkat(n):
#     return lambda angka: angka**n

# input_pangkat = pangkat(int(input("Masukan Pangkat yang anda inginkan : ")))
# masukan = int(input("Masukan angka yang ingin di pangkatkan : "))
# print(f"hasil dari pangkat yang anda inginkan adalah {input_pangkat(masukan)} ")

