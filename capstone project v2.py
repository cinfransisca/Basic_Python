data = {
        'A001': {   'Kode barang': 'A001',
                    'Nama barang': 'T-shirt Adidas',
                    'Qty': 5,
                    'Harga satuan': 250000,
                    'Tanggal penjualan': '2020-03-01'},
        'B002': {   'Kode barang': 'B002',
                    'Nama barang': 'Kemeja Uniqlo',
                    'Qty': 10,
                    'Harga satuan': 300000,
                    'Tanggal penjualan': '2020-03-01'},
        'C002': {   'Kode barang': 'C002',
                    'Nama barang': 'Celana Uniqlo',
                    'Qty': 7,
                    'Harga satuan': 400000,
                    'Tanggal penjualan': '2020-03-02'},
        'D005': {   'Kode barang': 'D005',
                    'Nama barang': 'Topi Zara',
                    'Qty': 3,
                    'Harga satuan': 350000,
                    'Tanggal penjualan': '2020-03-05'}
        }


def tampilkan_seluruh_data():
    print(f'\nDATA PENJUALAN BARANG')
    print('____________________________________________________________________________________')
    print('Kode barang\t|Nama barang\t\t|Qty\t|Harga satuan\t|Tanggal penjualan')
    print('____________________________________________________________________________________')
    for i in data.keys():
        print(data[i]['Kode barang'] + '\t\t|' + data[i]['Nama barang'] + '\t\t|' + str(data[i]['Qty']) + '\t|' + str(data[i]['Harga satuan']) + '\t\t|' + data[i]['Tanggal penjualan'])
    print('____________________________________________________________________________________')
    
def tampilkan(kode='',nama='', qty='', harga='', tanggal=''):
    print(f'\nDATA PENJUALAN BARANG {kode}')
    print('____________________________________________________________________________________')
    print('Kode barang\t|Nama barang\t\t|Qty\t|Harga satuan\t|Tanggal penjualan')
    print('____________________________________________________________________________________')
    print(f'{kode}\t\t|{nama}\t\t|{qty}\t|{harga}\t\t|{tanggal}')
    print('____________________________________________________________________________________')

def tampilkan_data_berdasarkan_kode(kode):
    nama = data[kode]['Nama barang']
    qty = data[kode]['Qty']
    harga = data[kode]['Harga satuan']
    tanggal = data[kode]['Tanggal penjualan']
    
    tampilkan(kode, nama, qty, harga, tanggal)

def tampilkan_data_dengan_kolom_diubah(kode, kolom, nilai):
    nama = data[kode]['Nama barang']
    qty = data[kode]['Qty']
    harga = data[kode]['Harga satuan']
    tanggal = data[kode]['Tanggal penjualan']
    
    if kolom.lower() == 'nama barang':
        nama = nilai
    elif kolom.lower() == 'qty':
        qty = nilai
    elif kolom.lower() == 'harga satuan':
        harga = nilai
    else:
        tanggal = nilai

    tampilkan(kode, nama, qty, harga, tanggal)    

def tambah_data(kode, nama, qty, harga, tanggal):
    data[kode] = { 'Kode barang': kode,
                    'Nama barang': nama,
                    'Qty': qty,
                    'Harga satuan': harga,
                    'Tanggal penjualan': tanggal}


def ubah_data(kode, kolom, nilai):
    data[kode][kolom] = nilai


def hapus_data(kode):
    data.pop(kode)


def menu_menampilkan_data():
    menu1 = 'jalan'
        
    while menu1 == 'jalan':
        print('''
======================= MENU 1 =======================
1. Menampilkan seluruh data penjualan barang
2. Menampilkan data untuk kode barang yang diinginkan
3. Kembali ke menu utama            
            ''')
        
        submenu = input('Masukan angka menu yang ingin dijalankan: ')
        
        if submenu == '1':
            if len(data) == 0:
                print('\n======= Tidak ada data penjualan, silakan tambahkan data pada menu =======')
            else:
                tampilkan_seluruh_data()
        
        elif submenu == '2':
            if len(data) != 0:
                kode = input('\nMasukan kode barang yang ingin ditampilkan: ').upper()
                
                if kode in data.keys():
                    tampilkan_data_berdasarkan_kode(kode) 
                
                else:
                    print('\n##### Data yang ingin ditampilkan tidak ada #####')
            
            else:
                print('\n======= Tidak ada data penjualan, silakan tambahkan data pada menu =======')

        elif submenu == '3':
            menu1 = 'berhenti'
        
        else:
            print('\n##### Masukan angka sesuai pilihan menu #####') 


