def fib(num):
    if num >=0:

        if num == 1:
            return 1
        elif num == 0:
            return 0
        else:
            result = fib(num-1) + fib (num-2)
            return result
    else:
        return "Invalid Number"

print (fib(10))
