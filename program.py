'''
    yazar: dogan
    email: dogan@trabzon.edu.tr
    
    aciklama: Python programlama dilini
    bir ogrenci bilgi sistemi senaryosu ile
    ogreten bir repo (anaprogram dosyasi)
'''


if __name__ == '__main__':

    ogrenci_adlari = []
    ogrenci_soyadlari = []
    ogrenci_numaralari = []

    print('''
------------------------------------
Ogrenci Bilgi Sistemi v.1
------------------------------------
| Komut Listesi                    |
------------------------------------
| kapat   | Uygulamayi sonlandir   |
| ekle    | Ogrenci ekle           |
| sil     | Ogrenci siler          |
| listele | Ogrencileri listeler   |
------------------------------------        
''')
    # "kapat".strip()="kapat"   " kapat  ".strip()="kapat"
    # "kapat".lower()="kapat"   "KaPat".lower()="kapat" 
    # "kapat".upper()="KAPAT"   "KaPat".upper()="KAPAT" 
    komut = input('Komut giriniz:').strip().lower()
    while komut != 'kapat':
        if komut == 'ekle':
            print('------------------------------------')
            ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

            for sira in range(ogrenci_sayisi):
                ogrenci_adlari.append(input(f'{sira+1}. Ogrenci adini giriniz:'))       
                ogrenci_soyadlari.append(input(f'{sira+1}. Ogrenci soyadini giriniz:')) 
                ogrenci_numaralari.append(input(f'{sira+1}. Ogrenci numarasini giriniz:'))
            print('------------------------------------')
        elif komut == 'sil':
            print('------------------------------------')
            print('Ogrence silme kodlari!!!!')
            print('------------------------------------')
        elif komut == 'listele':
            print('------------------------------------')
            print('-' * 100)
            print(f'|{" "*2}| {"Isim":<12} | {"Soyisim":<8} | {"Numara":<4} |')
            print('-' * 100)
            for sira in range(len(ogrenci_adlari)):
                print(f'|{(sira+1):>2}| {ogrenci_adlari[sira]:<12} | {ogrenci_soyadlari[sira]:<8} | {ogrenci_numaralari[sira]:<4} |')
            print('------------------------------------')
        else:
            print('------------------------------------')
            print(f'"{komut}" seklinde tanimli bir komut bulanamadi!')
            print('------------------------------------')
        
        komut = input('Komut giriniz:').strip().lower()

    print('------------------------------------')
    print('Program sonlandirildi!')
    print('------------------------------------')











'''
    baslik = 'Ogrenci Bilgi Sistemi (v1)'

    print('-' * 100)
    print(f'| {baslik:<94} |x|')
    print('-' * 100)

    ogrenci_adlari = []
    ogrenci_soyadlari = []
    ogrenci_numaralari = []

    ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

    for sira in range(ogrenci_sayisi):
        ogrenci_adlari.append(input(f'{sira+1}. Ogrenci adini giriniz:'))       
        ogrenci_soyadlari.append(input(f'{sira+1}. Ogrenci soyadini giriniz:')) 
        ogrenci_numaralari.append(input(f'{sira+1}. Ogrenci numarasini giriniz:'))


    print('-' * 100)
    print(f'|{" "*9}| {"Isim":<35} | {"Soyisim":<25} | {"Numara":<20} |')
    print('-' * 100)
    for sira in range(ogrenci_sayisi):
        print(f'| {(sira+1):>7} | {ogrenci_adlari[sira]:<35} | {ogrenci_soyadlari[sira]:<25} | {ogrenci_numaralari[sira]:<20} |')
'''  
