import numpy as np
from sklearn.preprocessing import MinMaxScaler

print("================================")
print("Nama : Ahmad Juantoro")
print("NIM  : 171011400142")
print("UAS  : Decision Tree")
print("================================")
awal = int(input("Input Nilai Awal : "))
akhir = int(input("Input Nilai Akhir : "))
baris = int(input("Input Nilai Baris : "))
kolom = int(input("Input Nilai Kolom : "))
if (awal > akhir):
    print("Nilai Akhir Harus Lebih Besar!")
else:
    hasil = np.random.randint(awal, akhir, (baris, kolom))
    print("Hasil : \n",hasil)

