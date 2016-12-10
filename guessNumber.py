#encoding:utf-8
import random
import os
history=[]
def getNumbers(n=4):
    r=[]
    while len(r)<n:
        t=random.randint(0,9)
        if not t in r:r.append(t)
    return r
getWebInput=None
def getInput():
    if getWebInput!=None:
        return getWebInput()
    return str(raw_input("Please input 4 numbers"))
def sPrint(s):
    global history
    history.insert(0,s)
    if len(history)>20:
        history.pop()
    if getWebInput==None:
        print s
def inputNumbers():
    r=[]
    s=getInput()
    t=list(s)
    if len(t)!=4:return
    for i in t:
       if (not i in r) and i.isdigit():
            r.append(i)
    if len(r)!=4:return
    # sPrint(str(','.join(r)))
    return map(int,r)
def guessResult(guessNumbers,trueNumbers):
    a,b=0,0 
    for i in range(len(trueNumbers)):
        if guessNumbers[i]==trueNumbers[i]:
            a+=1
        elif (guessNumbers[i] in trueNumbers):
            b+=1
    return a,b

n=getNumbers()
a=0
t=0
def newGame():
    global a,t,n,history
    a=0
    t=0
    history=[]
    n=getNumbers()
    # sPrint(str(n))
def gameOver():
    return a==4 or t==7
def oneGuess(guessTimes=7):
    global a,t,n
    inputs=inputNumbers()
    if inputs:
        a,b=guessResult(inputs,n)
        t+=1
    else:
        sPrint("Please type 4 different number:")
        return
    # print n
    sPrint("The %sth time input %s the result is:%s A ,%s B"%(t,','.join(map(str,inputs)),a,b))
    if  gameOver():
        sPrint("You win!" if a==4 else "Times up!You lose!answer is :%s"%n)
        sPrint("A new game begin.")
    return def main():
    while True:
        while not gameOver():
            oneGuess()
        newGame()
if __name__=="__main__":
    main()