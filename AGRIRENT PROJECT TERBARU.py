import csv
import datetime as dt

def garis(a, b=123):
    print(a * b)

def cover(b=123):
    garis("₊˚ʚ 🌱 ₊˚✧ ﾟ.", b)
    print("".center(b))
    print("██████╗  ██████╗ ██████╗ ██╗██████╗ ███████╗███╗   ██╗████████╗".center(b))
    print("██╔══██╗██╔════╝ ██╔══██╗██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝".center(b))
    print("███████║██║  ███╗██████╔╝██║██████╔╝█████╗  ██╔██╗ ██║   ██║   ".center(b))
    print("██╔══██║██║   ██║██╔══██╗██║██╔══██╗██╔══╝  ██║╚██╗██║   ██║   ".center(b))
    print("██║  ██║╚██████╔╝██║  ██║██║██║  ██║███████╗██║ ╚████║   ██║   ".center(b))
    print("╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝".center(b))
    print("".center(b))
    garis("₊˚ʚ 🌱 ₊˚✧ ﾟ.", b)

def enter(a=""):
    input(f"{a}tekan [ENTER] untuk melanjutkan >> ")

def halaman_agrirent():
    print("""
                                                1. REGISTRASI
                                                2. LOGIN SEBAGAI ADMIN
                                                3. LOGIN SEBAGAI PENYEWA
                                                4. EXIT
""")
    garis("=")
    while True :
        try:
            pilih = int(input("silahkan pilih opsi anda:) >> "))
            if pilih == 1:
                registrasi()
            elif pilih == 2:
                login_admin()
            elif pilih == 3:
                login_penyewa()
            elif pilih == 4:
                exit_program()
            else:
                print("Opsss, opsi yang Anda pilih tidak tersedia:( ")
        except ValueError:
            print("Silahkan pilih opsi anda kembali dalam bentuk angka")
            halaman_agrirent()

def registrasi():
    while True:
        username_penyewa = input("Masukkan username baru: ")
        while len(username_penyewa) == 0:  # Memastikan input tidak kosong
            print("Username tidak boleh kosong. Silakan coba lagi.")
            username_penyewa = input("Masukkan username baru: ")
            
        password_penyewa = input("Masukkan password baru: ")
        while len(password_penyewa) == 0:  # Memastikan input tidak kosong
            print("Password tidak boleh kosong. Silakan coba lagi.")
            password_penyewa = input("Masukkan password baru: ")
        
        # Validasi NIK
        while True:
            nik = input("Masukkan NIK (16 digit): ")
            if len(nik) == 16 and nik.isdigit():
                break
            else:
                print("NIK harus berupa 16 digit angka. Silakan coba lagi.")
        
        # Validasi Nomor Telepon
        while True:
            nomor_telepon = input("Masukkan Nomor Telepon: ")
            if len(nomor_telepon) == 12 and nomor_telepon.isdigit():
                break
            else:
                print("nomor telepon harus berupa angka. Silakan coba lagi.")

        # Periksa duplikasi data
        if cek_duplikasi(username_penyewa, nik, nomor_telepon):
            print("\nPendaftaran gagal. Username, NIK, atau Nomor Telepon sudah terdaftar.\n")
        else:
            # Simpan data jika tidak ada duplikasi
            simpan_data([username_penyewa, password_penyewa, nik, nomor_telepon])
            print("\nPendaftaran berhasil. Silakan login.\n")
            
            # Tampilkan menu login khusus penyewa setelah registrasi
            while True:
                #clear()
                print("""
                                                1. LOGIN SEBAGAI PENYEWA
                                                2. EXIT
                """)
                garis("=")
                try:
                    pilih = int(input("Pilih Opsi yang tersedia >> "))
                    if pilih == 1:
                        #clear()
                        login_penyewa()
                    elif pilih == 2:
                        exit_program()
                    else:
                        print("Opsi yang Anda pilih tidak tersedia.")
                except ValueError:
                    print("Masukkan input dalam bentuk angka.")
                    break

