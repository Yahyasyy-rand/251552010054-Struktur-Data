#membuat dictionary
user = {
    "name":"Fadhil",
    "age": 27,
    "role":"DevOps"
}

#mengakses value berdasarkan key
print("Nama:", user["name"])
print("Usia:", user["age"])
print("peran:", user["role"])

#menambah key-value baru
user["email"] = "abc@example.com"

#mengubah value
user["age"] = 28

#hasil akhir
print(user)
