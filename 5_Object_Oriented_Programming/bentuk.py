# #Problem 1.1 Easy
import unittest
class Bentuk:
    def luas(self):
        pass
    
    def keliling(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi * self.sisi
    
    def keliling(self):
        return 4 * self.sisi

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return 0.5 * self.alas * self.tinggi
    
    def keliling(self):
        return self.alas + self.tinggi + (self.alas ** 2 + self.tinggi ** 2) ** 0.5

class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        return self.panjang * self.lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

def main():
    persegi = Persegi(4)
    segitiga = Segitiga(3, 4)
    persegipanjang = PersegiPanjang(7, 8)

    print("======== Easy 1========","\n")
    print("======== Luas ========")
    print("Persegi:", persegi.luas())
    print("Segitiga:", segitiga.luas())
    print("Persegi Panjang:", persegipanjang.luas(),"\n")
    
    print("====== Keliling ======")
    print("Persegi:", persegi.keliling())
    print("Segitiga:", segitiga.keliling())
    print("Persegi Panjang:", persegipanjang.keliling())

main()