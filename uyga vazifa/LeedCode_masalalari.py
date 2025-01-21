def sonlar(x):

    tekshirish=str(x)
    natija_x=tekshirish[::-1]
    return tekshirish==natija_x

x=int(input('Son kiriting='))
a=sonlar(x)
print(a)

