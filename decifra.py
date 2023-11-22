# import string

# for i in string.ascii_uppercase:
#     print('pos'+i+' = "'+string.ascii_lowercase+'"')

#Lo comentado lo utilice para generar las posibles letras

def carga(nombre):
    with open(nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido.split()

posA = "abcdefghijklmnopqrstuvwxyz"
posB = "abcdefghijklmnopqrstuvwxyz"
posC = "abcdefghijklmnopqrstuvwxyz"
posD = "abcdefghijklmnopqrstuvwxyz"
posE = "abcdefghijklmnopqrstuvwxyz"
posF = "abcdefghijklmnopqrstuvwxyz"
posG = "e"
posH = "abcdefghijklmnopqrstuvwxyz"
posI = "abcdefghijklmnopqrstuvwxyz"
posJ = "abcdefghijklmnopqrstuvwxyz"
posK = "abcdefghijklmnopqrstuvwxyz"
posL = "abcdefghijklmnopqrstuvwxyz"
posM = "abcdefghijklmnopqrstuvwxyz"
posN = "abcdefghijklmnopqrstuvwxyz"
posO = "abcdefghijklmnopqrstuvwxyz"
posP = "abcdefghijklmnopqrstuvwxyz"
posQ = "abcdefghijklmnopqrstuvwxyz"
posR = "abcdefghijklmnopqrstuvwxyz"
posS = "abcdefghijklmnopqrstuvwxyz"
posT = "abcdefghijklmnopqrstuvwxyz"
posU = "abcdefghijklmnopqrstuvwxyz"
posV = "abcdefghijklmnopqrstuvwxyz"
posW = "abcdefghijklmnopqrstuvwxyz"
posX = "abcdefghijklmnopqrstuvwxyz"
posY = "abcdefghijklmnopqrstuvwxyz"
posZ = "abcdefghijklmnopqrstuvwxyz"

#Texto 1
#En ingles

dicEng = carga('./diccionarios/dicEng.txt')
dicEng = list(set(dicEng))
# print(len(dicEng))

#Como la letra g es la que mas se repite podemos decir que esta es la letra e

#posG = 'e'

#probando con Dootg

c=0
for p in dicEng:
      if len(p)==6:
            if p[1]==p[2] and p[-1] in posG:
                  c+=1
                  print(p)
print(c)
