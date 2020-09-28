"""
Created on Sat Sep 26 18:13:32 2020
@author: David Garduño Guzmán
contraseña para ver datos: proyecto2GGD

colnames:
    register_id	direction	
    origin	
    destination	
    year	
    date	
    product	
    transport_mode	
    company_name	
    total_value

"""
import csv

pss_exp = []
pss_imp = []
pss_exp_des = []
pss_imp_des = []
tpts_exp = []
tpts_imp = [] 
datos_exp = []
datos_imp = []

with open("synergy_logistics_database.csv", "r") as database:
    
   lector = csv.DictReader(database)
   for linea in lector:
        if linea["direction"] == "Exports":
            pss_exp.append(linea["origin"])
            pss_exp_des.append(linea["destination"])
            tpts_exp.append(linea["transport_mode"])
            datos_exp.append(linea)
        else:
            pss_imp.append(linea["origin"])
            pss_imp_des.append(linea["destination"])
            tpts_imp.append(linea["transport_mode"])
            datos_imp.append(linea)
        transp_imp = set(tpts_exp)
        transp_exp = set(tpts_imp)
        paises_imp = set(pss_imp)
        paises_exp = set(pss_exp)
        paises_imp_des = set(pss_imp_des)
        paises_exp_des = set(pss_exp_des)

def normalizar(lista):
    for diccionario in lista:
        diccionario["register_id"] = int(diccionario["register_id"])
        diccionario["year"] = int(diccionario["year"])
        diccionario["total_value"] = int(diccionario["total_value"])
normalizar(datos_exp)
normalizar(datos_imp)

def truncar(numero):
    cadena = str(numero)
    if len(cadena) >= 5:
        nuevo_n = cadena[0:6]
    else:
        nuevo_n = cadena
    return (nuevo_n + " %")

def valor_acumulado(parametro, tabla, lista):
    guardado = []
    for dato0 in tabla:
        aux = []
        for diccionario in lista:
            if diccionario[parametro] == dato0:
                aux.append(diccionario["total_value"])
        guardado.append({parametro:dato0, "total":sum(aux)})
    ayuda =[]
    for minidicc in guardado:
        ayuda.append(minidicc["total"])
    for minidicc2 in guardado:
        minidicc2["percent"] = (minidicc2["total"] / sum(ayuda)) * 100
        minidicc2["presentable"] = truncar(minidicc2["percent"])
    final = sorted(guardado, key = lambda dicc : dicc["total"], 
                   reverse = True)
    return final

datos_exp_t = valor_acumulado("transport_mode", transp_exp, datos_exp) 
datos_imp_t = valor_acumulado("transport_mode", transp_imp, datos_imp)
datos_exp_p = valor_acumulado("origin", paises_exp, datos_exp)
datos_imp_p = valor_acumulado("origin", paises_imp, datos_imp)

def presentar(parametro, lista):
    for dato1 in lista:
        print("El valor por", dato1[parametro], 
              "es de: ", dato1["total"], "( ", dato1["presentable"], ")" )

def rutas(lista_origen, lista_destino, lista_datos):
    guardado2 = []
    for dato1 in lista_origen:
        for dato2 in lista_destino:
            aux2 = []
            for dato_base in lista_datos:
                if dato_base["origin"] == dato1 and dato_base["destination"] == dato2:
                    aux2.append(dato_base["total_value"])
            if sum(aux2) != 0:
                guardado2.append({"origen":dato1, "destino":dato2, 
                                              "total":sum(aux2)})
    final2 = sorted(guardado2, key = lambda dicc2 : dicc2["total"], 
                    reverse = True)
    return final2

rutas_imp = rutas(paises_imp, paises_imp_des, datos_imp)
rutas_exp = rutas(paises_exp, paises_exp_des, datos_exp)

def presentar_rutas(lista_rutas, cantidad):
    if cantidad <= len(lista_rutas):
        for i in range(0, cantidad):
            print("De", lista_rutas[i]["origen"], "a", lista_rutas[i]["destino"], 
                  "el valor es de: ", lista_rutas[i]["total"])
    else: 
        print("No existen tantos datos a mostrar")
                                                                                          
# A mostrar
password = input("Ingrese la contraseña: ")
contador = 0
while password != "proyecto2GGD":
    contador += 1
    print("Contraseña incorrecta, quedan", 4 - contador, "intento(s).")
    password = input("Vuelva a ingresar la contraseña: ")    
    if contador == 3:
        break

if password == "proyecto2GGD": 
    print("Bienvendido. Los datos estan organizados descendentemente.")
    print("Seleccione una opcion: ")
    print("1) Valor de las transacciones por ruta.")
    print("2) Valor de las transacciones por medios de transportes.")
    print("3) Valor de las transacciones por valor y pais de movimiento.")
    print("4) Cerrar el programa")
    informe = int(input("¿Qué datos le gustaría ver? Ingrese el número: "))
    while informe != 4:
        if informe == 1:
            cant = int(input("Ingrese cuantas rutas de exportación desea ver (Max. 144): "))
            print("-- Exportaciones --")
            presentar_rutas(rutas_exp, cant)
            cant2 = int(input("Ingrese cuantas rutas de importación desea ver (Max. 49): "))
            print("-- Importaciones --")
            presentar_rutas(rutas_imp, cant2)
        if informe == 2:
            print("-- Exportaciones --")
            presentar("transport_mode", datos_exp_t)
            print("-- Importaciones --")
            presentar("transport_mode", datos_imp_t)
        if informe == 3:
            print("-- Exportaciones --")
            presentar("origin", datos_exp_p)
            print("-- Importaciones --")
            presentar("origin", datos_imp_p)
        informe = int(input("¿Le gustaria ver otro dato? En caso negativo, ingrese el 4: "))
        
    