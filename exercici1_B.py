#Crear una funcion que muestre por consola y guarde un arxiu externo,
#un JSON con una key de nombre book que contendra title, cover, year i pages.
#Dentro del JSON habran 4 de cada book (se ha de llenar con valores).
import json
def mostrarc():

datas = {
     "book":[
          {"title": "a" },
          {"cover": "b" },
          {"year": "c" },
          {"pages": "d" }
     {"book": [
          {"title": "e"},
          {"cover": "f"},
          {"year": "g"},
          {"pages": "h"}
     {"book": [
          {"title": "i"},
          {"cover": "j"},
          {"year": "k"},
          {"pages": "l"}
     {"book": [
          {"title": "m"},
          {"cover": "n"},
          {"year": "ñ"},
          {"pages": "o"}

     ]
}

with open("data1", 'w') as file:
    json.dump(datas,file)

with open("data1", 'r') as file:
     result = json.load(file)
     print(result)


mostrarc()