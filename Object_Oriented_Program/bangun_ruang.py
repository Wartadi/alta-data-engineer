#Problem 2 Easy

class Bangun_Ruang:
    def volume(self):
        pass

class Kubus(Bangun_Ruang):
    def __init__(self, sisiv):
        self.sisiv = sisiv
    
    def volume(self):
        return self.sisiv ** 3

class Balok(Bangun_Ruang):
    def __init__(self, panjangv, lebarv, tinggiv):
        self.panjangv = panjangv
        self.lebarv = lebarv
        self.tinggiv = tinggiv
    
    def volume(self):
        return self.panjangv * self.lebarv * self.tinggiv

class Silinder(Bangun_Ruang):
    def __init__(self, radius, tinggiv):
        self.radius = radius
        self.tinggiv = tinggiv
    
    def volume(self):
        return 3.14 * self.radius ** 2 * self.tinggiv

def main():
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Silinder(7, 10)
    
    print("======= Easy 2 =======")
    print("Volume")
    print("Kubus:", kubus.volume())
    print("Balok:", balok.volume())
    print("Tabung:", tabung.volume())

main()

