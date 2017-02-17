import random

mynum = random.randint(1,10)

while True:
    try :

        guessnum = int(input("Guess a number"))
        if guessnum == mynum:
            print ("You guessed the {} number").format(mynum)
            break
        else:
            continue
    except ValueError:
        print "Please Enter a number only"
    except:
        print "Please Enter valid input only"


