
#Problem 1
def bilangan_prima(bilangan):
    # Bilangan kurang dari atau sama dengan 1 bukan bilangan prima
    if bilangan <= 1:
        return False
    if bilangan <= 3:
        return True
    if bilangan % 2 == 0 or bilangan % 3 == 0:
        return False
    i = 5
    while i * i <= bilangan:
        if bilangan % i == 0 or bilangan % (i + 2) == 0:
            return False
        i += 6
    return True


print("=======Problem 1=======", "\n")
print("hasil 10000000070 :",bilangan_prima(1000000007))  # True
print("hasil 1500450271 :",bilangan_prima(1500450271))  # True
print("hasil 1000000000 :",bilangan_prima(1000000000))  # False
print("hasil 10000000019 :",bilangan_prima(10000000019)) # True
print("hasil 10000000033 :",bilangan_prima(10000000033)) # True


#Problem 2
def pow(x, n):
    result = 1
    base = x
    exponent = n
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    
    return result

print("input (2, 3) :",pow(2, 3)) 
print("input (7, 2) :",pow(7, 2))  
print("input (10, 5) :",pow(10, 5)) 
print("input (17, 6) :",pow(17, 6)) 
print("input (5, 3) :",pow(5, 3))  



#Problem 3
def penggabungan_data (A,B):
    c = A+B
    newArray = list(set(c))
    return newArray

print(penggabungan_data(["apel","anggur"],["apel","leci","nanas"]),"\n")

print(penggabungan_data(["samsung","apple"],["apple","sony","xiomi"]),"\n")
   
print(penggabungan_data(["football","basketball"],["basketball","football"]),"\n")


#Problem 4
def nilai_muncul_sekali(string_array):
    munculnya = {}
    for nilai in string_array:
        if nilai in munculnya:
            munculnya[nilai] += 1
        else:
            munculnya[nilai] = 1
    
    return [int(k) for k, v in munculnya.items() if v == 1]

# Contoh penggunaan
print("input 1234123 :", nilai_muncul_sekali("1234123")) 
print("input 76523752 :",nilai_muncul_sekali("76523752")) 
print("input 12345 :",nilai_muncul_sekali("12345")) 
print("input 1122334455 :",nilai_muncul_sekali("1122334455")) 
print("input 0872504 :",nilai_muncul_sekali("0872504"))  

#problem 5

def pair_sum(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

print(pair_sum([1, 2, 3, 4, 6], 6))  # [1, 3]
print(pair_sum([2, 5, 9, 11], 11))  # [0, 2]
print(pair_sum([1, 3, 5, 7], 12))  # [2, 3]
print(pair_sum([1, 4, 6, 8], 10))  # [1, 2]
print(pair_sum([1, 5, 6, 7], 6))  # [0, 1]


#Problem 2
def pow(x, n):
    result = 1
    base = x
    exponent = n
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    
    return result

print("input (2, 3) :",pow(2, 3)) 
print("input (7, 2) :",pow(7, 2))  
print("input (10, 5) :",pow(10, 5)) 
print("input (17, 6) :",pow(17, 6)) 
print("input (5, 3) :",pow(5, 3))  
