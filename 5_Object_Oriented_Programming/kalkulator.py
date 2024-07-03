#Problem2 Medium

class Kalkulator:
    @staticmethod
    def penjumlahan(a, b):
        return a + b
    
    @staticmethod
    def pengurangan(a, b):
        return a - b
    
    @staticmethod
    def perkalian(a, b):
        return a * b
    
    @staticmethod
    def pembagian(a, b):
        return a / b

def main():
    print("====== Medium 1 ======")
    print("Penjumlahan:", Kalkulator.penjumlahan(3, 4))
    print("Pengurangan:", Kalkulator.pengurangan(15, 4))
    print("Perkalian:", Kalkulator.perkalian(10, 10))
    print("Pembagian:", Kalkulator.pembagian(12, 3))

main()
