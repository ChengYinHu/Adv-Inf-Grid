import cv2
import random
import numpy as np
import os

def initiation(POP):
    a, b, c = POP.shape

    for i in range(a):
        for j in range(b):
            for k in range(c):
                POP[i][j][k] = random.randint(0, 1)

    return POP


def QR(img_path, POP, X1, Y1, X2, Y2, path_adv, De):

    img = cv2.imread(img_path)
    L = int((Y2 - Y1) / 5)
    R = int(L/25)
    if R <= 0:
        R = 1


    a = 0

    # print('**************', int(X1 + (X2 - X1) / 4), int(X2 - (X2 - X1) / 4), int(L / De))
    for i in range(int(X1 + (X2 - X1) / 4), int(X1 + (X2 - X1) / 4) + L, int(L / De)):

        if a == De + 1:
            continue
        b = 0
        for j in range(int(Y1 + (Y2 - Y1) / 3), int(Y1 + (Y2 - Y1) / 3) + L, int(L / De)):
            # Ran = random.randint(0, 1)
            # print('Ran = ', Ran)
            # print('a, b = ', a, b)
            if b == De + 1:
                continue
            if POP[a][b] == 0:
                pts = np.array([[i, j], [i, j + int(L / De)], [i + int(L / De), j + int(L / De)], [i + int(L / De), j]],
                               np.int32)
                cv2.polylines(img, [pts], True, (0, 0, 0), R)
            b = b + 1
        a = a + 1

    cv2.imwrite(path_adv, img)

def QR_ablation_C(img_path, POP, X1, Y1, X2, Y2, path_adv, De, C):

    img = cv2.imread(img_path)
    L = int((Y2 - Y1) / 5)
    R = int(L/25)
    if R <= 0:
        R = 1


    a = 0

    # print('**************', int(X1 + (X2 - X1) / 4), int(X2 - (X2 - X1) / 4), int(L / De))
    for i in range(int(X1 + (X2 - X1) / 4), int(X1 + (X2 - X1) / 4) + L, int(L / De)):

        if a == De + 1:
            continue
        b = 0
        for j in range(int(Y1 + (Y2 - Y1) / 3), int(Y1 + (Y2 - Y1) / 3) + L, int(L / De)):
            # Ran = random.randint(0, 1)
            # print('Ran = ', Ran)
            # print('a, b = ', a, b)
            if b == De + 1:
                continue
            if POP[a][b] == 0:
                pts = np.array([[i, j], [i, j + int(L / De)], [i + int(L / De), j + int(L / De)], [i + int(L / De), j]],
                               np.int32)
                cv2.polylines(img, [pts], True, C, R)
            b = b + 1
        a = a + 1

    cv2.imwrite(path_adv, img)


def QR_car(img_path, POP, X1, Y1, X2, Y2, path_adv, De):

    img = cv2.imread(img_path)
    L = int((Y2 - Y1)/1.5)
    R = int(L/25)
    if R <= 0:
        R = 1


    a = 0

    # print('**************', int(X1 + (X2 - X1) / 4), int(X2 - (X2 - X1) / 4), int(L / De))
    for i in range(int(X1 + (X2 - X1) / 4), int(X1 + (X2 - X1) / 4)+L, int(L / De)):

        if a == De + 1:
            continue
        b = 0
        for j in range(int(Y1 + (Y2 - Y1) / 4), int(Y1 + (Y2 - Y1) / 4) + L, int(L / De)):
            # Ran = random.randint(0, 1)
            # print('Ran = ', Ran)
            # print('a, b = ', a, b)
            if b == De + 1:
                continue
            if POP[a][b] == 0:
                pts = np.array([[i, j], [i, j + int(L / De)], [i + int(L / De), j + int(L / De)], [i + int(L / De), j]],
                               np.int32)
                cv2.polylines(img, [pts], True, (0, 0, 0), R)
            b = b + 1
        a = a + 1

    cv2.imwrite(path_adv, img)


def selection(POP, conf):
    a, b, c = POP.shape


    for i in range(a):

        if conf[0][i] > 0.8:

            for j in range(b):
                for k in range(c):
                    POP[i][j][k] = random.randint(0, 1)

    return POP

def crossover(POP, Rc):
    a, b, c = POP.shape

    for i in range(0, a, 2):

        if random.randint(1, 10)/10 > Rc:
            continue

        for j in range(0, int(b/2)):

            for k in range(0, c):

                tag = POP[i][j][k]
                POP[i][j][k] = POP[i+1][j][k]
                POP[i+1][j][k] = tag


    return POP


def mutation(POP, Rm):
    a, b, c = POP.shape

    for i in range(a):

        if random.randint(1, 10)/10 > Rm:
            continue

        j = random.randint(0, b-1)
        k = random.randint(0, c-1)

        # print('j, k = ', j, k)

        if POP[i][j][k] == 0:
            POP[i][j][k] = 1
        else:
            POP[i][j][k] = 0

    return POP



















