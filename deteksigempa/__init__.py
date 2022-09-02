import requests
from bs4 import BeautifulSoup


class GempaTerkini:
    def __init__(self):
        self.description = 'To get the latest earthquake in Indonesia from BMKG.go.id'
        self.result = None

    def ekstrasi_data(self):
        try:
            content = requests.get("https://www.bmkg.go.id/")
        except Exception:
            return None

        if content.status_code == 200:
            # print(content.text)
            # print(soup.prettify())
            # tanggal = soup.find('span', {'class':'waktu'})
            soup = BeautifulSoup(content.text, 'html.parser')
            results = soup.find('span', {'class': 'waktu'})
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
            self.result = hasil
        else:
            return None

    def tampilkan_data(self):
        if self.result is None:
            print("Tidak bisa menemukan data gempa terkini")
            return

        print('Gempa terkakhir berdasarkan BMKG')
        print(f"Tanggal {self.result['tanggal']}")
        print(f"Waktu {self.result['waktu']}")
        print(f"Magnitudo: {self.result['magnitudo']}")
        print(f"Kedalaman {self.result['kedalaman']}")
        print(f"Koordinat: LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(f"Lokasi {self.result['lokasi']}")
        print(f"{self.result['dirasakan']}")

    def run(self):
        self.ekstrasi_data()
        self.tampilkan_data()

if __name__ == "__main__":
    gempa_di_indonesia = GempaTerkini()
    print('Deskripsi package', gempa_di_indonesia.description)
    gempa_di_indonesia.run()
    # gempa_di_indonesia.ekstrasi_data()
    # gempa_di_indonesia.tampilkan_data()



