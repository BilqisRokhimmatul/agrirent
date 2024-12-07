import csv
import datetime as dt
import os 

def clear():
    os.system("cls")
    
def garis(a, b=107):
    print(a * b)

def cover(b=107):
    garis("=", b)
    print("".center(b))
    print("██████╗  ██████╗ ██████╗ ██╗██████╗ ███████╗███╗   ██╗████████╗".center(b))
    print("██╔══██╗██╔════╝ ██╔══██╗██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝".center(b))
    print("███████║██║  ███╗██████╔╝██║██████╔╝█████╗  ██╔██╗ ██║   ██║   ".center(b))
    print("██╔══██║██║   ██║██╔══██╗██║██╔══██╗██╔══╝  ██║╚██╗██║   ██║   ".center(b))
    print("██║  ██║╚██████╔╝██║  ██║██║██║  ██║███████╗██║ ╚████║   ██║   ".center(b))
    print("╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝".center(b))
    print("".center(b))
    garis("=", b)

def enter(a=""):
    input(f"{a}[ENTER] untuk melanjutkan >> ")

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
            continue
            # halaman_agrirent()
            # clear()

def registrasi():
    clear()
    while True:
        username_penyewa = input("Masukkan username baru: ")
        while len(username_penyewa) == 0:
            clear() 
            print("Username tidak boleh kosong. Silakan coba lagi.")       
            # username_penyewa = input("Masukkan username baru: ")
            

        password_penyewa = input("Masukkan password baru: ")
        while len(password_penyewa) == 0:
            clear() 
            print(f"Usename Penyewa : {username_penyewa}")
            print("Password tidak boleh kosong. Silakan coba lagi.")
            password_penyewa = input("Masukkan password baru: ")
            
        while True:
            nik = input("Masukkan NIK (16 digit): ")
            if len(nik) == 16 and nik.isdigit():
                break
            else:
                clear()
                print(f"Username Penyewa: {username_penyewa}")
                print(f"Password : {password_penyewa}")
                print("NIK harus berupa 16 digit angka. Silakan coba lagi.")

        while True:
            nomor_telepon = input("Masukkan Nomor Telepon: ")
            if len(nomor_telepon) == 12 and nomor_telepon.isdigit():
                break
            else:
                clear()
                print(f"Username Penyewa: {username_penyewa}")
                print(f"Password : {password_penyewa}")
                print(f"Nomor NIK : {nik}")
                print("nomor telepon harus berupa 12 digit angka. Silakan coba lagi.")

                
        if cek_duplikasi(username_penyewa, nik, nomor_telepon):
            clear()
            print("\nPendaftaran gagal. Username, NIK, atau Nomor Telepon sudah terdaftar.\n")
        else:
            simpan_data([username_penyewa, password_penyewa, nik, nomor_telepon])
            clear()
            # print(f"Username Penyewa : {username_penyewa}")
            # print(f"Password : {password_penyewa}")
            # print(f"Nomor NIK : {nik}")
            # print(f"Nomor Telepon : {nomor_telepon}")
            print("\nPendaftaran berhasil. Silakan login.\n")

            while True:
                # clear()
                print("""
                                                1. LOGIN SEBAGAI PENYEWA
                                                2. EXIT
                """)
                garis("=")
                try:
                    pilih = int(input("Pilih Opsi yang tersedia >> "))
                    if pilih == 1:
                        # clear()
                        login_penyewa()
                    elif pilih == 2:
                        exit_program()
                    else:
                        print("Opsi yang Anda pilih tidak tersedia.")
                except ValueError:
                    print("Masukkan input dalam bentuk angka.")
                    break
            
def login_admin():
    while True:
        username_admin = input("Masukkan username: ")
        while len(username_admin) == 0:  
            print("Username tidak boleh kosong. Silakan coba lagi.")
            username_admin = input("Masukkan username baru: ")
        password_admin = input("Masukkan password: ")
        while len(password_admin) == 0:  
            print("Password tidak boleh kosong. Silakan coba lagi.")
            password_admin = input("Masukkan password baru: ")
        if cek_loginadmin(username_admin, password_admin):
            print("\nLogin berhasil sebagai Admin.")
            beranda_admin()
        else:
            print("Login gagal. Username atau password salah.")
            continue



def cek_loginadmin(username_admin, password_admin):
    file_admin = "dataadmin.csv" 
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
    

