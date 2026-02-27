#database pengguna
users = {
    "Fadhil":"password123",
    "Anya":"admin456",
    "Budi":"dev789"
}

print("===login manual cihuy===")
input_username = input("masukkan username :")
input_password = input("masukkan password :")

if input_username in users and users[input_username] == input_password:
    print("login {input_username}: Berhasil")
else:
    print("login {input_username}: Gagal - Username atau Password salah")