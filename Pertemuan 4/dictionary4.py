#database pengguna
users = {
    "Fadhil":"password123",
    "Anya":"admin456",
    "Budi":"dev789"
}

#daftar login yang ingin dicetak
login_attempts = {
    ("Fadhil","password123")
    ("Anya","admin456")
    ("Budi","dev789")
}

#cek semua login

for username, password in login_attempts:
    if username in users and users[username] == password:
        print(f"login {username}: Berhasil")
    else:
        print(f"login {username}: gagal - username atau password salah")