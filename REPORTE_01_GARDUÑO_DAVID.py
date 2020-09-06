from lifestore_file import *

'''
busquedas_mes = [id_prod, # busquedas]
ventas_mes = [mismo formato que sales]
prod_mes = [id_prod, # ventas, prom score, # devol]
categoria = [id_prod, # ventas, # busqued]
'''
busquedas_total = []
r = 1
while r < 97:
  cont = 0
  for busqueda in lifestore_searches:
    if busqueda[1] == r:
      cont += 1
  busquedas_total.append([r, cont])
  r += 1

ventas_enero = []
for dato in lifestore_sales:
  if dato[3][3:5] == "01":
    ventas_enero.append(dato)
ventas_febrero = []
for dato in lifestore_sales:
  if dato[3][3:5] == "02":
    ventas_febrero.append(dato)
ventas_marzo = []
for dato in lifestore_sales:
  if dato[3][3:5] == "03":
    ventas_marzo.append(dato)
ventas_abril = []
for dato in lifestore_sales:
  if dato[3][3:5] == "04":
    ventas_abril.append(dato)
ventas_mayo = []
for dato in lifestore_sales:
  if dato[3][3:5] == "05":
    ventas_mayo.append(dato)
ventas_junio = []
for dato in lifestore_sales:
  if dato[3][3:5] == "06":
    ventas_junio.append(dato)
ventas_julio = []
for dato in lifestore_sales:
  if dato[3][3:5] == "07":
    ventas_julio.append(dato)
ventas_agosto = []
for dato in lifestore_sales:
  if dato[3][3:5] == "08":
    ventas_agosto.append(dato)
ventas_sep = []
for dato in lifestore_sales:
  if dato[3][3:5] == "09":
    ventas_sep.append(dato)


prod_total = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in lifestore_sales:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_total.append([indice, contador1, contador2/contador1, contador3])
  else: 
    prod_total.append([indice, 0, 5, 0])

maxventas_total = [0, 0, 0, 0]
for dato in prod_total:
  if maxventas_total[1] < dato[1]:
    maxventas_total = dato
minscore_total = [0, 0, 5, 0]
for dato in prod_total:
  if dato[2] < minscore_total[2] :
    minscore_total = dato
i = 0
auxprod = prod_total[:]
maxs_total = []
while i < 20:
  newmax = [0, 0, 0, 0]
  for dato in auxprod:
    if newmax[1] < dato[1]:
      newmax = dato
  maxs_total.append(newmax)
  auxprod.remove(newmax)
  i += 1
k = 0
auxprod2 = prod_total[:]
mins_total = []
while k < 10:
  newmin = [0, 0, 5, 0]
  for dato in auxprod2:
    if dato[2] < newmin[2]:
      newmin = dato
  mins_total.append(newmin)
  auxprod2.remove(newmin)
  k += 1
l = 0
auxprod3 = prod_total[:]
maxs_score = []
while l < 20:
  newmax_score = [0, 0, 0, 0]
  for dato in auxprod3:
    if dato[2] > newmax_score[2] and dato[1] != 0:
      newmax_score = dato
  maxs_score.append(newmax_score)
  auxprod3.remove(newmax_score)
  l += 1

ganancia_total = 0
for dato in prod_total:
  ganancia_total += dato[1]*lifestore_products[dato[0] - 1][2]

sin_ventas = []
for dato in prod_total:
  if dato[1] == 0:
    sin_ventas.append(dato)

a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
z, y, x, w, v, u, t, s = 0, 0, 0, 0, 0, 0, 0, 0  
for dato in prod_total:
  if dato[0] > 0 and dato[0] < 10:
    a += dato[1]
    z +=busquedas_total[dato[0] - 1][1] 
  elif dato[0] > 9 and dato[0] < 29:
    b  += dato[1]
    y +=busquedas_total[dato[0] - 1][1]
  elif dato[0] > 28 and dato[0] < 47:
    c  += dato[1]
    x +=busquedas_total[dato[0] - 1][1]
  elif dato[0] > 46 and dato[0] < 60:
    d  += dato[1]
    w +=busquedas_total[dato[0] - 1][1]
  elif dato[0] > 59 and dato[0] < 62:
    e  += dato[1]
    v +=busquedas_total[dato[0] - 1][1]
  elif dato[0] > 61 and dato[0] < 74:
    f  += dato[1]
    u +=busquedas_total[dato[0] - 1][1]
  elif dato[0] > 73 and dato[0] < 84:
    g  += dato[1]
    t +=busquedas_total[dato[0] - 1][1]
  else:
    h += dato[1]
    s +=busquedas_total[dato[0] - 1][1]
categoria = (["Procesadores", a, z], ["Tarjetas de video", b, y], ["Tarjetas madre", c, x], ["Discos duro", d, w], ["Memorias RAM", e, v], ["Pantallas", f, u], ["Bocinas", g, t], ["Audifonos", h, s],)



prod_enero = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_enero:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_enero.append([indice, contador1, contador2/contador1, contador3])

prod_febrero = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_febrero:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_febrero.append([indice, contador1, contador2/contador1, contador3])

prod_marzo = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_marzo:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_marzo.append([indice, contador1, contador2/contador1, contador3])

prod_abril = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_abril:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_abril.append([indice, contador1, contador2/contador1, contador3])

prod_mayo = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_mayo:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_mayo.append([indice, contador1, contador2/contador1, contador3])

prod_junio = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_junio:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_junio.append([indice, contador1, contador2/contador1, contador3])

prod_julio = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_julio:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_julio.append([indice, contador1, contador2/contador1, contador3])

prod_agosto = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_agosto:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_agosto.append([indice, contador1, contador2/contador1, contador3])

prod_sep = []
for indice in range(1, 97):
  contador1 = 0
  contador2 = 0
  contador3 = 0
  for producto in ventas_sep:
    if producto[1] == indice:
      contador1 += 1
      contador2 += producto[2]
      contador3 += producto[4]
  if contador1 != 0:
    prod_sep.append([indice, contador1, contador2/contador1, contador3])

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"]
prod_comb = [prod_enero, prod_febrero, prod_marzo, prod_abril, prod_mayo, prod_junio, prod_julio, prod_agosto, prod_sep]

ganancias = []
for d in range(0, 9):
  ganancia_acumulada = 0
  ventas_acumuladas = 0
  for dato in prod_comb[d]:
    ganancia_acumulada += dato[1]*lifestore_products[dato[0] - 1][2]
    ventas_acumuladas += dato[1]
  ganancias.append([meses[d], ventas_acumuladas,  ganancia_acumulada])

for d in range(0, 9):
  for dato in prod_comb[d]:
    if dato[0] > 0 and dato[0] < 10: 
      dato.append("Procesador")
    elif dato[0] > 9 and dato[0] < 29:
      dato.append("Tarjeta de video")
    elif dato[0] > 28 and dato[0] < 47:
      dato.append("Tarjeta madre")
    elif dato[0] > 46 and dato[0] < 60:
      dato.append("Disco duro")
    elif dato[0] > 59 and dato[0] < 62:
      dato.append("Memoria RAM")
    elif dato[0] > 61 and dato[0] < 74:
      dato.append("Pantalla")
    elif dato[0] > 73 and dato[0] < 84:
      dato.append("Bocinas")
    else:
      dato.append("Audifonos")


