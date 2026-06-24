# Q2) Print the multiplication table of a given number.

n=int(input("Enter a number: "))

for i in range(1 , 11):

    result = n * i

    print(n , "X" , i , "=" , result)