def menu_menambahkan_data():
    menu2 = 'jalan'
        
    while menu2 == 'jalan':
        print('''
======================= MENU 2 =======================
1. Menambah data penjualan barang
2. Kembali ke menu utama            
                ''')
        
        submenu = input('Masukan angka menu yang ingin dijalankan: ')
        
        if submenu == '1': 
            kode = input('\nMasukan kode barang yang ingin ditambahkan: ').upper()

            if  kode in data.keys():
                print('\n##### Data yang ingin ditambahkan sudah ada #####')
            
            else:
                nama = input('Masukan nama barang: ')
                
                qty = input('Masukan qty barang: ')
                while not qty.isdecimal():
                    print('\n######### Qty harus berupa angka #########\n')
                    qty = input('Masukan qty barang: ')

                harga = input('Masukan harga satuan barang: ')
                while not harga.isdecimal():
                    print('\n######### Harga satuan harus berupa angka #########\n')
                    harga = input('Masukan harga satuan barang: ')

                tanggal = input('Masukan tanggal penjualan barang: ')

                konfirmasi_ubah = 'menunggu'
                while konfirmasi_ubah == 'menunggu':
                    tampilkan(kode, nama, qty, harga, tanggal)
                    tambah = input(f'\nApakah anda ingin menambah data {kode}? (ya/tidak): ')
                    
                    if tambah.lower() == 'ya':
                        tambah_data(kode, nama, int(qty), int(harga), tanggal)
                        print(f'\n============= Data {kode} berhasil ditambahkan =============')
                        konfirmasi_ubah = 'selesai'
                    elif tambah.lower() == 'tidak':
                        print(f'\n============= Tambah data {kode} dibatalkan =============')
                        konfirmasi_ubah = 'selesai'
                    else:
                        print('\nJawab dengan \'ya\' atau \'tidak\'')
        
        elif submenu == '2':
            menu2 = 'berhenti'

        else:
            print('\n##### Masukan angka sesuai pilihan menu #####')  


def menu_mengubah_data():
    menu3 = 'jalan'
    while menu3 == 'jalan':
        print('''
======================= MENU 3 =======================
1. Mengubah data penjualan barang
2. Kembali ke menu utama            
                ''')
        submenu = input('Masukan angka menu yang ingin dijalankan: ')
        
        if submenu == '1':
            
            if len(data) != 0:
                tampilkan_seluruh_data()
                kode = input('\nMasukan kode barang yang ingin diubah: ').upper()
                
                if kode in data.keys():
                    
                    lanjut_ubah = 'jalan'
                    while lanjut_ubah == 'jalan':
                        tampilkan_data_berdasarkan_kode(kode)
                        ubah = input(f'\nApakah anda ingin mengubah data {kode}? (ya/tidak): ')
                        
                        if ubah.lower() == 'ya':
                            
                            kolom = input('Masukan nama kolom yang ingin diubah: ')

                            if kolom.lower() == 'kode barang':
                                print('\n##### Tidak dapat mengubah kode barang, silakan tambahkan kode baru pada menu #####')
                            
                            elif kolom.lower() in [keys.lower() for keys in data[kode].keys()]:
                                
                                if (kolom.lower() == 'qty') or (kolom.lower() == 'harga satuan'):
                                    nilai =  input(f'Masukan {kolom.lower()} yang baru: ')
                                    while not nilai.isdecimal():
                                        print(f'\n######### {kolom.capitalize()} harus berupa angka #########\n')
                                        nilai =  input(f'Masukan {kolom.lower()} yang baru: ')
                                else:
                                    nilai =  input(f'Masukan {kolom.lower()} yang baru: ')


                                konfirmasi_simpan = 'menunggu'
                                while konfirmasi_simpan == 'menunggu':
                                        tampilkan_data_dengan_kolom_diubah(kode, kolom.capitalize(), nilai)
                                        ubah = input('\nApakah anda ingin menyimpan perubahan data? (ya/tidak): ')
                                        
                                        if ubah.lower() == 'ya':
                                            if (kolom.lower() == 'qty') or (kolom.lower() == 'harga satuan'):
                                                ubah_data(kode, kolom.capitalize(), int(nilai))
                                                print(f'\n============= Ubah data {kode} berhasil =============')
                                                konfirmasi_simpan = 'selesai'
                                            else:
                                                ubah_data(kode, kolom.capitalize(), nilai)
                                                print(f'\n============= Ubah data {kode} berhasil =============')
                                                konfirmasi_simpan = 'selesai'            
                                        
                                        elif ubah.lower() == 'tidak':
                                            print(f'\n============= Ubah data {kode} dibatalkan =============')
                                            konfirmasi_simpan = 'selesai'
                                        
                                        else:
                                            print('\nJawab dengan \'ya\' atau \'tidak\'')

                            else:
                                print('\n##### Kolom yang ingin diubah tidak ada #####')
                            
                            lanjut_ubah = 'berhenti'
                        
                        elif ubah.lower() == 'tidak':
                            print(f'\n============= Ubah data {kode} dibatalkan =============')
                            lanjut_ubah = 'berhenti'
                        else:
                            print('\nJawab dengan \'ya\' atau \'tidak\'')

                else:
                    print('\n##### Data yang ingin diubah tidak ada #####') 

            else:
                print('\n======= Tidak ada data penjualan, silakan tambahkan data pada menu =======')
    
        elif submenu == '2':
            menu3 = 'berhenti'
        
        else:
                print('\n##### Masukan angka sesuai pilihan menu #####')

