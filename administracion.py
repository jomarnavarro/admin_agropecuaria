datos = []

menu_principal = """

Elija alguna de las siguientes opciones en el programa administrativo.

Opciòn 1 > Administraciones
Opciòn 2 > Entrega de cupos
Opciòn 3 > Recepciòn
Opciòn 4 > Registrar calidad
Opciòn 5 > Registrar peso bruto
Opciòn 6 > Registrar descarga
Opciòn 7 > Registrar tara
Opciòn 8 > Reportes
Opciòn 0 > Fin del programa

INGRESAR UNA OPCIÒN:  
"""

menu_opcion_1 = """
"""

def imprimir_menu_principal():
    return int(input(menu_principal))

print("BIENVENIDO")


opcion_menu_ppal = imprimir_menu_principal()
while opcion_menu_ppal != 0:

    if opcion_menu_ppal == 1:
        opcion_menu_admin =int(input
            ("\nOpciònes de administraciòn\n\n 1 > Titulares\n 2 > Productos\n 3 > Rubros\n 4 > Rubros x Productos\n 5 > Silos\n 6 > Sucursales\n 7 > Producto por titular\n 8 > Volver al menù principal\n\n INGRESAR UNA OPCIÒN: "))
        if opcion_menu_admin == 1:
            color =str(input
                ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            if color == 'A':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'B':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'C':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'M':
                print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'V':
                opcion_menu_ppal
            else:
                opcion_menu_ppal
            if color == 'F':
                print("\n\nElija alguna de las siguientes opciones en el programa administrativo")
                opcion_menu_ppal =int(input(
                                                 ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN:  ")))
            else:
                opcion_menu_ppal

        if opcion_menu_admin == 2:
            color =str(input
                ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            if color == 'A':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'B':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'C':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'M':
                print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'V':
                opcion_menu_ppal
            else:
                opcion_menu_ppal
            if color == 'F':
                print("\n\nElija alguna de las siguientes opciones en el programa administrativo")
                opcion_menu_ppal =int(input(
                                                 ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN:  ")))
            else:
                opcion_menu_ppal

        
        if opcion_menu_admin == 3:
            color =str(input
                ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            if color == 'A':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'B':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'C':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'M':
                print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'V':
                opcion_menu_ppal
            else:
                opcion_menu_ppal
            if color == 'F':
                print("\n\nElija alguna de las siguientes opciones en el programa administrativo")
                opcion_menu_ppal =int(input(
                                                 ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN:  ")))
            else:
                opcion_menu_ppal
        
        if opcion_menu_admin == 4:
            color =str(input
                ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            if color == 'A':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'B':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'C':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'M':
                print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'V':
                opcion_menu_ppal
            else:
                opcion_menu_ppal
            if color == 'F':
                print("\n\nElija alguna de las siguientes opciones en el programa administrativo")
                opcion_menu_ppal =int(input(
                                                 ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN:  ")))
            else:
                opcion_menu_ppal



        if opcion_menu_admin == 5:
           color =str(input
                ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
           if color == 'A':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
           else:
                opcion_menu_ppal
           if color == 'B':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
           else:
                opcion_menu_ppal
           if color == 'C':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
           else:
                opcion_menu_ppal
           if color == 'M':
                print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
           else:
                opcion_menu_ppal
           if color == 'V':
                opcion_menu_ppal
           else:
                opcion_menu_ppal
           if color == 'F':
                print("\n\nElija alguna de las siguientes opciones en el programa administrativo")
                opcion_menu_ppal =int(input(
                                                 ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN:  ")))
           else:
                opcion_menu_ppal
          


        if opcion_menu_admin == 6:
            color =str(input
                ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            if color == 'A':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'B':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'C':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'M':
                print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'V':
                opcion_menu_ppal
            else:
                opcion_menu_ppal
            if color == 'F':
                print("\n\nElija alguna de las siguientes opciones en el programa administrativo")
                opcion_menu_ppal =int(input(
                                                 ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN:  ")))
            else:
                opcion_menu_ppal
          

        if opcion_menu_admin == 7:
            color =str(input
                ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            if color == 'A':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'B':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'C':
                print("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'M':
                print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
                color =str(input
                    ("\n A > Alta\n B > Baja \n C > Consulta \n M > Modificaciòn \n V > Volver al menù anterior\n F > VOLVER AL MENÙ PRINCIPAL\n\n INGRESAR UNA OPCIÒN: "))
            else:
                opcion_menu_ppal
            if color == 'V':
                opcion_menu_ppal
            else:
                opcion_menu_ppal
            if color == 'F':
                print("\n\nElija alguna de las siguientes opciones en el programa administrativo")
                opcion_menu_ppal =int(input(
                                                 ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN:  ")))
            else:
                opcion_menu_ppal
           


        
        if opcion_menu_admin == 8:
            print("\n\nElija alguna de las siguientes opciones en el programa administrativo")
            opcion_menu_ppal =int(input(
                                             ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN:  ")))
    
    
    if opcion_menu_ppal == 2:
        print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
        print("\n\nElija alguna de las siguientes opciones en el programa administrativo")

        opcion_menu_ppal =int(input(
                                         ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN: ")))
    
   
    if opcion_menu_ppal == 3:
        patente =(int(input("INGRESAR NÙMERO DE PATENTE: ")))
        tipo_producto =(str(input("INGRESAR TIPO DE PRODUCTO: ")))
        peso_bruto =(float(input("INGRESAR PESO BRUTO: ")))
        tara =(float(input("INGRESAR TARA: ")))
        print("\nDATOS GUARDADOS CORRECTAMENTE EN REPORTES\n")
        data_camion = {
            "patente": patente,
            "tipo_producto": tipo_producto,
            "peso_bruto": peso_bruto,
            "tara": tara
        }

        datos.append(data_camion)
        print(datos)
        opcion_menu_ppal = imprimir_menu_principal()

        # while patente >= 0:
        #     patente + 1
        # print("camiones: ", patente)

    
        
    if opcion_menu_ppal == 4:
        print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
        print("\n\nElija alguna de las siguientes opciones en el programa administrativo")

        opcion_menu_ppal =int(input(
                                         ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN: ")))

    if opcion_menu_ppal == 5:
        print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
        print("\n\nElija alguna de las siguientes opciones en el programa administrativo")

        opcion_menu_ppal =int(input(
                                         ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN: ")))

    if opcion_menu_ppal == 6:
        print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
        print("\n\nElija alguna de las siguientes opciones en el programa administrativo")

        opcion_menu_ppal =int(input(
                                         ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n INGRESAR UNA OPCIÒN: ")))
    
    if opcion_menu_ppal == 7:
        print ("ESTA FUNCIONALIDAD ESTA EN CONSTRUCCIÒN")
        print("\n\nElija alguna de las siguientes opciones en el programa administrativo")

        opcion_menu_ppal =int(input(
                                         ("\n Opciòn 1 > Administraciones\n Opciòn 2 > Entrega de cupos\n Opciòn 3 > Recepciòn\n Opciòn 4 > Registrar calidad\n Opciòn 5 > Registrar peso bruto\n Opciòn 6 > Registrar descarga\n Opciòn 7 > Registrar tara\n Opciòn 8 > Reportes\n Opciòn 0 > Fin del programa\n\n  INGRESAR UNA OPCIÒN: ")))

    if opcion_menu_ppal == 8:
        cantidad_camiones = len(datos)
        cantidad_camiones_soja = len([x for x in datos if tipo_producto == 'soja'])
        print("BIENVENIDOS AL REPORTE DEL DIA")
        print("- Cantidad total de camiones que ingresaron: " ,cantidad_camiones)
        print("- Cantidad total de camiones de soja: " ,cantidad_camiones_soja)
        print("- Cantidad total de camiones de maiz: " , cantidad_camiones)
        print("- Peso neto total de soja: " , cantidad_camiones)
        print("- Peso neto total de maiz: " , cantidad_camiones)
        print("- Promedio del peso neto de soja por camión: " , cantidad_camiones)
        print("- Promedio del peso neto de maíz camión: " , cantidad_camiones)
        print("- Patente del camión de soja que mayor cantidad de soja descargó: " , cantidad_camiones)
        print("- Patente del camión de maíz que menor cantidad de maíz descargó: " , cantidad_camiones)
        print("- Patentes ingresadas: " , cantidad_camiones)
        print ("\nsaludos exelente dia laboral\n")

    opcion_menu_ppal = imprimir_menu_principal()
