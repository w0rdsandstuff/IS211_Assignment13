#Fibonnaci Sequence
def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + (n-2)

#GCD
def gcd(x,y):
    if x == 0:
        return y
    else:
        z = y % x
    return z

#Comparision
def compareTo(s1, s2):
    if s1 < s2:
        val = -1
        return val
    if s1 == s2:
        return 0
    if s1 > s2:
        val2 = 1
        return val2
    return

    


