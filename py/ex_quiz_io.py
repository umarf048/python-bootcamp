import os
os.system('cls')
markah = 0


print("Soalan pertama \nApakah ibu negara Malaysia? \nJawapan anda :")
a = input().lower().strip()
if a == "kuala lumpur":
    print("Anda betul!")
    markah = markah + 1
else:
    print("Anda salah!")
    input()
    os.system('cls')

print("Soalan kedua \nApakah hasil 200 x 3? \nJawapan anda :")
b = input()
if b == "600":
    print("Anda betul!")
    markah +=1
else:
    print("Anda salah!")
    input()
    os.system('cls')

print("Soalan ketiga \nApakah hasil warna antara biru dan kuning? \nJawapan anda :")
c = input().lower().strip()
if c == "hijau":
    print("Anda betul!")
    markah = markah + 1
else:
    print("Anda salah!")
    input()
    os.system('cls')

if markah == 3:
    print(f"Tahniah nilai anda {markah}/3")
else:
    print(f"Cuba lagi, nilai anda {markah}/3")
