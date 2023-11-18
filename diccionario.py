import wikipediaapi                 #pip install wikipedia-api
import re
import unidecode                    #pip install unidecode
import matplotlib.pyplot as plt     #pip install matplotlib
from collections import Counter
from scipy.stats import pearsonr    #pip install scipy

#sacare palabras de una pagina de wikipedia utilzando su API

def consulta(pagina,idioma):

    user_agent ="diccionario (https://github.com/FMM28/proyecto_marcelo.git)"
    wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent,language=idioma)

    page = wiki_wiki.page(pagina)

    datos = page.text.split()
    diccionario=[]

    for i in datos:
        i=valida(i)
        if not i in diccionario:          #Filtra las repetidas
            diccionario.append(i)
    return diccionario

def cuenta(lista):
    letras = ''.join(lista)                             #Junta todas las palabras de la lista en una sola
    frecuencias = Counter(letras)                       #Cuenta la frequencia con la que se repite cada letra
    letras_ordenadas = frecuencias.most_common()        #Ordena las letras
    letras, frecuencias = zip(*letras_ordenadas)        #Separa las letras de las frecuencias para graficarlas
    return letras,frecuencias

def grafica(lista,idioma):
    letras, frecuencias = cuenta(lista)
    
    plt.bar(letras, frecuencias)                        #Grafica
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de Letras '+idioma)
    plt.show()

def grafica2(lista1,lista2,idioma,texto):
    letras, frecuencias = cuenta(lista1)
    letras2, frecuencias2= cuenta(lista2)
    correlacion = pearsonr(frecuencias[:20], frecuencias2[:20]).correlation

    
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))

    # Grafica el primer conjunto de frecuencias
    axs[0].bar(letras, frecuencias)
    axs[0].set_title(idioma)

    # Grafica el segundo conjunto de frecuencias
    axs[1].bar(letras2, frecuencias2)
    axs[1].set_title(texto)

    plt.suptitle('Comparación de frecuencias')
    plt.figtext(0.01, 0.01, 'Correlacion '+str(correlacion), fontsize=10)
    plt.show()

    return correlacion,idioma

def valida(palabra):
    return unidecode.unidecode(re.sub(r'[^A-Za-záéíóúüñÁÉÍÓÚÜÑç]','',palabra)).lower()

def guarda(lista,nombre):
    
    datos = ' '.join(lista)
    nombre=nombre+'.txt'
    with open(nombre,'w') as archivo:
        archivo.write(datos)
    
#consigue datos de paginas de wikipedia

dicEng=consulta('YouTube','en')
dicEng.extend(consulta('Facebook','en'))
dicEng.extend(consulta('Wikipedia','en'))

dicFr=consulta('YouTube','fr')
dicFr.extend(consulta('Facebook','fr'))
dicFr.extend(consulta('Wikipedia','fr'))

dicAle=consulta('YouTube','de')
dicAle.extend(consulta('Facebook','de'))
dicAle.extend(consulta('Wikipedia','de'))

dicPor=consulta('YouTube','pt')
dicPor.extend(consulta('Facebook','pt'))
dicPor.extend(consulta('Wikipedia','pt'))

dicIt=consulta('YouTube','it')
dicIt.extend(consulta('Facebook','it'))
dicIt.extend(consulta('Wikipedia','it'))

#Guarda los diccionarios

guarda(dicEng,'dicEng')
guarda(dicFr,'dicFr')
guarda(dicAle,'dicAle')
guarda(dicPor,'dicPor')
guarda(dicIt,'dicIt')

#imprime la longitud de las listas de palabras

# print('ingles',len(dicEng))
# print('frances',len(dicFr))
# print('aleman',len(dicAle))
# print('portugues',len(dicPor))
# print('italiano',len(dicIt))

#grafica las frecuencias de las listas
    
# grafica(dicEng,'ingles')
# grafica(dicFr,'frances')
# grafica(dicAle,'aleman')
# grafica(dicPor,'portugues')
# grafica(dicIt,'italiano')

