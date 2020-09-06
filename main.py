from REPORTE_01_GARDUÑO_DAVID import *
from lifestore_file import *

admins = ["David", "Javier", "Emtech"]

print("Para accesar al reporte, ingrese su nombre como usuario empezando con mayúscula y usando la contraseña 'admin', si esta registrado en la base de datos como administrador, se le dara acceso.")

user = input("Ingrese el nombre de usuario: ")
passw = input("Ingrese la contraseña: ")

if user in admins and passw == "admin":
  print("Administrador identificado. Bienvenido, " + user + ".")

  print("_______________________________________________")
  print("Reporte de ventas global")
  print("_______________________________________________")
  print("-> Ventas totales hasta el momento:", len(lifestore_sales))
  print("-> Ingresos hasta el momento: $", ganancia_total )
  print("-> Ventas registradas en 2019: 1")
  print("-> Ventas registradas en 2020:", len(lifestore_sales) - 1)

  print("--- Productos mas vendidos  ---")
  print("Unid Vend | Id.prod | Busqued | Devoluc | Stock | Score promedio")
  for j in range(0, 20):
    print("   ", maxs_total[j][1], "      " ,maxs_total[j][0], "      ", busquedas_total[maxs_total[j][0] - 1][1], "       ", maxs_total[j][3], "      " ,lifestore_products[maxs_total[j][0] - 1][-1], "     " ,maxs_total[j][2])
  print("-> El producto que mas se ha vendido es " +  lifestore_products[maxventas_total[0] - 1][1] + " el cual se vendieron", maxventas_total[1] ,"unidades y que tiene una calificación media de los compradores de", maxventas_total[2], ". Se han devuelto", maxventas_total[3], "unidades." )

  print("--- Producto sin ventas --- ")
  print("Se han registrado ", len(sin_ventas), "productos sin ventas" )
  print("Id.prod | Busqued | Stock |")
  for j in range(0, len(sin_ventas)):
    print("   ", sin_ventas[j][0], "      ", busquedas_total[sin_ventas[j][0] - 1][1], "      ",  lifestore_products[sin_ventas[j][0] - 1][-1])  

  print("--- Productos con peor calificación media ---")
  print("Existen 5 productos que han recibido una calificación menor o igual a 3.")
  print("Unid Vend | Id.prod | Busqued | Devoluc | Stock | Score promedio")
  for j in range(0, 10):
    print("   ", mins_total[j][1], "       " ,mins_total[j][0], "      ", busquedas_total[mins_total[j][0] - 1][1], "       ", mins_total[j][3], "      " ,lifestore_products[mins_total[j][0] - 1][-1], "     " ,mins_total[j][2])

  print("--- Productos con mejor calificación media ---")
  print("En total 18 productos han recibido una calificación excelente, es decir, de 5.")
  print("Unid Vend | Id.prod | Busqued | Devoluc | Stock | Score promedio")
  for j in range(0, 20):
    print("   ", maxs_score[j][1], "       " ,maxs_score[j][0], "      ", busquedas_total[maxs_score[j][0] - 1][1], "       ", maxs_score[j][3], "      " ,lifestore_products[maxs_score[j][0] - 1][-1], "     " ,maxs_score[j][2])
  print("--- Ventas por categoria ---")
  print("Se presentan los articulos vendidos por categoria.")
  print("Unid Vend | Busqued | Categoria ")
  for dato in categoria:
    print("  ", dato[1], "      ", dato[2], "      " ,  dato[0])

  for j in range (0, 9):
    print("_______________________________________________")
    print("Reporte de ventas", meses[j])
    print("-> Ventas totales en el mes:", ganancias[j][1], "productos.")
    print("-> Ingresos por ventas del mes: $", ganancias[j][2])
    print("--- Ventas mensuales ---")
    print("Id prod | Unid Vend | Categoria ")
    for k in range(0, len(prod_comb[j])):
      print("   ", prod_comb[j][k][0], "       ", prod_comb[j][k][1], "     ", prod_comb[j][k][4] )
else:
  print("Usted no cuenta con permisos de administrador, mejor vaya de chismoso al muro de su ex en Facebook :)")
input("Para cerrar esta ventana, escriba 'adios': ")
