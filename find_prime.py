num = input("Enter the number = ")
def find_prime(num):
    bool = True
    if num==2:
        return bool
    else:
        for i in range(2,num):
            if num % i == 0:
                bool = False
    return bool

for i in range(2,num):
    if (find_prime(i)):
        print i
