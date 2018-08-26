# xyz = [i for i in range(5000)]
# print(xyz)
# xy = (i for i in range(5000))
# print(xy)

input_list = {5, 6, 12, 25, 15, 20, 2, 3, 8, 13}


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))
[print(i) for i in xyz]

xyz = [i for i in input_list if div_by_five(i)]
print(xyz)
