def input_data():
    nama = input ("Masukkan Nama :")
    alamat = input (" Masukkan Alamat :")
    return [nama, alamat ];

def cetak(nama, alamat="Bekasi"):
    print("Namanya Adalah:", nama)
    print("Alamatnya Adalah:", alamat)
def cetak2(*data):
    for x in data:
        print(x)

#while true
data = input_data()
cetak(data[0])
cetak(data[0], data[1])
cetak(alamat=data[1], nama=data[0])
#cetak(alamat=data[1])

cetak2("daul", "iin", "yuli", "yuni")

data2 = lambda x, y: (x+y) *2
print(data2(100,10))

data3 = list(map(lambda x: (x * 2), data))
data4 = list(filter(lambda  x: x== 'jakarta',data))
print(data3)
print(data4)