def login_penyewa():
    # clear()
    while True:
        username_penyewa = input("Masukkan username: ")
        password_penyewa = input("Masukkan password: ")
        if cek_loginpenyewa(username_penyewa, password_penyewa):
            print("Login berhasil sebagai Penyewa.")
            while True:
                clear()
                beranda_penyewa(username_penyewa)
                break  
            break 
        else:
            # clear()
            print("Login gagal. Username atau password salah.")
            continue  

def cek_loginpenyewa(username_penyewa, password_penyewa):
    file_penyewa = "datapenyewa.csv"  
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

def cek_duplikasi(username_penyewa, nik, nomor_telepon):
    file_penyewa = "datapenyewa.csv"  
    data = baca_data(file_penyewa)  
    for row in data:
        if row[0] == username_penyewa or row[2] == nik or row[3] == nomor_telepon:
            return True  
    return False

def simpan_data(data):
    file_penyewa = "datapenyewa.csv"  
    with open(file_penyewa, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def exit_program():
    clear()
    print("\n")
    print("Terima kasih telah menggunakan AGRIRENT(●'◡'●)\n\n".center(114))
    garis("=", 114)
    exit()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BERANDA PENYEWA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def beranda_penyewa(username_penyewa):
    while True:
        print(f"Selamat datang, {username_penyewa}!")
        print("""
                                                1. LIHAT STOK BARANG
                                                2. PENGEMBALIAN BARANG
                                                3. LOGOUT
        """)
        garis("=")
        try:
            pilihan = int(input("Pilih opsi yang tersedia >> "))
            if pilihan == 1:
                lihat_stok_barang(username_penyewa) 
            elif pilihan == 2:
                pengembalian_barang(username_penyewa)
            elif pilihan == 3:
                halaman_agrirent()  
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
                enter()
        except ValueError:
            print("Masukkan input dalam bentuk angka.")
            enter()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LIHAT STOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def lihat_stok_barang(username_penyewa):
    clear()
    stok_barang = baca_data_barang()
    if not stok_barang:
        print("Stok barang tidak tersedia atau file tidak ditemukan.")
        return None

    garis("=")
    print(f"{'Nama Barang':<30}{'Harga Sewa/Hari':<20}{'Total Stok':<10}")
    garis("-")
    for nama, info in stok_barang.items():
        print(f"{nama:<30}Rp {info['harga']:<19}{info['stok']:<10}")
    garis("=")
    
    while True:
        print("""
            1. Sewa Barang
            2. Kembali ke Menu
        """)
        garis("=")
        try:
            pilihan = int(input("Pilih Opsi yang tersedia >> "))
            if pilihan == 1:
                sewa_barang(stok_barang, username_penyewa)  
                break
            elif pilihan == 2:
                break  
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

def simpan_data_barang(stok_barang):
    with open('databarang.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama Barang', 'Harga Sewa', 'Total Stok'])
        for nama, info in stok_barang.items():
            writer.writerow([nama, info['harga'], info['stok']])


