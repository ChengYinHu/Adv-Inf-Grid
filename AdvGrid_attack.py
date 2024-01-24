import cv2
import random
import numpy as np
import matplotlib.pyplot as plt
import os
from functions import initiation, QR, selection, crossover, mutation


from detect_single_img import detect_v3_inf




De = 8 #dimension
Seed =50
Step = 10
Rc = 0.6
Rm = 0.1

ASR, Query, count_all = 0, 0, 0




dir_inf = r'C:\Users\a\PycharmProjects\pythonProject\yolo_v3_train\yolo_v3\data\custom\val_people'

file = os.listdir(dir_inf)

for id, pic in enumerate(file):



    picture = dir_inf + '/' + pic

    print('id, picture, count_all', id, picture, count_all)

    path_adv = 'adv.jpg'

    res_clean_inf = detect_v3_inf(picture)

    shape_inf, b1 = res_clean_inf.shape

    print('shape_inf = ', shape_inf)

    if shape_inf != 1:
        tag = 1
        continue

    X1, Y1, X2, Y2 = int(res_clean_inf[0][0]), int(res_clean_inf[0][1]), int(res_clean_inf[0][2]), int(res_clean_inf[0][3])


    count_all = count_all + 1

    POP = np.zeros((Seed, De, De))

    conf = np.ones((1, Seed))

    # print('POP = ', POP)
    #
    # print('conf = ', conf)

    POP = initiation(POP)

    # print('POP = ', POP)


    tag_break = 0
    for step in range(Step):
        for seed in range(Seed):

            Query = Query + 1

            print('count_all, step, seed, ASR, Query = ', count_all, step, seed, ASR, Query)

            QR(picture, POP[seed], X1, Y1, X2, Y2, path_adv, De-1)

            # img_show = plt.imread(path_adv)
            # plt.imshow(img_show)
            # plt.show()

            res_adv = detect_v3_inf(path_adv)

            print(res_adv.shape)

            if res_adv.shape == (0, 6):
                tag_break = 1
                ASR = ASR + 1
                break

            # print('res_adv[0][4] = ', res_adv[0][4])

            conf[0][seed] = res_adv[0][4]

        if tag_break == 1:
            break

        # print('POP = ', POP)

        # print('conf = ', conf)

        POP = selection(POP, conf)

        # print('POP = ', POP)

        POP = crossover(POP, Rc)

        # print('POP = ', POP)

        POP = mutation(POP, Rc)

        # print('POP = ', POP)




    # if shape_inf == 1:
    #     break
print('ASR, Query = ', ASR, Query)
print('ASR/count_all, Query/count_all = ', ASR/count_all, Query/count_all)



