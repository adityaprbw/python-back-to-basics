text = input("Input text apa pun: ")
print(f"data: {text}, bertipe: {type(text)}")

data_int = int(input("Input nomor kesukaan: "))
print(f"data: {data_int}, bertipe: {type(data_int)}")

data_bool = bool(int(input("Input bulan kelahiran: ")))
print(f"data: {data_bool}, bertipe: {type(data_bool)}")
"""
catatan:

input itu diterimanya sebagai str sehingga untuk kebutuhan angka perlu dilakukan type casting
"""