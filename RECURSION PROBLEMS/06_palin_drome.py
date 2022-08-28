num = input('Enter a no to check palindrome :-')
reverse = num[::-1]

if num == reverse:
    print(num,'Your Number Is Palindrome')
else:
    print(num,'Your Number is Not Palindrome')