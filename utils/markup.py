import os
import cv2
import matplotlib.pyplot as plt
import random
import imutils
import time
import shutil
import numpy as np
from utils.utils import resize_to_fit


def get_separate_letters(image):

    #image_resize = cv2.resize(image, (200, 10), cv2.INTER_AREA)
    #image_resize = cv2.resize(image_resize, (200, 60), cv2.INTER_AREA)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gray = cv2.threshold(gray, 100, 250, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    #cv2.imshow("Preview", gray)
    
    #finalImg = gray
    
    #contours = cv2.findContours(finalImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #contours = contours[0]

    #letter_image_regions = []

    letter1 = gray[0:64, 130:160]
    letter2 = gray[0:64, 155:185]
    letter3 = gray[0:64, 180:205]
    letter4 = gray[0:64, 200:225]
    letter5 = gray[0:64, 220:245]
    letter6 = gray[0:64, 240:275]

    letters = []

    letters.append(letter1)
    letters.append(letter2)
    letters.append(letter3)
    letters.append(letter4)
    letters.append(letter5)
    letters.append(letter6)

    # for contour in contours:
        #(x, y, w, h) = cv2.boundingRect(contour)

        #y = 0
        #h = 60

        #if w / h > 1.0:
        #    if w < 75:
        #        half_width = int(w / 2)
        #        letter_image_regions.append((x, y, half_width, h))
        #        letter_image_regions.append((x + half_width, y, half_width, h))
        #    else:
        #         aaa = int(w / 3)
        #         letter_image_regions.append((x, y, aaa, h))
        #         letter_image_regions.append((x + aaa, y, aaa, h))
        #         letter_image_regions.append((x + 2 * aaa, y, aaa, h))
        # else:
        #     letter_image_regions.append((x, y, w, h))

    # letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])
    # letters = []

    # for letter_bounding_box in letter_image_regions:
    #     x, y, w, h = letter_bounding_box

    #     image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     image_gray = cv2.threshold(image_gray, 50, 250, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #     letter_image = image_gray[2:59, x - 5:x + w + 5]

    #     if w > 15 and letter_image.shape[1] > 15:
    #         letters.append(letter_image)

    return letters

def create_train_set(output_folder, markup_files):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    counts = {}
    fails = 0
    
    for file in markup_files:
        filename = file.replace('\\', '/')
        labels = [x for x in filename.split('/')[-1].split('.')[0]]

        image = plt.imread(filename)

        letters = get_separate_letters(image)

        if len(letters) != 0 and len(letters) == len(labels):
            for letter, label in zip(letters, labels):
                save_path = os.path.join(output_folder, label)

                if not os.path.exists(save_path):
                    os.makedirs(save_path)

                count = counts.get(label, 1)
                p = os.path.join(save_path, "{}.jpg".format(str(count).zfill(6)))

                cv2.imwrite(p, letter)
                counts[label] = count + 1
        else:
            fails += 1
            print("letters count = {}, labels count = {}".format(len(letters), len(labels)))

    print('Total: ' + str(len(markup_files)) + ' Fails: ' + str(fails))
