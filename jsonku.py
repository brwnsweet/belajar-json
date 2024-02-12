import json

class Jsonku:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def baca(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return "File tidak ditemukan."
    
    def tulis(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)


# Program Utama
if __name__ == "__main__":
    jsonku = Jsonku("data.json")
    
    data = {
        "pembeli": "Song Kang",
        "kasir": "Nuril",
        "barang": "kartu",
        "harga": 20000,
        "tempat": "toko bulan"
    }
    print(jsonku.tulis(data))
    # Membaca data dari file JSON
    print(jsonku.baca())     
