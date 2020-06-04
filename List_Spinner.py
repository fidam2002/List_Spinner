### SOAL 2

# Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka (Putaran 1X counter-clockwise) seperti keterangan di bawah ini .
# List Awal
# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]

# Function
# # Function Initialization
#  def counterClockwise(...):
#      .....
     
# # Use the Function
# print(counterClockwise(List_awal))

# List Output

# [[3, 6, 9],
# [2, 5, 8],
# [1, 4, 7]]

#############################################

def spinkiri(list_awal):
    baris1 = []
    baris2 = []
    baris3 = []
    baris1.append(list_awal [0][2])
    baris1.append(list_awal [1][2])
    baris1.append(list_awal [2][2])
    baris2.append(list_awal [0][1])
    baris2.append(list_awal [1][1])
    baris2.append(list_awal [2][1])
    baris3.append(list_awal [0][0])
    baris3.append(list_awal [1][0])
    baris3.append(list_awal [2][0])
    baris_a = str(baris1)
    baris_b = str(baris2)
    baris_c = str(baris3)
    hasil = (f'[{baris_a} \n{baris_b} \n{baris_c}]')
    return hasil

awal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spinkiri(awal))


#############################################
### Maaf, saya hanya bisa mengerjakan soal ini dengan cara manual berikut ###
#############################################