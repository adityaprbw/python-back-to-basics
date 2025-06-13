from ctypes import c_ulonglong

# tipe data untuk bilangan bulat
data_int : int = 1
print(f"data: {data_int}, bertipe: {type(data_int)}")

# tipe data untuk bilangan decimal/pecahan
data_float : float = 3.5
print(f"data: {data_float}, bertipe: {type(data_float)}")

# tipe data untuk kumpulan karakter
data_str : str = "I will win"
print(f"data: {data_str}, bertipe: {type(data_str)}")

# tipe data untuk pernyataan kebenaran
data_bool : bool = False
print(f"data: {data_bool}, bertipe: {type(data_bool)}")

## tipe data complex
data_complex : complex = complex(3,4)
print(f"data: {data_complex}, bertipe: {type(data_complex)}")

## tipe data none
data_none : None = None
print(f"data: {data_none}, bertipe: {type(data_none)}")

## tipe data dari C language
data_c_ulonglong : c_ulonglong = c_ulonglong(18573921111)
print(f"data: {data_c_ulonglong}, bertipe: {type(data_c_ulonglong)}")
