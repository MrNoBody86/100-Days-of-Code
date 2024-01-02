# You need to write a function that checks whether if the number passed into it is a prime number or not.

def prime_checker(number):
    is_prime = True
    for num in range(2,number):
        if number % num == 0 :
            is_prime = False
            break
    
    if  is_prime & number == 1 | 0 :
        print("It's a prime number.")
    else :
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)