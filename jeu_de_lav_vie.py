import random, os, time
x = 5
y = 5

tab = [[0] * x for i in range(x)]
tab2 = [[0] * x for i in range(x)]
for i in range(x):
    for j in range(y):
        tab[i][j] = random.randint(0,1)
        tab2[i][j] = tab[i][j]


def printTab(x,y, tab):
    for i in range(x):
        print(tab[i])


def cell(x,y,tab):
    return tab[y][x]

printTab(x,y, tab)
print('\n \n \n')

while True:
    os.system('cls')
    for i in range(1, x-1):
        for j in range(1, y-1):
            cpt = 0
            if tab[i-1][j-1] == 1:
                cpt += 1
            if tab[i][j-1] == 1:
                cpt += 1
            if tab[i+1][j-1] == 1:
                cpt += 1
            if tab[i-1][j] == 1:
                cpt += 1
            if tab[i+1][j] == 1:
                cpt += 1
            if tab[i-1][j+1] == 1:
                cpt += 1
            if tab[i][j+1] == 1:
                cpt += 1
            if tab[i+1][j+1] == 1:
                cpt += 1

            if cpt > 3 or cpt < 2:
                tab2[i][j] = 0
            elif cpt == 3:
                tab2[i][j] = 1
            else:
                tab2[i][j] = tab[i][j]

    tab = [row[:] for row in tab2]
    printTab(x,y, tab)
    print('\n')
    time.sleep(0.5)



