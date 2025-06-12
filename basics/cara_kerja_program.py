import time

start_time = time.time()

print("Moshi moshi")

# assign nilai 6 ke variable x
x = 6

# assign nilai 12 ke variable y
y = 12

for i in range(1, 1000):
    x = 99

print(x)
print(y)

"""
cara kerja python:

- bahasa interpreted yang menterjemahkan code baris per baris
- comments tidak akan dihiraukan oleh interpreter
- walaupun bahasa interpreted, kode python juga bisa dicompile menjadi bytecode
- untuk skrip kecil run menggunakan .py
- untuk skrip besar compile dulu dan run menggunakan .pyc
"""

print(time.time() - start_time, "detik")