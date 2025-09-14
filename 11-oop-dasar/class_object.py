class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):
        print(f"Halo, saya {self.nama}")

kucing = Hewan("Kucing")
kucing.sapa()