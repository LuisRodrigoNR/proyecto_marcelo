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
posQ = "s"
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

c=0

#Como la letra g es la que mas se repite podemos decir que esta es la letra e

#posG = 'e'

#probando con qggq

# for p in dicEng:
#       if len(p)==4:
#             if p[1]==p[2] and p[1] in posG and p[0]==p[-1]:
#                   c+=1
#                   print(p)
# print(c)

#sees
#posQ = 's'

#probando con dobqgn

# for p in dicEng:
#       if len(p)==6:
#             if p[4] in posG and p[3] in posQ and p[2]!=p[3] and p[-1]!=p[3]:
#                   c+=1
#                   print(p)
# print(c)

#chosen biased closer closed raised caused poised

#posD = 'cbrp'
#posO = 'ilao'
#posB = 'aoiu'
#posN = 'ndr'

#probando con xonqgclvb

for p in dicEng:
      if len(p)==9:
            if p[3:5]=='se':
                  c+=1
                  print(p)
print(c)

# 