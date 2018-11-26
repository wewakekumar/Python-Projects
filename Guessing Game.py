import random
a=""
print(" {0:^60}NUMBER GUESSING CHALLENGE".format(a))
print("Rules and Hints:")
print("1. For Easy level you will have to guess a number between 1 and 100 and You will get 100 points at first and 10 points will deducted on every wrong guess")
print("2. For Easy level you will have to guess a number between 1 and 1000 and You will get 100 points at first and 5 points will deducted on every wrong guess")
print("3. For Easy level you will have to guess a number between -100 and 1000 and You will get 100 points at first and 3 points will deducted on every wrong guess")
print("4. For Easy level you will have to guess a number between -1000 and 1000 and You will get 100 points at first and 1 points will deducted on every wrong guess")
print("5. If your guess is less than 1 or greater than 100 you will get OUT OF BOUNDS as remark")
print("6. On your first turn if your guess number's difference with real number is less than 10 then you will get WARM as remarks else you will get COLD as remark")
print("7. On your further turn if your guess number's difference with real number is less than the first one then you will get WARMER as remarks else you will get COLDER as remarks")
print("8. You will get CONGRATS as remarks if you have guessed the number correctly")

print("Choose Dificulty Level:")
print("1.Easy\n2.Medium\n3.Hard\n4.Advanced")

while True:
    try:
        i = int(input("Please Enter Level No."))
    except:
        print("Looks like you have inserted a non-integer value\nPlease Enter it again")
        continue
    else:
        p=1
        q=100
        if(i==1):
            p=1
            q=100
        if(i==2):
            p=1
            q=1000
        if(i==3):
            p=-100
            q=1000
        if (i == 4):
             p =-1000
             q =1000
        x=random.randint(p,q)
        l=[]
        r=0
        while True:
            y=int(input("PLEASE ENTER THE NUMBER"))
            l.append(y)
            if i==1:
                if y>100 or y<1:
                print("Out of bound")
                r=r+1
                continue;
            if i==2:
                if y > 1000 or y < 1:
                    print("Out of bound")
                    r = r + 1
                    continue;
            if i==3:
                if y > 1000 or y < -100:
                    print("Out of bound")
                    r = r + 1
                    continue;
            if i==4:
                if y > 1000 or y < -1000:
                    print("Out of bound")
                    r = r + 1
                    continue;
            if (x-y)==0:
                    print("CONGRATS")
                    break;
            if len(l)>1:
              if abs(l[-2]-x)<abs(x-y):
                    print("COLDER")
                    r=r+1
                    continue;
              if abs(l[-2]-x)>=abs(x-y):
                    print("WARMER")
                    r = r + 1
                    continue;
            elif abs(x-y) <= 10:
                    print("WARM")
                    r = r + 1
                    continue;
            elif abs(x-y) > 10:
                    print("COLD")
                    r = r + 1
                    continue;
        if i==1:
         p=100-(10*r)
        if i==2:
            p=100-(5*r)
        if(i==3):
            p=100-(3*r)
        if(i==4):
            p=100-r
        print("You have scored {} points".format(p))
        break
