
green_eggs = open('green_eggs_text', 'r+')

errors = []
list_num = []
counter = 0
for i in green_eggs:


    new_text = i.replace('-i-', '-I-')
    new_text2 = new_text.replace('i ', 'I ')
    stripping = new_text2.strip('\n')
    print(stripping, stripping.count('I'))
    errors.append(stripping.count('I'))
    with open("green_eggs_edit", 'a') as new_file:
        new_file.write(stripping + '\n')
for num in errors:
    if num != 0:
        list_num.append(num)
print(list_num)

for counting in list_num:
    counter += counting

print('There are:', counter, 'errors')


