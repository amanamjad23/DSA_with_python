def palindromeCheck(num):
    temp = num
    rev = 0
    while (num != 0):
        r = num % 10
        rev = rev * 10 + r
        num = num // 10
    if (rev == temp):
        print(temp, "is a palindrome number")
    else:
        print(temp, "is not a palindrome number")

palindromeCheck(1221)