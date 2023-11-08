import requests
from bs4 import BeautifulSoup


def extraction():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            # print(i , res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['ls'] = ls
        hasil['bt'] = bt
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None



def show_data(result):
    if result is None:
        print('Tidak menemukan data gempa terkini')
        return

    print('Gempa terakhir berrdasarkan BMKG')
    print(f'Tanggal : {result['tanggal']}')
    print(f'Waktu : {result['waktu']}')
    print(f'Magnitudo : {result['magnitudo']}')
    print(f'Kedalaman : {result['kedalaman']}')
    print(f'Koordinat : LS={result['ls']}, BT={result['bt']}')
    print(f'Lokasi : {result['lokasi']}')
    print(f'Dirasakan : {result['dirasakan']}')

    return result
