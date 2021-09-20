def multi(x):
    total = 1
    for num in x:
        total = total * num
    return total

user_list = [1,2,3,-4]
print(multi(user_list))
