v1 = [0] * 22
v1[0] = 84
v1[1] = 101
v1[2] = 97
v1[3] = 109
v1[4] = 84
v1[5] = 53
v1[6] = 123
v1[21] = 125
#=====================
v1[17] = 25
v1[11] = 168
v1[12] = 31
# v1[8] = 
v1[7] = 163
# v1[9] = 
# v1[10] = 
v1[13] = 75
v1[14] = 151
v1[15] = 10
# v1[16] = 
# v1[18] = 
v1[19] = 11
v1[20] = 24
#=====================
# (v1[12] + v1[7]) == 194
# (v1[16] + v1[8]) == 147
# (v1[10] + -56 - v1[9]) == 244
# (v1[11] - v1[13] + 2) == 246
# (v1[19] + v1[12] - v1[20]) == 44
# (v1[5] - v1[14]) == 205
# (3 * v1[0] + 2 * v1[17]) == 200
# (4 * v1[15] - 7 * v1[17]) == 2
# (v1[16] + 2 * v1[17] - 3 * v1[18]) == 152
# (5 * v1[8] + 3 * v1[5] + v1[2]) == 4
# (v1[16] + v1[7] - v1[12] - v1[20]) == 252
# (v1[11] + v1[19]) == 156
# (v1[17] - 2 * v1[13]) == 126
# (6 * v1[9] + 8 * v1[15]) == 226
# (v1[13] - v1[15]) == 65
# (v1[11] - v1[7]) == 5 

print(v1)
for i in range(22):
    v1[i] = chr(v1[i])
print(v1)