# Fungsi login untuk admin
def login_admin():
    username_admin = input("Masukkan username: ")
    while len(username_admin) == 0:  # Memastikan input tidak kosong
        print("Username tidak boleh kosong. Silakan coba lagi.")
        username_admin = input("Masukkan username baru: ")
    password_admin = input("Masukkan password: ")
    while len(password_admin) == 0:  # Memastikan input tidak kosong
        print("Password tidak boleh kosong. Silakan coba lagi.")
        password_admin = input("Masukkan password baru: ")
    if cek_loginadmin(username_admin, password_admin):
        print("\nLogin berhasil sebagai Admin.")
        # enter()
        beranda_admin()
    else:
        print("Login gagal. Username atau password salah.")
        enter()

# Fungsi untuk memeriksa login dari CSV
def cek_loginadmin(username_admin, password_admin):
    file_admin = "dataadmin.csv"  # Nama file tetap
    try:
        with open(file_admin, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username_admin and row[1] == password_admin:
                    return True
        return False
    except FileNotFoundError:
        print(f"File {file_admin} tidak ditemukan.")
        return False
    
# Fungsi login untuk penyewa
def login_penyewa():
    while True:
        username_penyewa = input("Masukkan username: ")
        password_penyewa = input("Masukkan password: ")
        if cek_loginpenyewa(username_penyewa, password_penyewa):
            print("Login berhasil sebagai Penyewa.")
            while True:
                #clear()
                # print(f"Selamat datang, {username}!")
                beranda_penyewa(username_penyewa)
                break  # Kembali ke menu login utama setelah logout
            break  # Setelah login berhasil, keluar dari loop login
        else:
            print("Login gagal. Username atau password salah.")
            continue  # Mengulang input jika login gagal


# Fungsi untuk memeriksa login dari CSV
def cek_loginpenyewa(username_penyewa, password_penyewa):
    file_penyewa = "datapenyewa.csv"  # Nama file tetap
    try:
        with open(file_penyewa, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username_penyewa and row[1] == password_penyewa:
                    return True
        return False
    except FileNotFoundError:
        print(f"File {file_penyewa} tidak ditemukan.")
        return False

    
# Fungsi untuk mengecek apakah data sudah ada
def cek_duplikasi(username_penyewa, nik, nomor_telepon):
    file_penyewa = "datapenyewa.csv"  # Nama file tetap
    data = baca_data(file_penyewa)  # Fungsi baca_data harus menggunakan nama file tetap ini
    for row in data:
        if row[0] == username_penyewa or row[2] == nik or row[3] == nomor_telepon:
            return True  # Duplikasi ditemukan
    return False

def simpan_data(data):
    file_penyewa = "datapenyewa.csv"  # Nama file tertentu
    with open(file_penyewa, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


# Fungsi untuk menampilkan pesan terima kasih dan keluar
def exit_program():
    #clear()
    print("\n")
    print("Terima kasih telah menggunakan program ini\n\n".center(114))
    garis("=", 114)
    exit()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BERANDA PENYEWA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Fungsi untuk beranda penyewa
def beranda_penyewa(username_penyewa):
    while True:
        #clear()
        print(f"Selamat datang, {username_penyewa}!")
        print("""
                                                1. LIHAT STOK BARANG
                                                2. PENGEMBALIAN BARANG
                                                3. KEMBALI KE MENU UTAMA
        """)
        garis("=")
        try:
            pilihan = int(input("Pilih opsi yang tersedia >> "))
            if pilihan == 1:
                lihat_stok_barang()  # Panggil fungsi stok barang
            elif pilihan == 2:
                pengembalian_barang(username_penyewa)
            elif pilihan == 3:
                halaman_agrirent()  # Kembali ke menu utama
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
                enter()
        except ValueError:
            print("Masukkan input dalam bentuk angka.")
            enter()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LIHAT STOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Fungsi untuk menampilkan stok barang
def lihat_stok_barang():
    stok_barang = baca_data_barang()
    if not stok_barang:
        print("Stok barang tidak tersedia atau file tidak ditemukan.")
        return None

    # Menampilkan tabel stok barang
    garis("=")
    print(f"{'Nama Barang':<30}{'Harga Sewa/Hari':<20}{'Total Stok':<10}")
    garis("-")
    for nama, info in stok_barang.items():
        print(f"{nama:<30}Rp {info['harga']:<19}{info['stok']:<10}")
    garis("=")

    # Menambahkan menu setelah stok barang ditampilkan
    while True:
        print("""
            1. Sewa Barang
            2. Kembali ke Menu
        """)
        garis("=")
        try:
            pilihan = int(input("Pilih Opsi yang tersedia >> "))
            if pilihan == 1:
                sewa_barang(stok_barang)  # Panggil fungsi sewa_barang
                break
            elif pilihan == 2:
                break  # Kembali ke menu sebelumnya
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

# Fungsi untuk menyimpan data barang ke CSV setelah diubah
def simpan_data_barang(stok_barang):
    with open('databarang.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama Barang', 'Harga Sewa', 'Total Stok'])
        for nama, info in stok_barang.items():
            writer.writerow([nama, info['harga'], info['stok']])

# Fungsi untuk menyewa barang
def sewa_barang(stok_barang):
    if not stok_barang:
        print("Stok barang tidak ditemukan.")
        return None

    while True:
        nama_barang = input("Masukkan nama barang yang ingin disewa: ")
        if len(nama_barang) == 0:  # Jika input kosong
            print("Nama barang tidak boleh kosong. Coba lagi.")  # Menampilkan pesan kesalahan
        elif nama_barang in stok_barang:  # Jika barang ditemukan
            break  # Jika barang ditemukan, keluar dari loop
        else:
            print("Barang tidak ditemukan. Coba lagi.")  # Menampilkan pesan dan meminta input ulang
        

    try:
        # Validasi input jumlah barang yang ingin disewa
        while True:
            try:
                jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin disewa: "))
                if jumlah <= 0:
                    print("Jumlah barang yang disewa harus lebih dari 0.")
                    continue
                if jumlah > stok_barang[nama_barang]['stok']:
                    print("Stok tidak mencukupi.")
                    continue
                break  # Jika jumlah valid, keluar dari loop
            except ValueError:
                print("Jumlah barang harus berupa angka yang valid.")

        # Validasi tanggal penyewaan
        while True:
            try:
                tanggal_mulai_input = input("Masukkan tanggal penyewaan (YYYY-MM-DD): ")
                tanggal_mulai = dt.datetime.strptime(tanggal_mulai_input, "%Y-%m-%d")
                break  # Jika format tanggal benar, keluar dari loop
            except ValueError:
                print("Format tanggal salah! Pastikan format yang benar adalah YYYY-MM-DD.")
        
        # Validasi durasi penyewaan
        while True:
            try:
                durasi_hari = int(input("Masukkan durasi penyewaan (hari): "))
                if durasi_hari <= 0:
                    print("Durasi penyewaan harus lebih dari 0 hari.")
                    continue
                break  # Jika durasi valid, keluar dari loop
            except ValueError:
                print("Durasi penyewaan harus berupa angka.")

        # Menentukan tanggal kembali
        tanggal_kembali = tanggal_mulai + dt.timedelta(days=durasi_hari)
        
        # Menampilkan informasi tanggal penyewaan dan pengembalian
        print(f"Tanggal penyewaan: {tanggal_mulai.strftime('%Y-%m-%d')}")
        print(f"Tanggal pengembalian: {tanggal_kembali.strftime('%Y-%m-%d')}")

        total_harga = jumlah * stok_barang[nama_barang]['harga'] * durasi_hari

        # Mengurangi stok barang
        stok_barang[nama_barang]['stok'] -= jumlah

        # Meminta username
        while True:
            username_input = input("Masukkan username Anda: ")
            if len(username_input) == 0 or username_input.isspace():  # Mengecek apakah input kosong atau hanya spasi
                print("Username tidak boleh kosong. Coba lagi.")
            elif username_input != username_penyewa:  # Mengecek apakah username cocok dengan username login
                print("Username tidak sesuai dengan username login. Coba lagi.")
            else:
                username_penyewa = username_input
                break  # Keluar dari loop jika username valid        
       

        # Menambahkan status "Disewa" pada data penyewaan
        status = "Disewa"

        # Simpan perubahan ke databarang.csv
        simpan_data_barang(stok_barang)

        # Simpan transaksi ke datapenyewaan.csv dengan format yang diminta
        simpan_data('datapenyewaan.csv', [username_penyewa, nama_barang, jumlah, durasi_hari, total_harga, tanggal_mulai.strftime('%Y-%m-%d'), tanggal_kembali.strftime('%Y-%m-%d'), status])

        print(f"Barang berhasil disewa. Total harga: Rp {total_harga:,}")
        return username_penyewa, nama_barang, jumlah, durasi_hari, total_harga, tanggal_mulai, tanggal_kembali, status

    except ValueError as e:
        print("Input tidak valid. Pastikan memasukkan angka dan format tanggal yang benar.")
        return None

# Fungsi Baca data stok dari CSV
def baca_data_barang():
    try:
        stok_barang = {}
        with open('databarang.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    stok_barang[row['Nama Barang']] = {
                        "harga": int(row['Harga Sewa']),
                        "stok": int(row['Total Stok']) if row['Total Stok'] else 0  # Tangani None atau kosong
                    }
                except (ValueError, TypeError) as e:
                    print(f"Data tidak valid untuk barang '{row.get('Nama Barang', 'Unknown')}': {e}")
        return stok_barang
    except FileNotFoundError:
        print("File databarang.csv tidak ditemukan.")
        return None

# Fungsi Menyimpan perubahan ke file stok
def simpan_data_barang(stok_barang):
    with open('databarang.csv', mode='w', newline='') as file:
        fieldnames = ['Nama Barang', 'Harga Sewa', 'Total Stok']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for nama, info in stok_barang.items():
            writer.writerow({
                "Nama Barang": nama,
                "Harga Sewa": info['harga'],
                "Total Stok": info['stok']
            })

# Fungsi untuk menyimpan data ke file CSV (overwrite)
def simpan_data_csv(file_barang, data):
    try:
        with open(file_barang, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except IOError:
        print("Terjadi kesalahan saat menyimpan data ke file.")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PENGEMBALIAN BARANG<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Fungsi untuk menampilkan riwayat penyewaan dan melakukan pengembalian
# Fungsi untuk pengembalian barang
def pengembalian_barang(username_penyewa):
    #clear()
    riwayat = baca_data('datapenyewaan.csv')  # Baca riwayat penyewaan
    barang_disewa = [entry for entry in riwayat if entry[0] == username_penyewa and entry[7] == "Disewa"]
    
    if not barang_disewa:
        print("Tidak ada barang yang sedang Anda sewa.")
        enter()
        return
    
    print(f"Riwayat penyewaan untuk {username_penyewa}:\n")
    garis("=")
    print(f"{'No.':<5}{'Nama Barang':<30}{'Jumlah':<10}{'Durasi':<10}{'Total Harga':<15}{'Tanggal Kembali':<15}{'Status':<10}")
    garis("-")
    for idx, entry in enumerate(barang_disewa, start=1):
        print(f"{idx:<5}{entry[1]:<30}{entry[2]:<10}{entry[3]:<10}Rp {int(entry[4]):<13}{entry[6]:<15}{entry[7]:<10}")
    garis("=")
    
    try:
        no_barang = int(input("Masukkan nomor barang yang ingin dikembalikan: "))
        if no_barang < 1 or no_barang > len(barang_disewa):
            print("Nomor tidak valid.")
            enter()
            return
        
        barang = barang_disewa[no_barang - 1]
        nama_barang, jumlah, total_harga, tanggal_kembali = barang[1], int(barang[2]), int(barang[4]), barang[6]
        tanggal_kembali = dt.datetime.strptime(tanggal_kembali, '%Y-%m-%d')
        hari_terlambat = (dt.datetime.now() - tanggal_kembali).days
        
        # Hitung denda jika ada
        denda = 0
        if hari_terlambat > 0:
            denda = int(total_harga * 0.05 * hari_terlambat)
            print(f"\nAnda terlambat mengembalikan barang selama {hari_terlambat} hari.")
            print(f"Denda yang harus dibayar: Rp {denda:,}")
        
        total_bayar = total_harga + denda
        print(f"Total yang harus Anda bayar: Rp {total_bayar:,}")
        
        # Meminta input nominal pembayaran
        while True:
            try:
                nominal = int(input("Masukkan nominal pembayaran: "))
                if nominal < total_bayar:
                    print("Nominal pembayaran kurang. Silakan coba lagi.")
                    continue
                break
            except ValueError:
                print("Masukkan angka yang valid.")
        
        if nominal > total_bayar:
            print(f"Kembalian Anda: Rp {nominal - total_bayar:,}")
        
        # Perbarui status di CSV
        barang[7] = "Dikembalikan"
        simpan_data_csv('datapenyewaan.csv', riwayat)
        
        # Kembalikan stok barang
        stok_barang = baca_data_barang()
        if nama_barang in stok_barang:
            stok_barang[nama_barang]['stok'] += jumlah
            simpan_data_barang(stok_barang)
        
        print("\nBarang berhasil dikembalikan. Terima kasih!")
        enter()
    except ValueError:
        print("Masukkan input dalam bentuk angka yang valid.")
        enter()




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BERANDA ADMIN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Tambahkan fungsi beranda admin
def beranda_admin():
    while True:
        #clear()
        print("""
                                                    BERANDA ADMIN
        """)
        garis("=")
        print("""
                                                1. MELIHAT STOK BARANG
                                                2. MELIHAT RIWAYAT PENYEWAAN
                                                3. KEMBALI KE MENU UTAMA
        """)
        garis("=")

        try:
            pilih = int(input("Pilih Opsi yang tersedia >> "))
            if pilih == 1:
                #clear()
                menu_stok_barang()
            elif pilih == 2:
                #clear()
                lihat_riwayat_penyewaan()
            elif pilih == 3:
                halaman_agrirent()
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

# Fungsi untuk menu stok barang

def menu_stok_barang():
    while True:
        print("Stok Barang Saat Ini:\n")
        garis("-")  # Asumsikan `garis` adalah fungsi untuk mencetak garis pemisah
        barang = baca_data('databarang.csv')  # Membaca file CSV
        
        if barang:
            barang = barang[1:]  # Melewati baris pertama (header)
            print("No | Nama Barang          | Harga Barang     | Jumlah Stok")
            print("-" * 60)
            for i, row in enumerate(barang):
                nama = row[0]
                harga = row[1]
                stok = row[2]
                print(f"{i + 1:<3} | {nama:<20} | Rp {harga:<12} | {stok:<5}")
        else:
            print("Tidak ada data barang saat ini.")

        garis("-")

        print("""
                                                1. TAMBAH STOK BARANG
                                                2. KEMBALI KE BERANDA ADMIN
        """)
        garis("=")
        try:
            pilih = int(input("Pilih Opsi yang tersedia >> "))
            if pilih == 1:
                tambah_stok_barang()
            elif pilih == 2:
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

# Fungsi untuk menambah stok barang
def tambah_stok_barang():
    # Membaca data barang dari file CSV
    barang = baca_data('databarang.csv')
    
    while True:
        nama_barang = input("Masukkan nama barang: ")
        if len(nama_barang) == 0 or nama_barang.isspace():  # Mengecek apakah input kosong atau hanya spasi
            print("Nama barang tidak boleh kosong. Coba lagi.")  # Menampilkan pesan kesalahan
        else:
            break  # Keluar dari loop jika input valid

    # Periksa apakah barang sudah ada
    barang_ditemukan = False
    for row in barang:
        # Validasi: Pastikan baris memiliki setidaknya 3 kolom
        if len(row) >= 3 and row[0].lower() == nama_barang.lower():
            try:
                jumlah_tambah = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
                row[2] = str(int(row[2]) + jumlah_tambah)  # Update stok barang
                print(f"\nStok barang '{nama_barang}' berhasil ditambahkan sebanyak {jumlah_tambah}.")
                barang_ditemukan = True
                break
            except ValueError:
                print("Input jumlah stok harus berupa angka. Silakan coba lagi.")
                return

    if not barang_ditemukan:
        # Jika barang belum ada, tambahkan barang baru
        try:
            harga_barang = int(input("Masukkan harga barang: "))
            jumlah_stok = int(input("Masukkan jumlah stok barang: "))
            barang.append([nama_barang, str(harga_barang), str(jumlah_stok)])
            print(f"\nBarang baru '{nama_barang}' berhasil ditambahkan dengan harga {harga_barang} dan stok {jumlah_stok}.")
        except ValueError:
            print("Input harga dan stok harus berupa angka. Silakan coba lagi.")
            return

    # Simpan perubahan ke file CSV
    try:
        with open('databarang.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(barang)
        print("\nPerubahan telah disimpan ke dalam file.")
    except IOError:
        print("Terjadi kesalahan saat menyimpan data ke file.")
    
    enter("")

# Fungsi untuk membaca data dari file CSV
def baca_data(file_barang):
    try:
        with open(file_barang, mode='r') as file:
            reader = csv.reader(file)
            return [row for row in reader if len(row) > 0]  # Hapus baris kosong
    except FileNotFoundError:
        print(f"File '{file_barang}' tidak ditemukan. Membuat file baru...")
        return []  # Kembalikan list kosong jika file tidak ditemukan

def lihat_riwayat_penyewaan():
    try:
        # Menggunakan nama file langsung (relatif ke lokasi script)
        file_penyewaan = 'datapenyewaan.csv'
        riwayat_penyewaan = []

        # Membaca file CSV
        with open(file_penyewaan, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Membaca header

            for row in reader:
                username_penyewa = row[0]
                nama_barang = row[1]
                jumlah = int(row[2])
                durasi_hari = int(row[3])
                total_harga = int(row[4])
                tanggal_mulai = row[5]
                tanggal_kembali = row[6]
                
                # Menentukan status penyewaan
                tanggal_kembali_obj = dt.datetime.strptime(tanggal_kembali, "%Y-%m-%d")
                hari_ini = dt.datetime.now()
                status = "Selesai" if hari_ini > tanggal_kembali_obj else "Sedang Berjalan"

                # Menyimpan data
                riwayat_penyewaan.append([
                    username_penyewa, nama_barang, jumlah, durasi_hari,
                    total_harga, tanggal_mulai, tanggal_kembali, status
                ])

        # Menampilkan tabel secara manual
        print("\nRiwayat Penyewaan Barang:")
        print("-" * 115)
        print(f"{'Username':<15} {'Barang':<15} {'Jumlah':<10} {'Durasi':<10} {'Total Harga':<15} {'Tgl Mulai':<12} {'Tgl Kembali':<12} {'Status':<15}")
        print("-" * 115)

        for row in riwayat_penyewaan:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} Rp {row[4]:<12,} {row[5]:<12} {row[6]:<12} {row[7]:<15}")

        print("-" * 115)
        
        print("""
                                                1. KEMBALI KE BERANDA ADMIN
        """)
        garis("=")
        try:
            pilih = int(input("Pilih Opsi yang tersedia >> "))
            if pilih == 1:
                beranda_admin()
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

    except FileNotFoundError:
        print("File 'datapenyewaan.csv' tidak ditemukan di direktori saat ini.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    #clear()
    cover()
    enter("\nSELAMAT DATANG DI TEMPAT SEWA KAMI, AGRIRENT:). ")
    halaman_agrirent()
    beranda_penyewa()
    pengembalian_barang()
    beranda_admin()
    lihat_riwayat_penyewaan()
