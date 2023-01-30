import random
x = 5
y = 5

def init_tab(x,y):
    tab = [[0] * x for i in range(x)]
    for i in range(x):
        for j in range(y):
            tab[i][j] = str(random.randint(0,1))

    #print(tab)
    return tab

def print_tab(x,y):
    tab = init_tab(x,y)
    for i in range(x):
        print(tab[i])


print_tab(x,y)
#init_tab(5)




