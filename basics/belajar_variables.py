x = 2

y = x + 4

print("nilai y =", y)

# penamaan yang tidak boleh digunakan di python:
# def = 20
# 10Juta =  10_000_000
# $koneksi = "Ini bukan PHP bro yang menggunakan dollar sign!"

# penamaan yang boleh digunakan di python:
a = 10
juta10 = 10_000_000
alas_segitiga = 10
_first_name = "Aditya"

print(a)
print(juta10)
print(alas_segitiga)
print(_first_name)

# reassignment value
y = 20
print("nilai y =", y)

a = 93
b = a # indirect assignment, bikin nama baru yang menunjuk ke objek integer yang sudah ada

print(id(a), id(b))
print(a is b)


# variable annotations:

forename : str = "Aditya"
surname : str = "Prabowo"
age : int = 17
is_handsome : bool = True

print(forename)
print(surname)
print(age)
print(is_handsome)

twelve : int = "Dua belas" # type bisa dilanggar
print(twelve)
"""
catatan:
x = 12

x adalah variable (wadah penampung nilai)

= adalah operator assignment untuk memasukkan data 12 ke x

12 adalah value yang akan dimasukkan ke variable

andaikan:
x = 10
x = 20
y = 10

value baru x yaitu 20 tidak menimpa value lama, tetapi menunjuk objek integer baru yaitu 20 yang ada di integer caching (interning),
ini adalah mekanisme python untuk menyimpan dan menggunakan kembali objek integer kecil (biasanya -5 sampai 256) agar lebih efisien dalam penggunaan memori dan performa.

variable annotations pada python digunakan ketika project sudah serius, perlu berkolaborasi dengan orang.
type pada variable annotations bisa dilanggar karena desain awal python adalah dynamically typed.
""" 