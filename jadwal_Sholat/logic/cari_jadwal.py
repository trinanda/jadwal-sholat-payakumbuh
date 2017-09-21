from jadwal_Sholat.data.data_bs4 import cari

def jadwal():
    LAGI = 'Y'
    while LAGI == 'Y':

        dictionary = {}

        for k in cari:
            a = k.find_all('td')
            for j,r in enumerate(a):

                print(j,r)

                if j == 0:
                    dictionary['no'] = r.get_text()
                elif j == 1:
                    dictionary['Imsyak'] = r.get_text()
                elif j == 2:
                    dictionary['Shubuh'] = r.get_text()
                elif j == 3:
                    dictionary['Terbit'] = r.get_text()
                elif j == 4:
                    dictionary['Dzuhur'] = r.get_text()
                elif j == 5:
                    dictionary['Ashr'] = r.get_text()
                elif j == 6:
                    dictionary['Maghrib'] = r.get_text()
                elif j == 7:
                    dictionary['Isya'] = r.get_text()

        print('')
        print('BERIKUT ADALAH DATA')
        print('-------------------')
        print('Imsyak')
        print('Shubuh')
        print('Terbit')
        print('Dzuhur')
        print('Ashr')
        print('Maghrib')
        print('Isya')
        print('')


        jadwal = input('Anda ingin melihat jadwal sholat apa: ')

        if jadwal in dictionary:
            print('Sholat',jadwal,'masukan pada pukul',dictionary[jadwal])
        else:
            print('keyword yang anda masukan salah, program ini masih case sensitif, mohon masukan data sesusai dengan data di atas')

        print('')
        LAGI = input('Ingin melihat jadwal sholat lagi..? (tekan Y)')

    return LAGI

