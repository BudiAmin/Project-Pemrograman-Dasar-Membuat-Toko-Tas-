import mysql.connector
import matplotlib.pyplot as plt

pengunjung_aktif = None
admin_aktif = None

# Establishing a connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coba_4",
)
cursor = conn.cursor()


def register_admin():
    print("Register Admin")
    nama = input("Nama: ")
    no_tlp = input("Nomor Telepon: ")
    email = input("Email: ")
    password = input("Password: ")
    alamat = input("Alamat: ")

    sql = "INSERT INTO admin (nama, no_tlp, email, password, alamat) VALUES (%s, %s, %s, %s, %s)"
    values = (nama, no_tlp, email, password, alamat)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Registrasi berhasil.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def register_pengunjung():
    print("Register Pengunjung")
    nama_pelanggan = input("Nama Pelanggan: ")
    no_tlp = input("Nomor Telepon: ")
    email = input("Email: ")
    password = input("Password: ")
    alamat = input("Alamat: ")

    sql = "INSERT INTO pengunjung (nama_pelanggan, no_tlp, email, password, alamat) VALUES (%s, %s, %s, %s, %s)"
    values = (nama_pelanggan, no_tlp, email, password, alamat)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Registrasi berhasil.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def login_admin():
    print("Login Admin")
    email = input("Email: ")
    password = input("Password: ")

    sql = "SELECT * FROM admin WHERE email = %s AND password = %s"
    values = (email, password)

    cursor.execute(sql, values)
    result = cursor.fetchone()

    if result:
        print("Login berhasil.")
        print("Informasi Admin:")
        print("ID:", result[0])
        print("Nama:", result[1])
        print("No. Telepon:", result[2])
        print("Email:", result[3])
        print("Alamat:", result[5])
        return result  # Kembalikan data admin yang berhasil login
    else:
        print("Login gagal. Periksa kembali email dan password.")
        return None


def login_pengunjung():
    print("Login Pengunjung")
    email = input("Email: ")
    password = input("Password: ")

    sql = "SELECT * FROM pengunjung WHERE email = %s AND password = %s"
    values = (email, password)

    cursor.execute(sql, values)
    result = cursor.fetchone()

    if result:
        print("Login berhasil.")
        print("Informasi Pengunjung:")
        print("ID:", result[0])
        print("Nama Pelanggan:", result[1])
        print("No. Telepon:", result[2])
        print("Email:", result[3])
        print("Alamat:", result[5])
        return result  # Kembalikan data pengunjung yang berhasil login
    else:
        print("Login gagal. Periksa kembali email dan password.")
        return None


def admin_menu():
    print("Admin Menu:")
    print("1. Create Pelanggan")
    print("2. Update Pelanggan")
    print("3. Delete Pelanggan")
    print("4. Display Pelanggan")
    print("5. Create Produk")
    print("6. Update Produk")
    print("7. Delete Produk")
    print("8. Display Produk")
    print("9. Create Transaksi")
    print("10. View Transaksi")
    print("11. Exit")


def user_menu():
    print("User Menu:")
    print("1. Display Produk")
    print("2. Create Transaksi")
    print("3. Exit")


def create_pengunjung():
    print("Create Pengunjung")
    nama_pelanggan = input("Nama Pelanggan: ")
    no_tlp = input("Nomor Telepon: ")
    email = input("Email: ")
    password = input("Password: ")
    alamat = input("Alamat: ")

    # Insert data into pengunjung table
    sql = "INSERT INTO pengunjung(nama_pelanggan, no_tlp, email, password, alamat) VALUES (%s, %s, %s, %s, %s)"
    values = (nama_pelanggan, no_tlp, email, password, alamat)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Data Pengunjung berhasil ditambahkan.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def update_pengunjung():
    print("Update Pengunjung")
    id_pelanggan = int(input("Masukkan ID Pelanggan yang akan diupdate: "))
    nama_pelanggan = input("Nama Pelanggan baru: ")
    no_tlp = input("Nomor Telepon baru: ")
    email = input("Email baru: ")
    password = input("Password baru: ")
    alamat = input("Alamat baru: ")

    # Update data in pengunjung table
    sql = "UPDATE pengunjung SET nama_pelanggan = %s, no_tlp = %s, email = %s, password = %s, alamat = %s WHERE id_pelanggan = %s"
    values = (nama_pelanggan, no_tlp, email, password, alamat, id_pelanggan)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Data Pengunjung berhasil diupdate.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def delete_pengunjung():
    print("Delete Pengunjung")
    id_pelanggan = int(input("Masukkan ID Pelanggan yang akan dihapus: "))

    # Delete data from pengunjung table
    sql = "DELETE FROM pengunjung WHERE id_pelanggan = %s"
    values = (id_pelanggan,)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Data Pengunjung berhasil dihapus.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def display_pengunjung():
    print("Display Pengunjung")
    cursor.execute("SELECT * FROM pengunjung")
    result = cursor.fetchall()
    for row in result:
        print(row)


