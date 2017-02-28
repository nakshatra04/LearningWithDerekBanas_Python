import os
import io

average = 0.0
charcount = 0.0
with io.open("test.txt", mode='w',encoding ="utf-8") as myFile:
    myFile.write(u"Hello \nI think it should\nBe able to track the \nNew Lines")

with io.open("test.txt", encoding="utf-8") as myFile:
    linenum = 1

    while True:

        line = myFile.readline()
        print line
        line = line.split()

        for word in line:
            for char in word:
                charcount += 1

        average = average + len(line)

        if not line :
            break



        linenum += 1
    print "Total no of lines in the file " + str(linenum -1)
    print "Total words in the file " + str(average)
    print "Total character in the file " + str(charcount)

    charcount = charcount/(linenum-1)
    average = average/(linenum-1)


    print "Average Words per lines are " + str(average)
    print "Average character's per line " + str(charcount)





