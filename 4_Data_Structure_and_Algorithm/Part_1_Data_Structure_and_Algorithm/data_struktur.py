# #Problem1
import unittest


def hapus_duplikasi(arraylist):
    if not arraylist:
        return 0
    
    seen = {}
    unique_count = 0
    
    for item in arraylist:
        if item not in seen:
            seen[item] = True
            unique_count += 1
    
    return unique_count

# Test cases
print("where input [2, 3, 3, 3, 6, 9, 9] :", 
      hapus_duplikasi([2, 3, 3, 3, 6, 9, 9]))  
print("where input [2, 3, 4, 5, 6, 9, 9] :",
      hapus_duplikasi([2, 3, 4, 5, 6, 9, 9]))  
print("where input [2, 2, 2, 11] :",
      hapus_duplikasi([2, 2, 2, 11]))         
print("where input [2, 2, 2, 11]] :",
      hapus_duplikasi([1, 2, 3, 11, 11]))     


#Problem 2
def bilangan_prima(x):
    def is_prima(angka):
        if angka <= 1:
            return False
        if angka == 2:
            return True  
        if angka % 2 == 0:
            return False
        sqrt_angka = int(angka**0.5) + 1
        for i in range(3, sqrt_angka, 2):
            if angka % i == 0:
                return False
        return True
    
    count = 0
    angka = 2
    while True:
        if is_prima(angka):
            count += 1
            if count == x:
                return angka
        angka += 1

print("where input 1 : ",bilangan_prima(1))  
print("where input 5 : ",bilangan_prima(5))  
print("where input 8 : ",bilangan_prima(8)) 
print("where input 9 : ",bilangan_prima(9)) 
print("where input 10 : ",bilangan_prima(10)) 

#Problem 3
def deret_fibonacci(angka):
    if angka <= 1:
        return angka
    
    sebelumnya, sekarang = 0, 1
    for _ in range(2, angka + 1):
        sebelumnya, sekarang = sekarang, sebelumnya + sekarang
    
    return sekarang

# Test cases
print("input (0) :",deret_fibonacci(0))  
print("input (1) :",deret_fibonacci(1))  
print("input (2) :",deret_fibonacci(2))   
print("input (9) :",deret_fibonacci(9))   
print("input (10) :",deret_fibonacci(10))  
print("input (12) :",deret_fibonacci(12)) 
print("input (15) :",deret_fibonacci(15)) 

#Problem 4
def generate_grid_lebar_tinggi(lebar, tinggi, mulai):
    def is_prime(angka):
        if angka <= 1:
            return False
        if angka == 2:
            return True  
        if angka % 2 == 0:
            return False
        sqrt_angka = int(angka**0.5) + 1
        for i in range(3, sqrt_angka, 2):
            if angka % i == 0:
                return False
        return True
    
    result = ""
    sekarang = mulai
    for h in range(tinggi):
        for w in range(lebar):
            while not is_prime(sekarang):
                sekarang += 1
            result += str(sekarang) + " "
            sekarang += 1
        result += "\n"
    
    return result.strip()


print("where input :(2, 3, 13)","\n",generate_grid_lebar_tinggi(2, 3, 13))
print("====================")
print("where input :(2, 3, 13)","\n",generate_grid_lebar_tinggi(5, 2, 1))

#Problem 5
def max_sequence(arr):
    if not arr:
        return 0
    
    penjumlahan_maksimal = float('-inf')
    penjumlahan_sekarang = 0
    
    for num in arr:
        penjumlahan_sekarang = max(num, penjumlahan_sekarang + num)
        penjumlahan_maksimal = max(penjumlahan_maksimal, penjumlahan_sekarang)
    
    return penjumlahan_maksimal

# Test cases
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  
print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))   
print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))   
print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))   
print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))    


