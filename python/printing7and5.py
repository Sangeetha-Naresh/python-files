# Function to convert binary number using recursion
def toBinary(n):
    # checks if n is greater than 1, teminates r
    if n > 1:
        toBinary(n//2)
    print(n % 2,end = '')
    
for num in range(5, 105+1):
      
    # checking condition for multiple of 5 and converting it to binary
    if num % 5 == 0:
        print(num, end=" ")
        toBinary(num)
        print()

    # checking condition for multiple of 7 and displaying  it
    if num % 7 == 0:
        print(num, end=" ")
        print()
        