def sewa_barang(stok_barang, username_penyewa):
    if not stok_barang:
        print("Stok barang tidak ditemukan.")
        return None

    while True:
        nama_barang = input("Masukkan nama barang yang ingin disewa: ").upper()
        if len(nama_barang) == 0: 
            print("Nama barang tidak boleh kosong. Coba lagi.")  
        elif nama_barang in stok_barang:  
            break  
        else:
            print("Barang tidak ditemukan. Coba lagi.")  
        
    try:
        while True:
            try:
                jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin disewa: "))
                if jumlah <= 0:
                    print("Jumlah barang yang disewa harus lebih dari 0.")
                    continue
                elif jumlah > stok_barang[nama_barang]['stok']:
                    print("Stok tidak mencukupi.")
                    continue
                break  
            except ValueError:
                print("Jumlah barang harus berupa angka yang valid.")

     
        while True:
            try:
                tanggal_mulai_input = input("Masukkan tanggal penyewaan (DD-MM-YYYY): ")
                tanggal_mulai = dt.datetime.strptime(tanggal_mulai_input, "%d-%m-%Y")
                break 
            except ValueError:
                print("Format tanggal salah! Pastikan format yang benar adalah DD-MM-YYYY.")
        
     
        while True:
            try:
                durasi_hari = int(input("Masukkan durasi penyewaan (hari): "))
                if durasi_hari <= 0:
                    print("Durasi penyewaan harus lebih dari 0 hari.")
                    continue
                break  
            except ValueError:
                print("Durasi penyewaan harus berupa angka.")

      
        tanggal_kembali = tanggal_mulai + dt.timedelta(days=durasi_hari)
        
        
        print(f"Tanggal penyewaan: {tanggal_mulai.strftime('%d-%m-%Y')}")
        print(f"Tanggal pengembalian: {tanggal_kembali.strftime('%d-%m-%Y')}")

        total_harga = jumlah * stok_barang[nama_barang]['harga'] * durasi_hari

        
        stok_barang[nama_barang]['stok'] -= jumlah

        
        while True:
            username_input = input("Masukkan username Anda: ")
            if len(username_input) == 0 or username_input.isspace():  
                print("Username tidak boleh kosong. Coba lagi.")
            elif username_input != username_penyewa: 
                print("Username tidak sesuai dengan username login. Coba lagi.")
            else:
                username_penyewa = username_input
                break          

        
        status = "Disewa"

        simpan_data_barang(stok_barang)

        simpan_data_penyewaan([username_penyewa, nama_barang, jumlah, durasi_hari, total_harga, tanggal_mulai.strftime('%d-%m-%Y'), tanggal_kembali.strftime('%d-%m-%Y'), status])

        print(f"Barang berhasil disewa. Total harga: Rp {total_harga:,}")
        return username_penyewa, nama_barang, jumlah, durasi_hari, total_harga, tanggal_mulai, tanggal_kembali, status

    except ValueError as e:
        print("Input tidak valid. Pastikan memasukkan angka dan format tanggal yang benar.")
        
