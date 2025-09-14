class Manusia:
    def __init__(self, nama):
        self.nama = nama

    def perkenalan(self):
        print(f"Halo, saya {self.nama}")

m = Manusia("Raihan")
m.perkenalan()