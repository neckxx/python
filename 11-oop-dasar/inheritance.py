class Hewan:
    def suara(self):
        print("Suara hewan")

class Kucing(Hewan):
    def suara(self):
        print("Meong!")

k = Kucing()
k.suara()