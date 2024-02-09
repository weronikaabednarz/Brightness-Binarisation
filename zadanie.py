import numpy as np
from PIL import Image

image = Image.open("mapa.bmp")

matrix = np.array(image)
h,w = image.size

def dark_level(percent):

    if percent >= 1 and percent <= 99:
        
        x = int(percent/100 * 256)
        for i in range(h):
            for j in range(w):
                if matrix[j,i] - x < 0:
                    matrix[j,i] = 0
                else:
                    matrix[j,i] = matrix[j,i] - x

        img = Image.fromarray(matrix)
        img.save("dark.bmp")

dark_level(80)

def bright_level(percent):

    if percent >= 10 and percent <= 20:
        
        x = int(percent/100 * 256)
        for i in range(h):
            for j in range(w):
                if matrix[j,i] + x > 255:
                    matrix[j,i] = 255
                else:
                    matrix[j,i] = matrix[j,i] + x

matrix = np.array(image)

bright_level(10)
Image.fromarray(matrix).save("bright1.bmp")
bright_level(20)
Image.fromarray(matrix).save("bright2.bmp")
bright_level(40)
Image.fromarray(matrix).save("bright3.bmp")

#...............................................................................

def binaryzacja():

    tab=[]
    tab2=[]
    for i in range(w):  
        tab.append(min(matrix[i]))
        tab2.append(max(matrix[i]))
    MIN=int(min(tab))
    MAX=int(max(tab2))
    avg = int((MIN+MAX)/2)

    for i in range(h):
        for j in range(w):
            if matrix[j,i] <= avg:
                matrix[j,i] = 0
            else:
                matrix[j,i] = 255
    
matrix = np.array(image)
binaryzacja()
Image.fromarray(matrix).save("binaryzacja1.bmp")

def binaryzacja_mediana():

    tab=[]
    for i in range(h):
        for j in range(w):
            tab.append(matrix[j,i])

    tab.sort()
    srodek = tab[int(len(tab)/2)]
    print(srodek) 

    for i in range(h):
        for j in range(w):
            if matrix[j,i] <= srodek:
                matrix[j,i] = 0
            else:
                matrix[j,i] = 255

matrix = np.array(image)
binaryzacja_mediana()
Image.fromarray(matrix).save("binaryzacja2.bmp")

def binaryzacja_reczna():

    tab=[]
    for i in range(h):
        for j in range(w):
            tab.append(matrix[j,i])

    srodek = int(input("Podaj wartosc progu:"))

    for i in range(h):
        for j in range(w):
            if matrix[j,i] <= srodek:
                matrix[j,i] = 0
            else:
                matrix[j,i] = 255

matrix = np.array(image)
binaryzacja_reczna()
Image.fromarray(matrix).save("binaryzacja3.bmp")