def create_produk():
    print("Create Produk")
    jenis_tas = input("Jenis Tas: ")
    merk_tas = input("Merk Tas: ")
    harga = int(input("Harga: "))
    stock = int(input("Stock: "))

    # Insert data into produk table
    sql = (
        "INSERT INTO produk (jenis_tas, merk_tas, harga, stock) VALUES (%s, %s, %s, %s)"
    )
    values = (jenis_tas, merk_tas, harga, stock)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Data Produk berhasil ditambahkan.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def read_produk():
    print("Read Produk")
    cursor.execute("SELECT * FROM produk")
    result = cursor.fetchall()
    for row in result:
        print(row)


def update_produk():
    print("Update Produk")
    id_produk = int(input("Masukkan ID Produk yang akan diupdate: "))
    jenis_tas = input("Jenis Tas baru: ")
    merk_tas = input("Merk Tas baru: ")
    harga = int(input("Harga baru: "))
    stock = int(input("Stock baru: "))

    # Update data in produk table
    sql = "UPDATE produk SET jenis_tas = %s, merk_tas = %s, harga = %s, stock = %s WHERE id_produk = %s"
    values = (jenis_tas, merk_tas, harga, stock, id_produk)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Data Produk berhasil diupdate.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def delete_produk():
    print("Delete Produk")
    id_produk = int(input("Masukkan ID Produk yang akan dihapus: "))

    # Delete data from produk table
    sql = "DELETE FROM produk WHERE id_produk = %s"
    values = (id_produk,)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Data Produk berhasil dihapus.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def create_transaksi():
    print("Create Transaksi")
    id_pengunjung = int(input("ID Pengunjung: "))
    id_produk = int(input("ID Produk: "))
    jumlah = int(input("Jumlah: "))

    # Ambil harga produk dan stok terkini dari tabel produk
    cursor.execute("SELECT harga, stock FROM produk WHERE id_produk = %s", (id_produk,))
    result = cursor.fetchone()

    if result is None:
        print("Produk tidak ditemukan.")
        return

    harga, stock_produk = result

    if jumlah > stock_produk:
        print("Stok tidak mencukupi.")
        return

    total_nilai = jumlah * harga

    # Insert data into transaksi table
    sql = "INSERT INTO transaksi (id_pengunjung, id_produk, jumlah, total_nilai) VALUES (%s, %s, %s, %s)"
    values = (id_pengunjung, id_produk, jumlah, total_nilai)

    try:
        cursor.execute(sql, values)

        # Update stock in produk table
        new_stock_produk = stock_produk - jumlah
        update_stock_sql = "UPDATE produk SET stock = %s WHERE id_produk = %s"
        update_stock_values = (new_stock_produk, id_produk)
        cursor.execute(update_stock_sql, update_stock_values)

        conn.commit()
        print("Transaksi berhasil ditambahkan. Stok produk diupdate.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()


def display_transaksi():
    print("Display Transaksi")
    cursor.execute("SELECT * FROM transaksi")
    result = cursor.fetchall()
    for row in result:
        print(row)


def display_bill():
    print("Display Bill")
    id_transaksi = int(input("Masukkan ID Transaksi: "))

    # Ambil detail transaksi dari tabel transaksi
    cursor.execute("SELECT * FROM transaksi WHERE id_transaksi = %s", (id_transaksi,))
    result = cursor.fetchone()

    if result is None:
        print("Transaksi tidak ditemukan.")
        return

    id_pengunjung, id_produk, jumlah, total_nilai = result

    # Ambil detail produk dari tabel produk
    cursor.execute(
        "SELECT jenis_tas, harga FROM produk WHERE id_produk = %s", (id_produk,)
    )
    result_produk = cursor.fetchone()

    if result_produk is None:
        print("Produk tidak ditemukan.")
        return

    jenis_tas, harga = result_produk

    print("\n--- Bill ---")
    print("ID Transaksi:", id_transaksi)
    print("ID Produk:", id_produk)
    print("Jenis Tas:", jenis_tas)
    print("Jumlah:", jumlah)
    print("Harga per Unit:", harga)
    print("Total Nilai:", total_nilai)
    print("-------------\n")


def view_transaksi():
    print("View Transaksi")
    cursor.execute("SELECT * FROM transaksi")
    result = cursor.fetchall()

    if not result:
        print("Tidak ada transaksi.")
    else:
        print("\n--- Daftar Transaksi ---")
        for row in result:
            print("ID Transaksi:", row[0])
            print("ID Pengunjung:", row[1])
            print("ID Produk:", row[2])
            print("Jumlah:", row[3])
            print("Total Nilai:", row[4])
            print("-------------------------")
        print()


def get_total_harga_per_transaksi():
    cursor.execute("SELECT id_transaksi, total_nilai FROM transaksi")
    result = cursor.fetchall()
    return result


def display_grafik_transaksi():
    data_transaksi = get_total_harga_per_transaksi()

    if not data_transaksi:
        print("Tidak ada transaksi untuk ditampilkan.")
    else:
        id_transaksi, total_harga = zip(*data_transaksi)

        plt.bar(id_transaksi, total_harga, color="blue")
        plt.xlabel("ID Transaksi")
        plt.ylabel("Total Harga")
        plt.title("Grafik Total Harga per Transaksi")
        plt.show()


while True:
    print("Menu:")
    print("1. Register Admin")
    print("2. Register Pengunjung")
    print("3. Login Admin")
    print("4. Login Pengunjung")
    print("5. Exit")

    choice = input("Pilih menu (1-5): ")

    if choice == "1":
        register_admin()
    elif choice == "2":
        register_pengunjung()
    elif choice == "3":
        admin_aktif = login_admin()
    elif choice == "4":
        pengunjung_aktif = login_pengunjung()
    elif choice == "5":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    # # Jika ada admin yang aktif, tampilkan menu admin
    if admin_aktif:
        while True:
            admin_menu()
            admin_choice = input("Masukkan pilihan Anda (1-11): ")

            if admin_choice == "11":
                admin_aktif = None  # Reset admin_aktif setelah logout
                break
            elif admin_choice == "1":
                create_pengunjung()
            elif admin_choice == "2":
                update_pengunjung()
            elif admin_choice == "3":
                delete_pengunjung()
            elif admin_choice == "4":
                display_pengunjung()
            elif admin_choice == "5":
                create_produk()
            elif admin_choice == "6":
                update_produk()
            elif admin_choice == "7":
                delete_produk()
            elif admin_choice == "8":
                read_produk()
            elif admin_choice == "9":
                create_transaksi()
            elif admin_choice == "10":
                view_transaksi()
                display_grafik_transaksi()
            else:
                print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 11.")

    # Jika ada pengunjung yang aktif, tampilkan menu pengunjung
    if pengunjung_aktif:
        while True:
            user_menu()
            user_choice = input("Masukkan pilihan Anda (1-3): ")

            if user_choice == "1":
                read_produk()
            elif user_choice == "2":
                create_transaksi()
            elif user_choice == "3":
                print("Keluar dari menu pengguna. Selamat tinggal!")
                pengunjung_aktif = None  # Reset pengunjung_aktif setelah logout
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")


# Close the connection
cursor.close()
conn.close()
