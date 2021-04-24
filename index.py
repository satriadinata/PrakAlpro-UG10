# program menghitung utang jajan warung
utang={'dinda':1000, 'jordi':1500,'joni':2000}
while True:
    print('Menu Utang:\n1. Tambah daftar\n2. Lihat daftar\n3. Keluar')
    choose=input('Pilih Menu :')
    if choose=='1':
        name=input('Nama : ')
        nominal=int(input('Nominal utang : '))
        if name in utang:
            utang[name]+=nominal
        else:
            utang[name]=nominal
    elif choose=='2':
        print('Nama\t\tNominal\n')
        for key in utang:
            print(str(key)+'\t\t'+str(utang[key]))
    elif choose=='3':
        break
    else:
        print('Tidak ada menu\n')