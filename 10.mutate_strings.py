first_string = input()
second_string = input()

last_printed_string = first_string

for char_index in range(len(first_string)):
    left_part = second_string[:char_index + 1]
    right_part = first_string[char_index + 1:]
    new_string = left_part + right_part

    if first_string[char_index] != second_string[char_index]:
        print(new_string)




# my_string = "alabalaportokala"
# print(my_string[:3])
# print(my_string[3:7])
# print(my_string[7:16])