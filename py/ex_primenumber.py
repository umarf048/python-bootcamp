limit = int(input("Enter the limit for listing prime number : "))

for num in range(2, limit + 1):

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if is_prime == True:
       print(num)
        
