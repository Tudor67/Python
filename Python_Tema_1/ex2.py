import random
def ghiceste():
    nr = random.randint(1,20)
    incercare = 1
    cauta = True
    
    print "Ma gandesc la un numar intre 1 si 20 ..."
    print "Reusesti sa il ghicesti din 5 incercari?" 
    
    while cauta:
        print "Incercarea",incercare,":"
        x = int(raw_input())
        
        if x == nr:
            cauta = False
            print "Bravo, ai ghicit numarul din",incercare,"incercari!"
        elif nr > x:
            print "Numarul la care m-am gandit este mai mare"
        else:
            print "Numarul la care m-am gandit este mai mic"
        
        if incercare == 5 and cauta == True:
            cauta = False
            print "Game over! :("
 
        incercare += 1   
        
ghiceste()
