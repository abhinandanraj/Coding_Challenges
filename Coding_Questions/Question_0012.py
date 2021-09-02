#Method 1 

def uc_lc(s):
    lowercase = 0
    uppercase = 0

    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f"String: {s}")
    print(f'No. of Upper Case Characters: {uppercase}')
    print(f'No. of Lower Case Characters: {lowercase}')

s = str(input())
uc_lc(s)
print()

#Method 2 : Using Dictionary

def uc_lc(s):
    dic = {'upper':0, 'lower':0}

    for char in s:
        if char.isupper():
            dic['upper'] += 1
        elif char.islower():
            dic['lower'] += 1
        else:
            pass
    print(f"String: {s}")
    print(f'No. of Upper Case Characters: {dic["upper"]}')
    print(f'No. of Lower Case Characters: {dic["lower"]}')

s = str(input())
uc_lc(s)
print()
