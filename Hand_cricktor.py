import random as p

ran = [1,2]
ran2 = ["bat","ball"]

x = p.choice(ran)
n = p.choice(ran2)

how = int(input("how many matchs do you want to play : "))

win = str(input("odd or even: "))

inpt2 = int(input("enter an number : "))

print("the output of the computer is : ",x)

a = 0
a = a + (x+inpt2)

if win == "odd":
    if a%2 == 0:
        print("the sum of the number is even ")
        print("you lose the computer choice to ",n)
    else :
        print("the sum of the number is odd")
        you = str(input("you win do you choice to bat or ball : "))

elif win == "even":
    if a%2 == 0:
        print("the sum of the number is even ")
        you = str(input("you win do you choice to bat or ball : "))
    else :
        print("the sum of the number is odd")
        print("you lose the computer choice to ",n)
    
inpt = int(input("shall we start(1/0) : "))
print("--"*30)

y = 0
z = 0
e = how
for i in range(how):
    f = how-i 
    while f > 0:
        inpt = int(input("enter an number value : "))
        x = p.choice(ran)
        print("the output of the computer is : ", x)
        y = y + (inpt)
        print("the sum of the two scores is : ",y)
        print("--"*30)
        if x == inpt:
            print("you lose")
            print("--"*30)
            shall = int(input("now my turn shall we start(1/2) : "))
            while f > 0:
                x = p.choice(ran)
                inpt = int(input("enter an number value : "))
                print("the output of the computer is : ", x)
                z = z + (x)
                print("the sum of the two scores is : ",z)
                print("--"*30)
                if x == inpt:
                    print("you lose")
                    print("--"*30)
                    if z > y:
                        print("the computer wins ")
                        print("the first match score is ",y)
                        print("the second match score is ",z)
                    else:
                        print("you win")
                        print("the first match score is ",y)
                        print("the second match score is ",z)
    if f == 0:
        break
 
if x> y:
    print("as you choice to the score of yours is greater than of that of the computer so you win" )
else :
    print("as you choice to the score of yours is lesser than of that of the computer so you loss" )
