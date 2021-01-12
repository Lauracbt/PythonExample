

nombre = ""
edad = ""
salario = ""
lista_usuarios2 = []
mayor = 0
menor = 9999
total = 0
nombre_mayor_edad = ""
nombre_menor_salario = ""

option = True
while option:
    print ("""
    1.Ingrese el usuario
    2.Imprimir usuario con mayor edad
    3.Imprimir usuario con menor salario
    4.Imprimir el número de usuarios ingresados
    5.Mostrar los nombres de los usuarios ingresados
    6.Salir
     """)
    
    option=input("¿Qué deseas hacer?: ")
    if option=="1":          
        nombre = input("Ingrese el nombre del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))
        salario = int(input("Ingrese el salario del usuario: "))
        usuario = {"nombre": nombre, "edad": edad, "salario": salario}
        lista_usuarios2.append(usuario)
        print("\n Usuario ingresado") 
        print(usuario)
       


    elif option=="2":
        print("\n El nombre del usuario con mayor edad es: ", nombre_mayor_edad) 
            
        for i in lista_usuarios2:        
            if i ["edad"] > mayor:
                mayor = i["edad"]
                nombre_mayor_edad = i["nombre"]
        print(nombre_mayor_edad)            
         


    elif option=="3":
        print("\n El usuario con menor salario es: ", nombre_menor_salario) 
        for i in lista_usuarios2:
            total = total + i ["salario"]
            if i ["salario"] < menor:
                menor = i["salario"]
                nombre_menor_salario = i["nombre"]
        print(nombre_menor_salario)


    elif option=="4":
        print("\n El numero de usuarios ingresados es: ") 
        cont = 0
        for i in lista_usuarios2:
            cont = cont + 1  
        print(cont)


    elif option=="5":
        print("\n Los nombres de los usuarios ingresados son: ") 
        for i in lista_usuarios2:
            nombres = i ["nombre"]
            print(nombres)



    elif option=="6":
        option = False
        print("\n Goodbye!")
    elif option !="":
        print("\n Opción no válida, intenta otra vez") 

