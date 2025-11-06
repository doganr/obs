'''
    yazar: dogan
    email: dogan@trabzon.edu.tr
    
    aciklama: Python programlama dilini
    bir ogrenci bilgi sistemi senaryosu ile
    ogreten bir repo (anaprogram dosyasi)
'''


if __name__ == '__main__':

    #                       0            ,  1       ,  2 
    ogrenci_adlari =     ['Ramazan Ozgur', 'Hulya'  , 'Yigit Kagan']
    ogrenci_soyadlari =  ['Dogan'        , 'Yaldiz' ,    'Caliskan']
    ogrenci_numaralari = ['12345'        , '12346'  ,       '12347']

    print('''
----------------------------------------
Ogrenci Bilgi Sistemi v.1
----------------------------------------
| Komut Listesi                        |
----------------------------------------
| kapat   | Uygulamayi sonlandir       |
| ekle    | Ogrenci ekle               |
| sil     | Ogrenci siler              |
| listele | Ogrencileri listeler       |
----------------------------------------        
''')
    # "kapat".strip()="kapat"   " kapat  ".strip()="kapat"
    # "kapat".lower()="kapat"   "KaPat".lower()="kapat" 
    # "kapat".upper()="KAPAT"   "KaPat".upper()="KAPAT" 
    komut = input('Komut giriniz:').strip().lower()
    while komut != 'kapat':
        if komut == 'ekle':
            print('----------------------------------------')
            ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

            for sira in range(ogrenci_sayisi):
                ogrenci_adlari.append(input(f'{sira+1}. Ogrenci adini giriniz:'))       
                ogrenci_soyadlari.append(input(f'{sira+1}. Ogrenci soyadini giriniz:')) 
                ogrenci_numaralari.append(input(f'{sira+1}. Ogrenci numarasini giriniz:'))
            print('----------------------------------------')
        elif komut == 'sil':
            print('----------------------------------------')
            ogrenci_numarasi = input('Ogrenci numarasini giriniz:')

            try:
                index = ogrenci_numaralari.index(ogrenci_numarasi)

                ogrenci_numaralari.pop(index)
                ogrenci_adlari.pop(index)
                ogrenci_soyadlari.pop(index)
                print(f'{ogrenci_numarasi} numarali ogrenci silindi!')
            except ValueError:
                print(f'{ogrenci_numarasi} numarali bir ogrenci yok!')

            #index = -1
            #for numara in ogrenci_numaralari:
            #    if numara == ogrenci_numarasi:
            #        index = ogrenci_numaralari.index(numara)

            #index = -1
            #for i, numara in enumerate(ogrenci_numaralari):
            #    if numara == ogrenci_numarasi:
            #        index = i 

            '''
            index = ogrenci_numaralari.index(ogrenci_numarasi)
                        
            if index == -1:
                print(f'{ogrenci_numarasi} numarali bir ogrenci yok!')
            else:
                ogrenci_numaralari.pop(index)
                ogrenci_adlari.pop(index)
                ogrenci_soyadlari.pop(index)
                print(f'{ogrenci_numarasi} numarali ogrenci silindi!')
            '''
            
            print('----------------------------------------')
        elif komut == 'listele':
            print('----------------------------------------')
            print('-' * 40)
            print(f'|{" "*2}| {"Isim":<13} | {"Soyisim":<8} | {"Numara":<5} |')
            print('-' * 40)
            for sira in range(len(ogrenci_adlari)):
                print(f'|{(sira+1):>2}| {ogrenci_adlari[sira]:<13} | {ogrenci_soyadlari[sira]:<8} | {ogrenci_numaralari[sira]:<5} |')
            print('----------------------------------------')
        else:
            print('----------------------------------------')
            print(f'"{komut}" seklinde tanimli bir komut bulanamadi!')
            print('----------------------------------------')
        
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