def simpan_data_penyewaan(data):
    file_penyewaan = "datapenyewaan.csv"
    with open(file_penyewaan, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        
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

def simpan_data_csv(file_barang, data):
    try:
        with open(file_barang, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except IOError:
        print("Terjadi kesalahan saat menyimpan data ke file.")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PENGEMBALIAN BARANG<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def pengembalian_barang(username_penyewa):
    clear()
    riwayat = baca_data('datapenyewaan.csv') 
    barang_disewa = []

    for data_barang in riwayat:
        username = data_barang[0]
        status = data_barang[7]

        if username == username_penyewa and status == "Disewa":
            barang_disewa.append(data_barang)
    
    if not barang_disewa:
        print("Tidak ada barang yang sedang Anda sewa.")
        enter()
        return
    
    print(f"Riwayat penyewaan untuk {username_penyewa}:\n")
    garis("=")
    print(f"{'No.':<5}{'Nama Barang':<30}{'Jumlah':<10}{'Durasi':<10}{'Total Harga':<15}{'Tanggal Kembali':<15}{'Status':<10}")
    garis("-")
    
    nomor = 1
    for data_barang in barang_disewa:
        nama_barang = data_barang[1]
        jumlah = data_barang[2]
        durasi = data_barang[3]
        total_harga = int(data_barang[4])
        tanggal_kembali = data_barang[6]
        status = data_barang[7]

        print(f"{nomor:<5}{nama_barang:<30}{jumlah:<10}{durasi:<10}Rp {total_harga:<13}{tanggal_kembali:<15}{status:<10}")
        nomor += 1
    garis("=")


    try:
        while True:
            no_barang = int(input("Masukkan nomor barang yang ingin dikembalikan: "))
            if no_barang < 1 or no_barang > len(barang_disewa):
                print("Nomor tidak valid.")
                continue
            else:
                break
               
        
        barang = barang_disewa[no_barang - 1]
        nama_barang, jumlah, total_harga, tanggal_kembali = barang[1], int(barang[2]), int(barang[4]), barang[6]
        tanggal_kembali = dt.datetime.strptime(tanggal_kembali, '%d-%m-%Y')
        hari_terlambat = (dt.datetime.now() - tanggal_kembali).days
        

        denda = 0
        if hari_terlambat > 0:
            denda = int(total_harga * 0.05 * hari_terlambat)
            print(f"\nAnda terlambat mengembalikan barang selama {hari_terlambat} hari.")
            print(f"Denda yang harus dibayar: Rp {denda:,}")
        
        total_bayar = total_harga + denda
        print(f"Total yang harus Anda bayar: Rp {total_bayar:,}")
        
        
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
        
        
        barang[7] = "Dikembalikan"
        simpan_data_csv('datapenyewaan.csv', riwayat)
        
        
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

def beranda_admin():
    while True:
        clear()
        print("""
                                                    BERANDA ADMIN
        """)
        garis("=")
        print("""
                                                1. MELIHAT STOK BARANG
                                                2. MELIHAT RIWAYAT PENYEWAAN
                                                3. LOGOUT
        """)
        garis("=")

        try:
            pilih = int(input("Pilih Opsi yang tersedia >> "))
            if pilih == 1:
                clear()
                menu_stok_barang()
            elif pilih == 2:
                clear()
                lihat_riwayat_penyewaan()
            elif pilih == 3:
                halaman_agrirent()
                break
            else:
                print("Opsi yang Anda pilih tidak tersedia.")
        except ValueError:
            print("Masukkan input dalam bentuk angka.")

def menu_stok_barang():
    while True:
        print("Stok Barang Saat Ini:\n")
        print('=' * 60)        
        barang = baca_data('databarang.csv') 
        
        if barang:
            barang = barang[1:]  
            print("No | Nama Barang          | Harga Barang     | Jumlah Stok |")
            print("-" * 60)
            for i, row in enumerate(barang):
                nama = row[0]
                harga = row[1]
                stok = row[2]
                print(f"{i + 1:<3} | {nama:<20} | Rp {harga:<12} | {stok:<5}       |")
        else:
            print("Tidak ada data barang saat ini.")
        print('=' * 60)

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

def tambah_stok_barang():
    barang = baca_data('databarang.csv')
    
    while True:
        nama_barang = input("Masukkan nama barang: ").upper()
        if len(nama_barang) == 0 or nama_barang.isspace():  
            print("Nama barang tidak boleh kosong. Coba lagi.") 
        else:
            break  

    barang_ditemukan = False
    for row in barang:
        if len(row) >= 3 and row[0].lower() == nama_barang.lower():
            try:
                jumlah_tambah = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
                row[2] = str(int(row[2]) + jumlah_tambah) 
                print(f"\nStok barang '{nama_barang}' berhasil ditambahkan sebanyak {jumlah_tambah}.")
                barang_ditemukan = True
                break
            except ValueError:
                print("Input jumlah stok harus berupa angka. Silakan coba lagi.")
                return

    if not barang_ditemukan:
        try:
            harga_barang = int(input("Masukkan harga barang: "))
            jumlah_stok = int(input("Masukkan jumlah stok barang: "))
            barang.append([nama_barang, str(harga_barang), str(jumlah_stok)])
            print(f"\nBarang baru '{nama_barang}' berhasil ditambahkan dengan harga {harga_barang} dan stok {jumlah_stok}.")
        except ValueError:
            print("Input harga dan stok harus berupa angka. Silakan coba lagi.")
            return

    try:
        with open('databarang.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(barang)
        print("\nPerubahan telah disimpan ke dalam file.")
    except IOError:
        print("Terjadi kesalahan saat menyimpan data ke file.")
    
    enter("")

def baca_data(file_barang):
    try:
        with open(file_barang, mode='r') as file:
            reader = csv.reader(file)
            return [row for row in reader if len(row) > 0]  
    except FileNotFoundError:
        print(f"File '{file_barang}' tidak ditemukan. Membuat file baru...")
        return []  

def lihat_riwayat_penyewaan():
    try:
        file_penyewaan = 'datapenyewaan.csv'
        riwayat_penyewaan = []

        with open(file_penyewaan, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  

            for row in reader:
                username_penyewa = row[0]
                nama_barang = row[1]
                jumlah = int(row[2])
                durasi_hari = int(row[3])
                total_harga = int(row[4])
                tanggal_mulai = row[5]
                tanggal_kembali = row[6]
                
                
                tanggal_kembali_obj = dt.datetime.strptime(tanggal_kembali, "%d-%m-%Y")
                hari_ini = dt.datetime.now()
                status = "Selesai" if hari_ini > tanggal_kembali_obj else "Sedang Berjalan"

                
                riwayat_penyewaan.append([
                    username_penyewa, nama_barang, jumlah, durasi_hari,
                    total_harga, tanggal_mulai, tanggal_kembali, status
                ])

        
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
        while True:
            # clear()
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
    clear()
    cover()
    enter("\nSELAMAT DATANG DI TEMPAT SEWA KAMI, AGRIRENT(oﾟvﾟ)ノ. ")
    halaman_agrirent()
    beranda_penyewa()
    pengembalian_barang()
    beranda_admin()
    lihat_riwayat_penyewaan()
