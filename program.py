'''
    yazar: dogan
    email: dogan@trabzon.edu.tr
    
    aciklama: Python programlama dilini
    bir ogrenci bilgi sistemi senaryosu ile
    ogreten bir repo (anaprogram dosyasi)
'''


if __name__ == '__main__':

    baslik = 'Ogrenci Bilgi Sistemi (v1)'

    print(baslik)
    print(len(baslik))

    print('-' * 100)
    print(f'| {baslik:<94} |x|')
    print('-' * 100)
    
    ogrenci1_adi = input('1. Ogrenci adini giriniz:')
    ogrenci1_soyadi = input('1. Ogrenci soyadini giriniz:')
    ogrenci1_numara = input('1. Ogrenci numarasini giriniz:')

    ogrenci2_adi = input('2. Ogrenci adini giriniz:')
    ogrenci2_soyadi = input('2. Ogrenci soyadini giriniz:')
    ogrenci2_numara = input('2. Ogrenci numarasini giriniz:')

    ogrenci3_adi = input('3. Ogrenci adini giriniz:')
    ogrenci3_soyadi = input('3. Ogrenci soyadini giriniz:')
    ogrenci3_numara = input('3. Ogrenci numarasini giriniz:')

    '''
    | Isim                        | Soyisim                                       | Numara             |
    ----------------------------------------------------------------------------------------------------
    | ramazan                     | dogan                                         | 12345              |
    | hulya                       | dogan                                         | 12346              |
    '''

    print('-' * 100)
    print(f'|{" "*9}| {"Isim":<35} | {"Soyisim":<25} | {"Numara":<20} |')
    print('-' * 100)
    print(f'| {1:>7} | {ogrenci1_adi:<35} | {ogrenci1_soyadi:<25} | {ogrenci1_numara:<20} |')
    print(f'| {2:>7} | {ogrenci2_adi:<35} | {ogrenci2_soyadi:<25} | {ogrenci2_numara:<20} |')
    print(f'| {3:>7} | {ogrenci3_adi:<35} | {ogrenci3_soyadi:<25} | {ogrenci3_numara:<20} |')
    
