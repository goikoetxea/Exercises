def find (ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    else:
        return False


a=[2,4,6,8]

print(find(a, 9))