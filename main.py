"""
 Aplikasi deteksi gempa
"""

#from deteksigempa import ekstrasi_data, tampilkan_data
import deteksigempa

if __name__ == '__main__':
    print("Aplikasi Utama")
    result = deteksigempa.ekstrasi_data()
    deteksigempa.tampilkan_data(result)