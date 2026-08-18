numbers = [12,45,2,99,23,54,12,8 ]
max_num = numbers[0]
min_num = numbers[0]
T_sum =0
for i in numbers:
    T_sum +=i

    if i>max_num:
        max_num = i
    if i<min_num:
        min_mun = i

print("Maximum = ",max_num)
print("Minimum = ",min_num)

average = T_sum/len(numbers)
print("Average is : ",average)