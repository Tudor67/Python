def calcul():
    fn = 1
    n = 2
    
    while n != fn:
        n += 1
        fn += str(n).count('1')

    print n

calcul()
