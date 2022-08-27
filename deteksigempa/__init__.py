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
        dirasakan = None

        for res in result3:
            # print(i, res)
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
        hasil['koordinat'] = {'ls':ls, 'bt':bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan

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
    print(f"Koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"{result['dirasakan']}")

if __name__ == "__main__":
    result = ekstrasi_data()
    tampilkan_data(result)



