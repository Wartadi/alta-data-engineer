# #Problem 1
# def find_min_and_max(array):
#     if not array:
#         return "Array kosong"
    
#     min_value = float('inf')
#     max_value = float('-inf')
#     min_index = -1
#     max_index = -1
    
#     for i, num in enumerate(array):
#         if num < min_value:
#             min_value = num
#             min_index = i
#         if num > max_value:
#             max_value = num
#             max_index = i
            
#     return f"min: {min_value} index: {min_index} max: {max_value} index: {max_index}"

# print(find_min_and_max([5, 7, 4, -2, -1, 8])) 
# print(find_min_and_max([2, -5, -4, 22, 7, 7]))  
# print(find_min_and_max([4, 3, 9, 4, -21, 7]))  
# print(find_min_and_max([-1, 5, 6, 4, 2, 18]))  
# print(find_min_and_max([-2, 5, -7, 4, 7, -20])) 

# #Problem 2
# def maksimum_pembelian_produk(uang, harga_product):
#     harga_product = sorted(set(harga_product))
#     count = 0
    
#     for harga in harga_product:
#         if uang >= harga:
#             uang -= harga
#             count += 1
#         else:
#             break
    
#     return count

# print("where input (50000, [25000, 25000, 10000, 14000]) maka : ",
#       maksimum_pembelian_produk(50000, [25000, 25000, 10000, 14000])) 
# print("where input (30000, [15000, 10000, 12000, 5000, 3000]) maka : ",
#       maksimum_pembelian_produk(30000, [15000, 10000, 12000, 5000, 3000]))  
# print("where input (10000, [2000, 3000, 1000, 2000, 10000]) maka : ",
#       maksimum_pembelian_produk(10000, [2000, 3000, 1000, 2000, 10000]))  
# print("where input  (4000, [7500, 3000, 2500, 2000]) maka : ",
#       maksimum_pembelian_produk(4000, [7500, 3000, 2500, 2000]))  
# print("where input (0, [10000, 30000]) maka : ",
#       maksimum_pembelian_produk(0, [10000, 30000]))  

# #Problem3
# def bermain_domino(kartu2, deck):
#     karu_terbaik = []
#     jumlah_angkaMaks = -1
    
#     for kartu in kartu2:
#         if deck[0] in kartu or deck[1] in kartu:
#             if sum(kartu) > jumlah_angkaMaks:
#                 karu_terbaik = kartu
#                 jumlah_angkaMaks = sum(kartu)
    
#     return karu_terbaik

# # Test cases
# print(f"where input : [6, 5], [3, 4], [2, 1], [3, 3]], [4, 3] maka :","\n",  
#       bermain_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3])) 
# print(f"where input : [6, 5], [3, 3], [3, 4], [2, 1]], [3, 6] maka :",
#       "\n",bermain_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  


#Problem 4
def count_item_and_sort(items):
    from collections import Counter
    counts = Counter(items)
    sorted_items = sorted(counts.items(), key=lambda x: x[1])
    result = " ".join(f"{item}->{count}" for item, count in sorted_items)
    return result


print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))  


print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))  


print(count_item_and_sort(["football", "basketball", "tenis"]))  

