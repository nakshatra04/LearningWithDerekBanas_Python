customer = []

option = 'y'

while (option == 'y' or option =='yes'):

    option = raw_input("Do you wnat to enter customer information (Yes/No) : ")

    option = option[0].lower()

    if (option != 'y' and option != 'n'):
        print "Enter valild option"
        continue

    if (option =='n' or option =='no'):
        break
    fname , lname = raw_input("Enter the name of the customer : ").split()
    customer.append({'fname':fname,'lname':lname})
for name in customer:
    print name["fname"], name["lname"]


