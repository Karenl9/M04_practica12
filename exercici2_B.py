#Crear una funció que llegeixi el JSON de l’exercici 2 i surti el resultat (en format json) per consola.
def llegirj():
datas= datas = {"book":[
          {"title": "a" },
          {"cover": "b" },
          {"year": "c" },
          {"pages": "d" }
    ]}
print(json.dumps(datas))

llegirj()