def Calculator(num1 , num2):
    print('Your num1 value is :-',num1)
    print('Your num2 value is :-',num2)
    
    return num1+num2 , num1 - num2 , num1 * num2 , num1 / num2

num1 = int(input('Enter a num 1st value :-'))
num2 = int(input('Enter a num 2nd value :-'))

a,b,c,d =Calculator(num1,num2)

print("Your Sum Ans is :-",a)
print("Your Sub Ans is :-",b)
print("Your Mull     Ans is :-",c)
print("Your Div Ans is :-",d)

