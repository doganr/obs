'''
    yazar: dogan
    email: dogan@trabzon.edu.tr
    
    aciklama: Python programlama dilini
    bir ogrenci bilgi sistemi senaryosu ile
    ogreten bir repo (anaprogram dosyasi)
'''


if __name__ == '__main__':

    baslik = 'Ogrenci Bilgi Sistemi (v1)'

    print('-' * 100)
    print(f'| {baslik:<94} |x|')
    print('-' * 100)

    ogrenci_adlari = []
    ogrenci_soyadlari = []
    ogrenci_numaralari = []
    
    ogrenci_adlari.append(input('1. Ogrenci adini giriniz:'))       # 0. indeks
    ogrenci_soyadlari.append(input('1. Ogrenci soyadini giriniz:')) # 0. indeks
    ogrenci_numaralari.append(input('1. Ogrenci numarasini giriniz:')) # 0. indeks

    ogrenci_adlari.append(input('2. Ogrenci adini giriniz:')) # 1. indeks
    ogrenci_soyadlari.append(input('2. Ogrenci soyadini giriniz:')) # 1. indeks
    ogrenci_numaralari.append(input('2. Ogrenci numarasini giriniz:')) # 1. indeks

    ogrenci_adlari.append(input('3. Ogrenci adini giriniz:')) # 2. indeks
    ogrenci_soyadlari.append(input('3. Ogrenci soyadini giriniz:')) # 2. indeks
    ogrenci_numaralari.append(input('3. Ogrenci numarasini giriniz:')) # 2. indeks


    '''
    | Isim                        | Soyisim                                       | Numara             |
    ----------------------------------------------------------------------------------------------------
    | ramazan                     | dogan                                         | 12345              |
    | hulya                       | dogan                                         | 12346              |
    '''

    print('-' * 100)
    print(f'|{" "*9}| {"Isim":<35} | {"Soyisim":<25} | {"Numara":<20} |')
    print('-' * 100)
    print(f'| {1:>7} | {ogrenci_adlari[0]:<35} | {ogrenci_soyadlari[0]:<25} | {ogrenci_numaralari[0]:<20} |')
    print(f'| {2:>7} | {ogrenci_adlari[1]:<35} | {ogrenci_soyadlari[1]:<25} | {ogrenci_numaralari[1]:<20} |')
    print(f'| {3:>7} | {ogrenci_adlari[2]:<35} | {ogrenci_soyadlari[2]:<25} | {ogrenci_numaralari[2]:<20} |')
    
