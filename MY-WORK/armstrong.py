num=int(input("Enter a three number :- "))
temp = num
sum = 0
                        #   ARMSTRONG
while num > 0:
    digit = temp % 10
    sum +=digit ** 3
    temp //= 10

if num == sum:
    print(num,"Is Armstrong Number")
else:
    print(num,"Is Not Armstrong Number")