#grafica las frecuencias de los textos dados

# texto1='Jigcg xet onug e Uovnjcwfen xio mottgttgq jig fotj xonqgclvb Dootg wov uen afedang, loc gpgcw qew xign ig patajgq jig ngtj, jig Dootg ieq beaq e ygevjalvb, dbajjgcand, dobqgn gdd. Jig Uovnjcwfen jooh jig gddt jo fechgj enq toon ygden jo dgj caui. Yvj aj xet noj bond yglocg ig dcgx afmejagnj xaji jig Dootg yguevtg tig depg iaf onbw e tandbg dobqgn gdd e qew. Ig xet noj dgjjand caui letj gnovdi. Jign ong qew, eljgc ig ieq lanatigq uovnjand iat fongw, jig aqge uefg jo iaf jiej ig uovbq dgj ebb jig dobqgn gddt ej onug yw habband jig Dootg enq uvjjand aj omgn. Yvj xign jig qggq xet qong, noj e tandbg dobqgn gdd qaq ig lanq, enq iat mcguaovt Dootg xet qgeq'
# texto2='Tp sparnq oj Ijq jrd ebpqoj. At h p ijpzgnzk oj kajgjr. Pz bjf-oj-gcpzrrjj, at h p zq rptnq pljg zq kapqn, zqj rpttj-p-spqejb, zqj gzaraqj rkpgajzrj jd vpzqj jd zqj rpttj oj ipaq. At p wpad gnqrdbzabj jq ktzr zqj ijttj ljbpqop gnqdjqpqd zqj iaitandcjxzj, knzb kbnwadjb oz rntjat jd o’zqj lzj rzb tj vpboaq. Pz rnzr-rnt, at h p zqj gplj, knzb bpqejb tj laq. Pz kbjsajb jdpej, at h p dbnar gcpsibjr. Pz ojzuajsj jdpej, at h p zq izbjpz jd ojzu gcpsibjr, onqd tp rajqqj. Opqr tj izbjpz, at h p zq ljtn o’pkkpbdjsjqd, ojr cptdjbjr jd zq rdjkkjb. Tj vpboaq jrd tnqe jd jdbnad, at h p zqj iptpqçnabj pz wnqo jd zq ipbijgzj, kbngcj oj tp djbbprrj, rzb tpxzjttj jrd knrjj zq dbpqrpd. Ojr gcpdr lajqqjqd rnzljqd gcprrjb tjr wjzattjr xza lntjqd pz ljqd'

# #validamos los textos

# texto1=valida(texto1)
# texto2=valida(texto2)

# grafica(texto1,'texto 1')
# grafica(texto2,'texto 2')

#grafica los textos con los idiomas

# correlaciones=[]

# correlaciones.append (grafica2(dicEng,texto1,'ingles','texto 1'))
# correlaciones.append (grafica2(dicFr,texto1,'frances','texto 1'))
# correlaciones.append (grafica2(dicAle,texto1,'aleman','texto 1'))
# correlaciones.append (grafica2(dicPor,texto1,'portugues','texto 1'))
# correlaciones.append (grafica2(dicIt,texto1,'italiano','texto 1'))

# mayor = max(correlaciones, key=lambda x: x[0])

# print('El que tiene mayor correlacion es '+mayor[1])

# correlaciones=[]

# correlaciones.append (grafica2(dicEng,texto2,'ingles','texto 2'))
# correlaciones.append (grafica2(dicFr,texto2,'frances','texto 2'))
# correlaciones.append (grafica2(dicAle,texto2,'aleman','texto 2'))
# correlaciones.append (grafica2(dicPor,texto2,'portugues','texto 2'))
# correlaciones.append (grafica2(dicIt,texto2,'italiano','texto 2'))

# mayor = max(correlaciones, key=lambda x: x[0])

# print('El que tiene mayor correlacion es '+mayor[1])