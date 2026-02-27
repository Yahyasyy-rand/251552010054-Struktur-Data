user = {"name": "fadhil","age": 27}

#menggunakan get agar aman dari KeyError
email = user.get("email", "email belum tersedia")
print(email)

#menambahkan key jika belum ada dengan setdefault
user.setdefault("email", "fadhil@example.com")

#update data
user.update({"age": 28, "role":"DevOps"})

#menghapus key
age = user.pop("age")

#menampilkan semua key dan values
print(user.keys())
print(user.values())

#menyalin dictionary
user_copy = user.copy()
print(user_copy)

print(user)
print(user_copy)