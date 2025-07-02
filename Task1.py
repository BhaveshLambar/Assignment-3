def factorial(num):
    if num == 0:
        return 1 
    else:
        return num * factorial(num-1)
    
num_v = int(input("Enter a number : "))
print("Factorial of",num_v,"is :",factorial(num_v))