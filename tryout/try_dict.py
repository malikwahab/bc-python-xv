my_dict = {
    "hello":['Hee', 'Eee', 'Lee', 'Oee'],
    "how":['Hee', 'Oee', 'Wee'],
    "Are": ['Aee', 'Ree', 'Eee', 'kkt', 'ggw', 'yye'],
    "You":['Yee', 'Oee', 'Uee']
    }
    
def largest_list(my_dict):
    count = 0
    value_key = 0
    for key in my_dict:
        list_count = len(my_dict[key])
        if list_count > count:
            count = list_count
            value_key = key
    return value_key
    
def count_dict(my_dict):
    total_count = 0
    for key in my_dict:
        total_count += len(my_dict[key])
    return total_count

print(largest_list(my_dict))
print(count_dict(my_dict))
