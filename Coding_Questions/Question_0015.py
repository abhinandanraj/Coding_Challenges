def palindrome(s):
    #Remove Spaces String
    s = s.replace(' ','')
    return s == s[::-1]

word = input()
print(palindrome(word))
