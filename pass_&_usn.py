# kita akan buat mesin pasword & username :
nama_atau_username = input("Masukan username: ")
while nama_atau_username == "" or len(nama_atau_username) < 8:
    print("username tidak valid")
    nama_atau_username = input("Masukan username: ")
    if nama_atau_username == "sasadad":
        password = input("Masukan password: ")
        while len(password) < 8:
            print("password tidak valid")
            password = input("Masukan password: ")
            if password == "dadfefsa123":
                print("ANDA SUDAH LOGIN")
                break
