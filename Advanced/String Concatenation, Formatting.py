import os

names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    print('Hello there, ' + name)
    print(' '.join(['Hello there,', name]))

print(', '.join(names))


location_of_files = 'C:\\Users\\Me\\Desktop\\Python'
file_name = 'example.txt'
print(location_of_files + "\\" + file_name)
print(os.path.join(location_of_files, file_name))


who = 'Gary'
how_many = 12

print(who, 'bought', how_many, 'apples today!')
print('{} bought {} apples today!'.format(who, how_many))
