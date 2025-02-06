#Seccion de imports
import os
import time

def agregar_producto(inventario):
  nombre = input("Nombre del producto: ")
  precio = input("Precio del producto: ")
  precio_decimal = precio.replace(",", ".")
  precio = float(precio_decimal)
  cantidad = int(input("Cantidad del producto: "))
  producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad}
  inventario.append(producto)

  print("Producto agregado correctamente")
  time.sleep(3)
  os.system("cls")
  return inventario

def eliminar_producto(inventario):
  if len(inventario) == 0:
    print("No hay productos en el inventario. Por favor, agrega un producto")
    time.sleep(3)
    os.system("cls")
    return inventario
  else: 
    print(inventario)
    producto_a_eliminar = input("Nombre del producto a eliminar: ")
    for producto in inventario:
      if producto["nombre"].lower() == producto_a_eliminar.lower():
        if producto["cantidad"] > 1:
          print("Cuantos desea eliminar?")
          cantidad_a_eliminar = int(input("==> "))
          producto["cantidad"] -= cantidad_a_eliminar
          if producto["cantidad"] == 0:
            inventario.remove(producto)
          elif producto["cantidad"] < 0:
            producto["cantidad"] += cantidad_a_eliminar
            print(" La cantidad a eliminar es mayor a la cantidad en inventario, vuelva a intentarlo")
            time.sleep(3)
            os.system("cls")
            break
          else:
            print("Producto eliminado correctamente")
            time.sleep(2)
            os.system("cls")
            break

          print("Producto eliminado correctamente")
          time.sleep(2)
          os.system("cls")
          break

        else:
          inventario.remove(producto)
          print("Producto eliminado correctamente")
          time.sleep(3)
          os.system("cls")
          break

      else:
        print("Producto no encontrado")
        time.sleep(3)
        os.system("cls")
        continue
  return inventario

def ver_productos(inventario):
    if len(inventario) == 0:
      print("No hay productos en el inventario. Por favor, agrega un producto")
      time.sleep(3)
      os.system("cls")
      return inventario

    else:
      print("-------------------------------")
      for producto in inventario:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        print("-------------------------------")
      espera = input("Presiona enter para continuar\n")
      time.sleep(2)
      os.system("cls")
      return inventario

inventario = []

while True:
  print("1) Agregar un producto")
  print("2) Eliminar un producto")
  print("3) Ver todos los productos")
  print("4) Salir")
  opcion = input("Selecciona una opcion: ")

  if opcion == "1":
    inventario = agregar_producto(inventario)

  elif opcion == "2":
    inventario=eliminar_producto(inventario)

  elif opcion == "3":
    ver_productos(inventario)

  elif opcion == "4":
    print("Saliendo del programa...")
    time.sleep(3)
    os.system("cls")
    break

  else:
    print("Opcion no valida")
    time.sleep(1)
    os.system("cls")
    continue