#Problem 1
from collections import Counter

def intersection_impl(input1, input2):
    # Hitung frekuensi kemunculan karakter di masing-masing string
    menghitung1 = Counter(input1)
    menghitung2 = Counter(input2)
    
    # Ambil irisan dengan menggunakan minimum dari kedua Counter
    intersection = {char: min(menghitung1[char], menghitung2[char]) 
                    for char in menghitung1 if char in menghitung2}
    
    # Buat hasilnya berdasarkan urutan karakter pertama kali muncul di input1
    result = []
    for char in input1:
        if char in intersection and intersection[char] > 0:
            result.append(char)
            intersection[char] -= 1
    
    return ''.join(result)

print(intersection_impl("AKA", "AKASHI")) 
print(intersection_impl("KANGOORO", "KANG"))  
print(intersection_impl("KI", "KIJANG"))  
print(intersection_impl("KUPU-KUPU", "KUPU"))  
print(intersection_impl("ILALANG", "ILA"))  


# #Problem 2
def caesar_cipher(offset, string):
    result = []
    for char in string:
        if char.isalpha():
            shifted = ord(char) + offset
            if shifted > ord('z'):
                shifted -= 26
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

print(" Input abc xyz :",caesar_cipher(3, "abc xyz")) 
print(" Input hello world :",caesar_cipher(2, "hello world"))
print(" Input kupu-kupu :",caesar_cipher(1, "kupu-kupu")) 
print(" Input ilalang :",caesar_cipher(4, "ilalang"))  
print(" Input caesar :",caesar_cipher(5, "caesar")) 

#probelm 3
def problem3_unique(list1, list2):
    set1 = set(list2)
    result = []
    for angka in list1:
        if angka not in set1:
            result.append(angka)
    return result


print("input [1,2,3,4], [1,3,5,10,16]:", problem3_unique([1,2,3,4], [1,3,5,10,16]) ) 
print("input [10,20,30,40], [5,10,15,59]:",problem3_unique([10,20,30,40], [5,10,15,59]) ) 
print("input [[1,3,7], [1,3,5]:",problem3_unique([1,3,7], [1,3,5]) ) 
print("input [[3,8], [2,8]) :",problem3_unique([3,8], [2,8]) ) 
print("input [1,2,3 ],[3,2,1] :",problem3_unique([1,2,3 ],[3,2,1]) ) 

# #Problem 4
def max_sum_subarray_of_size_k(arr, k):
    n = len(arr)
    if n < k:
        return -1  
    
    # Hitung jumlah pertama
    max_sum = sum(arr[:k])
    current_sum = max_sum
    
    # Geser jendela array
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum


print("input[2, 1, 5, 1, 3, 2], 3) :", max_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3))
print("input[2, 3, 4, 1, 5], 2) :",max_sum_subarray_of_size_k([2, 3, 4, 1, 5], 2))     
print("input[2, 1, 4, 1, 1],2) :",max_sum_subarray_of_size_k([2, 1, 4, 1, 1],2))
print("input[2, 1, 4, 1, 1],3) :",max_sum_subarray_of_size_k([2, 1, 4, 1, 1],3))
print("input[2, 1, 4, 1, 1],4) :",max_sum_subarray_of_size_k([2, 1, 4, 1, 1],4))

#Problem 5
def hapus_duplikat(angka):
    if not angka:
        return 0
    
    # Menggunakan dua pointer untuk memindahkan elemen unik ke bagian depan array
    # Jumlah unik awalnya adalah 1 karena elemen pertama pasti unik
    unique_count = 1
    
    # Membandingkan elemen saat ini dengan elemen sebelumnya
    for i in range(1, len(angka)):
        if angka[i] != angka[i - 1]:
            angka[unique_count] = angka[i]
            unique_count += 1
    
    return unique_count

print(hapus_duplikat([2, 3, 3, 3, 6, 9, 9])) 
print(hapus_duplikat([2, 3, 4, 5, 6, 9, 9]))
print(hapus_duplikat([2, 2, 2, 11]))    
print(hapus_duplikat([1, 2, 3, 11, 11]))            
