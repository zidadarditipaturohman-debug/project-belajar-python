numbers_data= [68,54,34,54,75,6786,756,435,4234,34]
current_max = 0
for number in numbers_data:
    if number > current_max:
        current_max = number
print(current_max)
