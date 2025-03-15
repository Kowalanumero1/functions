def add(P, Q):
    return P+Q

def substract(P, Q):
    return P+Q

def multiply(P, Q):
    return P+Q

def divide(P, Q):
    return P+Q

#now we will take input from user
print("please select operation.")
print("a. add")
print("b. substract")
print("c.multiply")
print("d.devide")

choice = input("please enter your choice(a/b/c/d):")

num_1 = int(input("enter the first number: ")) 
num_2 = int(input("enter the second number: ")) 

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", substract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("ths is an invalid input")