def menu_menghapus_data():
    menu4 = 'jalan'
    while menu4 == 'jalan':
        print('''
======================= MENU 4 =======================
1. Menghapus data penjualan barang
2. Kembali ke menu utama            
            ''')
        submenu = input('Masukan angka menu yang ingin dijalankan: ')
        
        if submenu == '1':
            
            if len(data) != 0:
                tampilkan_seluruh_data()
                kode = input('\nMasukan kode barang yang ingin dihapus: ').upper()
                
                if kode in data.keys():
                    
                    konfirmasi_hapus = 'menunggu'
                    while konfirmasi_hapus == 'menunggu':
                        tampilkan_data_berdasarkan_kode(kode)
                        hapus = input(f'\nApakah anda ingin menghapus data {kode}? (ya/tidak): ')
                        
                        if hapus.lower() == 'ya':
                            hapus_data(kode)
                            print(f'\n============= Data {kode} berhasil dihapus =============')
                            konfirmasi_hapus = 'selesai'
                        elif hapus.lower() == 'tidak':
                            print(f'\n============= Hapus data {kode} dibatalkan =============')
                            konfirmasi_hapus = 'selesai'
                        else:
                            print('\nJawab dengan \'ya\' atau \'tidak\'')

                else:
                    print('\n##### Data yang ingin dihapus tidak ada #####')    
            
            else:
                print('\n======= Tidak ada data penjualan, silakan tambahkan data pada menu =======')

        elif submenu == '2':
            menu4 = 'berhenti'
        
        else:
            print('\n##### Masukan angka sesuai pilihan menu #####') 


program = 'jalan'

while program == 'jalan':
    print('''
SELAMAT DATANG DI PROGRAM PENJUALAN TOKO
=============================================
Menu 1  : Menampilkan data penjualan barang
Menu 2  : Menambahkan data penjualan barang
Menu 3  : Mengubah data penjualan barang
Menu 4  : Menghapus data penjualan barang
Menu 5  : Exit program
=============================================
        ''')

    menu = input('Masukan angka menu yang ingin dijalankan: ')

    if menu == '1':
        menu_menampilkan_data()

    elif menu == '2':
        menu_menambahkan_data()
        
    elif menu == '3':
        menu_mengubah_data()
    
    elif menu == '4':
        menu_menghapus_data()

    elif menu == '5':
        print('\n================ Exit program ================\n')
        program = 'berhenti'
    
    else:
        print('\n##### Masukan angka sesuai pilihan menu #####\n')