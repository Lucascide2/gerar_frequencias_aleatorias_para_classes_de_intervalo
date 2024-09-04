import random

def get_frequencies(arr):
    arr_sort = sorted(arr)
    freq_arr = []
    covered_idx = []
    
    for i in range(len(arr_sort)):
        if i in covered_idx:
            continue
        else:
            freq = 1
            covered_idx.append(i)
            for j in range(i+1, len(arr_sort)):
                if arr_sort[i] == arr_sort[j]:
                    freq += 1
                    covered_idx.append(j)
                    
            freq_arr.append(freq)
                    
    return freq_arr

def get_freq_ac(arr):
    freq_arr = get_frequencies(arr)
    return sum(freq_arr)

def get_new_xi_arr(arr, quantity):
    new_arr = []
    
    for i in range(quantity):
        new_arr.append(arr[random.randint(0, get_freq_ac(arr) -1)])
    
    return new_arr

def get_new_frequencies(arr, quantity):
    new_arr = get_new_xi_arr
    return get_frequencies(new_arr)
                  
rede_A = [2.5]*29 + [7.5] * 13 + [12.5] * 8 + [17.5] * 18 + [22.5] * 4 + [27.5] * 5 + [32.5] * 21
new_rede_A = get_new_xi_arr(rede_A, 100)
freq_new_rede_A = get_frequencies(new_rede_A)

rede_B = [2.5]*40 + [7.5] * 12 + [12.5] * 35 + [17.5] * 12 + [22.5] * 52 + [27.5] * 29 + [32.5] * 28
new_rede_B = get_new_xi_arr(rede_B, 100)
freq_new_rede_B = get_frequencies(new_rede_B)


print("freq_new_rede_A = " + str(freq_new_rede_A))
print("freq_new_rede_B = " + str(freq_new_rede_B))