import random
def generarDatos():
    datos=[]
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(['ACH01','ACH22','ACH43'])
        marca=random.choice(['Sony','Kalley','Haceb'])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(['Itagui','Envigado','Medellín','Sabaneta','Barbosa'])
        responsable=random.choice(['Camila Builes','Laura Toro','Gandalf Toro','Yiyo Builes','Dante Builes'])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos

print(generarDatos())