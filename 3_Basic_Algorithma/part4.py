######### Advance Looping & List #######

# ## Problem 1 - play with asterisk

# def play_with_asterisk(n):
#     for i in range(1, n + 1):
#         print(' ' * (n - i) + '* ' * i)

# play_with_asterisk(5)
# print()
# play_with_asterisk(8)




# # # Problem 2 - draw XYZ

# def draw_xyz(N):
#     result = []
#     for i in range(N):
#         row = []
#         for j in range(N):
#             position = i * N + j + 1
#             if position % 3 == 0:
#                 row.append('X')
#             elif position % 2 == 0:
#                 row.append('Z')
#             else:
#                 row.append('Y')
#         result.append(' '.join(row))
#     return '\n'.join(result)

# # Contoh penggunaan
# print("where input = 3")
# print(draw_xyz(3))
# print("where input = 5")
# print(draw_xyz(5))


# Proble 3 - Cetak Tabel Perkalian

# def cetak_table_perkalian(number):
#     for i in range(1, number + 1):
#         row = []
#         for j in range(1, number + 1):
#             row.append(str(i * j).rjust(4))
#         print(' '.join(row))

# print("where input = 9")
# cetak_table_perkalian(9)


# # Problem 4 - Ubah Huruf
# def ubah_huruf(sentence):
#     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     shifted_alphabet = 'KLMNOPQRSTUVWXYZABCDEFGHIJ'
#     translation_table = str.maketrans(alphabet, shifted_alphabet)
#     return sentence.translate(translation_table)

# # Contoh penggunaan
# print(("SEPULSA OKE \t="),ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
# print(("ALTERRA ACADEMY ="),ubah_huruf("ALTERRA ACADEMY"))  # KVDOBBK KMKNOWI
# print(("INDONESIA \t="),ubah_huruf("INDONESIA"))  # SXNYXOCSK
# print(("GOLANG \t\t="),ubah_huruf("GOLANG"))  # QYVKXQ
# print(("PROGRAMMER\t="),ubah_huruf("PROGRAMMER"))  # ZBYQBKWWOB


## Problem 5 - Mean & Median
def mean_median(array_input):
    n = len(array_input)
    mean = sum(array_input) / n
    
    if n % 2 == 0:
        median = (array_input[n // 2 - 1] + array_input[n // 2]) / 2
    else:
        median = array_input[n // 2]
    
    return (mean, median)

print("Mean, Median")
print(mean_median([1, 2, 3, 4]))  # (2.5, 2.5)
print(mean_median([1, 2, 3, 4, 5]))  # (3.0, 3)
print(mean_median([7, 8, 9, 13, 15]))  # (10.4, 9)
print(mean_median([10, 20, 30, 40, 50]))  # (30.0, 30)
print(mean_median([15, 20, 30, 60, 120]))  # (49.0, 30)
