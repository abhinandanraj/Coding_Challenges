def unique_list(lst):
    seen_number = []
    for number in lst:
        if number not in seen_number:
            seen_number.append(number)
    return seen_number

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
