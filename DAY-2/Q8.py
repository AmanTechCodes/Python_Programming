# Q8) Check palindrome number.

n = int(input("Enter number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome number")

else:
    print("Not a palindrome number")  
      