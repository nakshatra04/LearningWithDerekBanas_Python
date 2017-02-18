def solve_eq(equation):
    var1 , operator, var2, equal, var3 = equation.split()
    if var1 == 'x' or var1 == 'X' or var1 == 'y' or var1 == 'Y':
        if operator == '-':
            return (int(var3)+int(var2))
        elif operator == '+':
            return (int(var3)-int(var2))
        elif operator == '*':
            return (int(var3)/int(var2))
        elif operator == '/':
            return (int(var3)*int(var2))
    elif var2 == 'x' or var2 =='X' or var2 == 'y' or var2 =='Y':
        if operator == '-':
            return (-(int(var3))+int(var1))
        elif operator == '+':
            return (int(var3)-int(var1))
        elif operator == '*':
            return (int(var1)/int(var3))
        elif operator == '/':
            return (int(var3)*int(var1))


equation = raw_input("Enter the simple equation : ")

print solve_eq(equation)
