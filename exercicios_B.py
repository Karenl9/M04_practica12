#Crear una funcion que muestre por consola y guarde un archivo externo,
#un JSON con una key de nombre book que contenga titel, cover, year i pages.
#Dentro del JSON habran 4 en book.

import json
def maex():

     datas ="""
          {"book":[
               {"titel": "Crepusculo",
               "cover": "uno",
               "year": "1000",
               "pages": "7"},
               {"titel": "La casa fantasma",
               "cover": "9000",
               "year": "0",
               "pages": "120"}
               {"titel": "El nombre del viento",
               "cover": "6",
               "year": "2001",
               "pages": "250"
               {"title": "El gato con botas",
               "cover": "3000",
               "year": "2030",
               "pages": "220"}
     
          ]
     } """

     with open("datas", 'w') as file:
         json.dump(datas,file)

# Crear una función que lea el JSON del ejercicio y salga el resultado (en formato json) por consola.
     with open("datas", 'r') as file:
          result = json.load(file)
          print(result)

maex()

