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
    
