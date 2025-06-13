# int casting ke tipe data lain
temp : int = -2
print(f"data: {temp}, {type(temp)}")

str_variable : str = str(temp)
float_variable : float = float(temp)
bool_variable : bool = bool(temp)

print(f"data: {str_variable}, {type(str_variable)}")
print(f"data: {float_variable}, {type(float_variable)}")
print(f"data: {bool_variable}, {type(bool_variable)}")

print("\n==========\n")

# float casting ke tipe data lain
temp : float = 0.0
print(f"data: {temp}, {type(temp)}")

str_variable : str = str(temp)
int_variable : int = int(temp)
bool_variable : bool = bool(temp)

print(f"data: {str_variable}, {type(str_variable)}")
print(f"data: {int_variable}, {type(int_variable)}")
print(f"data: {bool_variable}, {type(bool_variable)}")

print("\n==========\n")

# str casting ke tipe data lain
temp : str = "0"
# temp : str = ""
print(f"data: {temp}, {type(temp)}")

float_variable : float = float(temp)
int_variable : int = int(temp)
bool_variable : bool = bool(temp)

print(f"data: {float_variable}, {type(float_variable)}")
print(f"data: {int_variable}, {type(int_variable)}")
print(f"data: {bool_variable}, {type(bool_variable)}")

print("\n==========\n")

# bool casting ke tipe data lain
temp : bool = "False"
print(f"data: {temp}, {type(temp)}")

# float_variable : float = float(temp) tidak bisa casting bool ke float
# int_variable : int = int(temp) tidak bisa casting bool ke int
str_variable : str = str(temp)

# print(f"data: {float_variable}, {type(float_variable)}")
# print(f"data: {int_variable}, {type(int_variable)}")
print(f"data: {str_variable}, {type(str_variable)}")

print("\n========== Coba-coba ==========\n")
float_var = 8.85 # walau >= 5.0 maka hasilnya tetap dibulatkan ke bawah
print(int(float_var))

