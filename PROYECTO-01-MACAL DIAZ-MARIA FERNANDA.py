#Importar registro de compras, búsquedas y productos de la tienda.
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#Importar librería Numpy
import numpy as np

#Bienvenida al programa
print ("Bienvenido(a) a LifeStore")

#Log In usuario
if __name__ == "__main__":
    Usuario = "fer_macal"
    Contraseña = "lifestore2021"
    username = input('Ingrese Usuario:\n > ')
    password = input('Ingrese Contraseña:\n > ')
    if username == Usuario:
        if password == Contraseña:
            print("¡Buen día! Ha ingresado exitosamente a LifeStore")
        else:
            print("Contraseña errónea, vuelva a intentarlo")
    else:
        print('Lo sentimos, el usuario no existe')


#Indicar el número de productos en el inventario
inventario = len(lifestore_products)
print(f'El número de productos únicos en el inventario es de {inventario}.')

#Redefinir la lista lifestore_sales excluyendo las devoluciones
lifestore_sales_n = []
for i in range(len(lifestore_sales)):
    if lifestore_sales[i][4] != 1:
        lifestore_sales_n.append(lifestore_sales[i])


#Construcción de listas de ventas mensuales
meses = ['/01','/02','/03','/04','/05','/06','/07','/08','/09','/10','/11','/12']

def meses_l(n):
    mes = []
    for datos in lifestore_sales_n:
        fecha_venta = datos[3]
        if meses[n] in fecha_venta:
            mes.append(datos)
    return mes


def ventas_mes(m):
    id = []
    for i,datos in enumerate(m):
        id.append([m[i][1]])
    values, count = np.unique(id, return_counts=True)
    return [values, count]

# def resenas(m):
#     id = []
#     for i,datos in enumerate(m):
#         id.append([ m[i][2], m[i][1] ])
#     for i,datos in enumerate(id):
#         if id [i-1][1] == id [i][1]:
#             id [i][0] += id [i-1][0]
#     values, indx = np.unique(id, return_index=True)
#     return id

enero = ventas_mes(meses_l(0))
febrero = ventas_mes(meses_l(1))
marzo = ventas_mes(meses_l(2))
abril = ventas_mes(meses_l(3))
mayo = ventas_mes(meses_l(4))
junio = ventas_mes(meses_l(5))
julio = ventas_mes(meses_l(6))
agosto = ventas_mes(meses_l(7))
septiembre = ventas_mes(meses_l(8))
octubre = ventas_mes(meses_l(9))
noviembre = ventas_mes(meses_l(10))
diciembre = ventas_mes(meses_l(11))

#imprimir los reportes mensuales
print(enero)
print(febrero)
print(marzo)
print(abril)
print(mayo)
print(junio)
print(julio)
print(agosto)
# print(septiembre)
# print(octubre)
# print(noviembre)
# print(diciembre)

