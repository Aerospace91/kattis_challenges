num_temps = 3
temp_string = '5 -10 15'
temp_list = list(map(int, temp_string.split(' ')))
print(sum(i < 0 for i in temp_list))