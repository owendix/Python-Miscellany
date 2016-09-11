# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def num2word(num,spaces=True):
    #Converts a number and returns the string word equivalent, all lower
    #option allows for no spaces
    
    ones = ('one','two','three','four','five','six','seven',\
            'eight','nine')
    teen = ('ten','eleven','twelve','thirteen','fourteen','fifteen',\
            'sixteen','seventeen','eighteen','nineteen')
    tens = ('twenty','thirty','forty','fifty','sixty','seventy',\
            'eighty','ninety')
    tripleSfx = ('thousand','million','billion','trillion', \
                 'quadrillion', 'quintillion', 'sextillion', \
                 'septillion', 'octillion', 'nonillion', 'decillion',\
                 'undecillion','duodecillion','tredecillion',\
                 'quattuordecillion','quindecillion','sexdecillion',\
                 'septendecillion','octodecillion','novemdecillion',\
                 'vigintillion')
    
    if spaces:
        wordSep = ' '
    else:
        wordSep = ''

    w = []
    revNumList = list(str(num))
    revNumList.reverse()    #mutates the list to reverse order
    if len(revNumList) == 1:
        if revNumList[0] == '0':
            w.append('zero')
        else:
            w.append(ones[int(revNumList[0])-1])
    elif len(revNumList) > 1:
        
        #w will be reversed back at end
        for i in range(len(revNumList)):  #skip i == 0, dep on tens place
            if i % 3 == 0:  #ones thousands millions billions etc
                if i != 0 and revNumList[i:i+3] != ['0','0','0']:
                    w.append(tripleSfx[i//3 -1])
                if revNumList[i] != '0':
                    w.append(ones[int(revNumList[i]) - 1])
            elif i % 3 == 1 and revNumList[i] == '1':   #tens if a teen
                if revNumList[i-1] != '0':
                    w.pop()     #remove previous from word list
                w.append(teen[int(revNumList[i - 1])])
            elif i % 3 == 1:    #tens if not a teen
                if revNumList[i] != '0':
                    w.append(tens[int(revNumList[i]) - 2])
            elif i % 3 == 2 and revNumList[i] != '0':    #hundreds
                w.append('hundred')
                w.append( ones[int(revNumList[i]) - 1] )

    w.reverse() #mutates the list to reverse order
    
    return wordSep.join(w)

#import string
#import matplotlib.pyplot as plt

#Count the number of letters in a number
try:
    num = int(input("Type a number, using only 0-9 (no commas): "))
except:
    print("Input must be a digit 0-9.")
else:
    if len(str(num)) > 66 or num < 0:
        print("\nPositive integers less than or equal to 999.999...",\
            "vigintillion, please.\n")
        raise SystemExit
    else:
        print("\nMapping from","{:,}".format(num),\
            "to its letter count, then repeat.\n")
    
#myDict = {} #dictionary {1st num:Its ltr Count} 
#for startNum in range(0,21,1):
    #num = startNum
    
    '''
    Eventually add number, letter-count pairs to a dict, if 
    it doesn't exist, then I can plot it {x:y}
    Once I know how to plot
    '''

done = False
while not done:
    numAsWord = num2word(num)
    print('-->', "{:,}".format(num), '-->', numAsWord)
    
    numWordNoSpace = numAsWord.replace(' ','')
    countNumLtrs = len(numWordNoSpace)        
    
    #myDict[num]=countNumLtrs
    
    if countNumLtrs == num:
        done = True
    
    num = countNumLtrs
print("Stable.\n")
'''q=[i for i in range(20)]
plt.plot(q,q)
plt.scatter(myDict.keys(),myDict.values())
plt.show()'''