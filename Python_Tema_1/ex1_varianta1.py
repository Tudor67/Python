def calcul():
    f = 1
    n = 2
    cauta = True

    while cauta :
        
        x = n #Descompun numarul si adaug la solutie cate cifre de 1 are acesta 
        while x > 0:
            if x % 10 == 1:
                f += 1
            x /= 10
        
        if n == f:
            cauta = False #Daca am f(n) == n atunci opresc cautarea
        else:
            n += 1 #Altfel trec la n+1
    
    print n

calcul() #Obtin raspunsul 199981
