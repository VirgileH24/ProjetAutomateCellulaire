
import random
import tkinter


def listes(taille):
    l = list(range(taille))
    for i in l:
        l[i] = list(range(taille))
        for j in range(taille):
            l[i][j] = 0
    return l


def CellActivation(i, j):
    etat[i][j] = 1
    grid[i][j] = can1.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill='white', outline='black')
    grid[i][j] = can1.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill='black')


def CellDesactivation(i, j):
    etat[i][j] = 0
    grid[i][j] = can1.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill='white', outline='black')
    grid[i][j] = can1.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill='black', outline='black')


def Random():
    nbr_cellules = random.randint(1, 200)
    for i in range(0, nbr_cellules):
        x = random.randint(0, cote - 1)
        y = random.randint(0, cote - 1)
        CellActivation(x, y)


########## Choix aléatoire d'un couple #########

def coin_HautGauche(x, y):
    p = random.randint(0, 1)
    if p == 0:
        return x, y + 1
    else:
        return x + 1, y


def coin_HautDroit(x, y):
    p = random.randint(0, 1)
    if p == 0:
        return x, y + 1
    else:
        return x - 1, y


def coin_BasGauche(x, y):
    p = random.randint(0, 1)
    if p == 0:
        return x + 1, y
    else:
        return x, y - 1


def coin_BasDroite(x, y):
    p = random.randint(0, 1)
    if p == 0:
        return x - 1, y
    else:
        return x, y - 1


def PremiereColonne(x, y):
    p = random.randint(0, 2)
    if p == 0:
        return x + 1, y
    if p == 1:
        return x, y + 1
    if p == 2:
        return x, y - 1


def DerniereColonne(x, y):
    p = random.randint(0, 2)
    if p == 0:
        return x - 1, y
    if p == 1:
        return x, y + 1
    if p == 2:
        return x, y - 1


def PremiereLigne(x, y):
    p = random.randint(0, 2)
    if p == 0:
        return x + 1, y
    if p == 1:
        return x, y + 1
    if p == 2:
        return x - 1, y


def DerniereLigne(x, y):
    p = random.randint(0, 2)
    if p == 0:
        return x + 1, y
    if p == 1:
        return x - 1, y
    if p == 2:
        return x, y - 1


def Interieur(x, y):
    p = random.randint(0, 3)
    if p == 0:
        return x, y + 1
    if p == 1:
        return x, y - 1
    if p == 2:
        return x + 1, y
    if p == 3:
        return x - 1, y


def random_couple_cell():
    x = random.randint(0, cote - 1)
    y = random.randint(0, cote - 1)
    z = x
    w = y

    # L'intérieur
    if (x > 0) and (x < cote - 1) and (y > 0) and (y < cote - 1):
        z, w = Interieur(x, y)

    # les Coins
    if (x == 0) and (y == 0):
        z, w = coin_HautGauche(x, y)
    if (x == 0) and (y == cote - 1):
        z, w = coin_BasGauche(x, y)
    if (x == cote - 1) and (y == 0):
        z, w = coin_HautDroit(x, y)
    if (x == cote - 1) and (y == cote - 1):
        z, w = coin_BasDroite(x, y)

    # les contours
    if (x == 0) and (y > 0) and (y < cote - 1):
        z, w = PremiereColonne(x, y)
    if (x == cote - 1) and (y > 0) and (y < cote - 1):
        z, w = DerniereColonne(x, y)
    if (y == 0) and (x > 0) and (x < cote - 1):
        z, w = PremiereLigne(x, y)
    if (y == cote - 1) and (x > 0) and (x < cote - 1):
        z, w = DerniereLigne(x, y)

    return x, y, z, w


def transition(x, y, z, w):
    if etat[x][y] == 1 and etat[z][w] == 0:
        transition = random.choices(tirage, weights=proba["NB"])
        t = transition[0]
        if t == 1:
            CellActivation(z, w)
            return
        if t == 2:
            CellDesactivation(x, y)
            CellActivation(z, w)
            return
        if t == 3:
            CellDesactivation(x, y)
            return

    if etat[x][y] == 1 and etat[z][w] == 1:

        transition = random.choices(tirage, weights=proba['NN'])
        t = transition[0]
        if t == 1:
            CellDesactivation(z, w)
            return
        if t == 2:
            CellDesactivation(x, y)
            CellDesactivation(z, w)
            return
        if t == 3:
            CellDesactivation(x, y)
            return

    if etat[x][y] == 0 and etat[z][w] == 1:
        transition = random.choices(tirage, weights=proba['BN'])
        t = transition[0]
        if t == 1:
            CellDesactivation(z, w)
            return
        if t == 2:
            CellActivation(x, y)
            CellDesactivation(z, w)
            return
        if t == 3:
            CellActivation(x, y)
            return

    if etat[x][y] == 0 and etat[z][w] == 0:
        transition = random.choices(tirage, weights=proba['BB'])
        t = transition[0]
        if t == 1:
            CellActivation(z, w)
            return
        if t == 2:
            CellActivation(x, y)
            CellActivation(z, w)
            return
        if t == 3:
            CellActivation(x, y)
            return


### partie Animation ####


def simulation():
    global stop
    if stop == 0:
        coordonnées = random_couple_cell()
        x = coordonnées[0]
        y = coordonnées[1]
        z = coordonnées[2]
        w = coordonnées[3]

        transition(x, y, z, w)

        top.after(100, simulation)


def stop1():
    global stop
    stop = 1


def continuer():
    global stop
    stop = 0
    simulation()


def colorier(event):
    can1.focus_set()
    x = event.x
    y = event.y

    CellActivation(x // 10, y // 10)


# demande a l'utilisatueur

def AskProbaUser(Nom):
    list = []
    print("Entrer les quatres probabilités de transition du couple:\n", Nom)
    for i in range(0, 4):
        print("Enter la probabilité Numero {}: ".format(i + 1))
        elm = float(input())
        list.append(elm)  # adding the element
    print("La liste est: \n", list)
    return list


#### main program  ####

Taille_grid = int(input("rentrer la taille de la grille:"))

proba_NB = AskProbaUser("Noir/Blanc")
proba_NN = AskProbaUser("Noir/Noir")
proba_BN = AskProbaUser("Blanc/Noir")
proba_BB = AskProbaUser("Blanc/Blanc")
proba = {"NB": proba_NB, "NN": proba_NN, "BN": proba_BN, "BB": proba_BB}

cote = Taille_grid // 10

etat = listes(Taille_grid)

tirage = [0, 1, 2, 3]

top = tkinter.Tk()

stop = 0

can1 = tkinter.Canvas(top, width=Taille_grid, height=Taille_grid, bg='white')

grid = [[can1.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill='white')
         for i in range(cote)] for j in range(cote)]

can1.pack()

button1 = tkinter.Button(top, text='Generation aléatoire', command=Random)
button1.pack()

can1.bind("<Button-1>", colorier)

button2 = tkinter.Button(top, text='Reprendre', command=continuer)
button2.pack()

button3 = tkinter.Button(top, text='Stop', command=stop1)
button3.pack()

button4 = tkinter.Button(top, text='Simulation', command=simulation)
button4.pack()

top.title("grid")
top.mainloop()
