# kita akan buat mesin pasword & username :

#proses buat username
while True :
    create_username = input("Buat username: ")
    if create_username == "":
        print("username tidak boleh kosong")
    elif create_username.isdigit():
        print("username tidak angka")
    elif len(create_username) < 5:
        print("username tidak boleh kurang dari 5")
    else :
            print("berhasil dibuat")
            break
while True:
    create_password = input("Buat password: ")
    if create_password == "":
        print("tidak boleh kosong")
    elif create_password.isdigit():
        print("password tidak boleh hanya angka")
    elif len(create_password) < 8:
        print("password tidak boleh kurang dari 8")
    else:
        print("password berhasil di buat")
        break
percoban = 0
while True:
    nama_atau_username = input("Masukan username: ")
    if nama_atau_username != create_username:
        print("username tidak valid")
    else :
        print("username valid")
        break
percobaan = 0
max_percobaan = 3
while True :
    password = input("Masukan password: ")
    if password == create_password:
        print("SUDAH LOGIN !")
        break
    else:
        percobaan += 1
        sisa_kesempatan = max_percobaan - percobaan
        if percobaan >= max_percobaan:
            print("Kesempatan habis coba beberapa menit lagi")
            break
        else :
            print(f'Password salah sisa kesempatan : {sisa_kesempatan}')
