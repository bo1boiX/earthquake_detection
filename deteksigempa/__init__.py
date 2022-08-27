import requests
from bs4 import BeautifulSoup


def ekstrasi_data():
    try:
        content = requests.get("https://www.bmkg.go.id/")
    except Exception:
        return None

    if content.status_code == 200:
        # print(content.text)
        # print(soup.prettify())
        # tanggal = soup.find('span', {'class':'waktu'})
        soup = BeautifulSoup(content.text, 'html.parser')
        results = soup.find('span', {'class':'waktu'})
        results = results.text.split(', ')
        waktu = results[1]
        tanggal = results[0]
        # print(tanggal.string)
        result2 = soup.find('div', {'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result3 = result2.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        lokasi = None

        for res in result3:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:


            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls':7.77, 'bt': 111.98}
        hasil['lokasi'] = 'Pusat gempa berada di darat 9 km BaratLaut Kota Kediri'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Kediri, II Barong, II Nganjuk'

        return hasil
    else:
        return None
"""
Tanggal : 26 Agustus 2022,
Waktu : 04:55:24 WIB
Magnitudo : 3.7
Kedalamanan : 9 km
Lokasi : 7.77 LS - 111.98 BT
Pusat Gempa : Pusat gempa berada di darat 9 km BaratLaut Kota Kediri
Dirasakan : Dirasakan (Skala MMI): II Kediri, II Barong, II Nganjuk
 """


def tampilkan_data(result):
    print('Gempa terkakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa {result['pusat_gempa']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__ == "__main__":
    result = ekstrasi_data()
    tampilkan_data(result)



