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
    print('|',baslik,' '*(94-(len(baslik)+1)),'|x|')
    print('-' * 100)
    
    ogrenci_adi = input('Ogrenci adini giriniz:')
    ogrenci_soyadi = input('Ogrenci soyadini giriniz:')
    ogrenci_numara = input('Ogrenci numarasini giriniz:')

    '''
    | Isim                        | Soyisim                                       | Numara             |
    ----------------------------------------------------------------------------------------------------
    | ramazan                     | dogan                                         | 12345              |
    | hulya                       | dogan                                         | 12346              |
    '''

    print('-' * 100)
    print('|','Isim',' '*(94-(len(baslik)+1)),'|x|')
    print('-' * 100)



    # print('|',' '*96,'|')
    # print('|',' '*96,'|')
    # print('|',' '*96,'|')
    # print('|',' '*96,'|')
    # print('-' * 100)