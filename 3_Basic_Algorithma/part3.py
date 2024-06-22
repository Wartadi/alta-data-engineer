###############  PART 3 : BASIC BRANCHING, LOOPING & FUNCTION

## Problem 1 = Nilai Siswa
# def konversi_nilai(student_score):
#     if 80 <= student_score <= 100:
#         return "Nilai A"
#     elif 65 <= student_score <= 79:
#         return "Nilai B+"
#     elif 50 <= student_score <= 64:
#         return "Nilai B"
#     elif 35 <= student_score <= 49:
#         return "Nilai C"
#     elif 5 <= student_score <= 34:
#         return "Nilai D"
#     else:
#         return "Nilai tidak valid"

# ### input
# student_name = input("Masukkan nama mahasiswa: ")
# student_score = int(input("Masukkan nilai mahasiswa: "))

# nilai_huruf = konversi_nilai(student_score)
# print (nilai_huruf)

########## Problem 2 #########
# 2.1
# def faktor_bilangan_ascending(number):
#     factors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             factors.append(i)
#     return factors

# number = int(input("Masukkan bilangan: "))
# factors = faktor_bilangan_ascending(number)
# print("Faktor dari", number, "adalah:")
# for factor in factors:
#     print(factor)

# # 2.2
# def faktor_bilangan_descending(number):
#     factors = []
#     for i in range(number, 0, -1):
#         if number % i == 0:
#             factors.append(i)
#     return factors


# number = int(input("Masukkan bilangan: "))
# factors = faktor_bilangan_descending(number)
# print("Faktor dari", number, "adalah:")
# for factor in factors:
#     print(factor)

# 2.3

# def prime_number(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# print("Input number 11 adalah",prime_number(11))  # True
# print("Input number 13 adalah",prime_number(13))  # True
# print("Input number 17 adalah",prime_number(17))  # True
# print("Input number 20 adalah",prime_number(20))  # False
# print("Input number 35 adalah",prime_number(35))  # False

# # 2.4 
# def palindrome(input_string):
#     # Menghilangkan spasi dan mengubah string menjadi huruf kecil
#     clean_string = input_string.replace(" ", "").lower()
#     # Membandingkan string dengan kebalikannya
#     return clean_string == clean_string[::-1]

# print("civic \t\t=",palindrome("civic"))       # True
# print("katak \t\t=",palindrome("katak"))       # True
# print("kasur rusak \t=", palindrome("kasur rusak")) # True
# print("kupu-kupu \t=",palindrome("kupu-kupu"))   # False
# print("lion \t\t=",palindrome("lion"))        # False

# 2.5 Pangkat

# def pangkat(base, exponent):
#     return base ** exponent

# print(" 2 pangkat 3 \t=",pangkat(2, 3))  # 8
# print(" 5 pangkat 3 \t=",pangkat(5, 3))  # 125
# print(" 10 pangkat 2 \t=",pangkat(10, 2)) # 100
# print(" 2 pangkat 5 \t=",pangkat(2, 5))  # 32
# print(" 7 pangkat 3 \t=",pangkat(7, 3))  # 343

##2.6
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def full_prima(N):
    if not is_prime(N):
        return False
    for digit in str(N):
        if not is_prime(int(digit)):
            return False
    return True

print("input 2 \t=",full_prima(2))   # True
print("input 3 \t=",full_prima(3))   # True
print("input 11 \t=",full_prima(11))  # False
print("input 13 \t=",full_prima(13))  # False
print("input 23 \t=",full_prima(23))  # True
print("input 29 \t=",full_prima(29))  # False
print("input 37 \t=",full_prima(37))  # True
print("input 41 \t=",full_prima(41))  # False
print("input 43 \t=",full_prima(43))  # False
print("input 53 \t=",full_prima(53))  # True
