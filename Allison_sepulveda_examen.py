import random 
import statistics
try:
    trabajadores = ["Juan perez", "Maria Garcia", "Carlos lopez", "Ana martinez", "Pedro rodriguez", "Laura hermandez", "Miguel Sanchez", "Isabel Gomez", "Francisco diaz", "Elena Fernandez"]

    nom_valores={}

    #Asignación aleatoria 
    def asignacion_aleatoria():
            for nombres in trabajadores:
                sueldo_aleatorio=random.randint(800000,2000000)
                nom_valores.update({nombres:sueldo_aleatorio})
            print(nom_valores)
except TypeError:
    print("Error tipo de datos")
except SyntaxError:
     print("ERROR DE Syntaxis")
except ValueError:
     print("ERROR VALOR")


    #Clacificación por rango 
try:
        #RANGO MENOR
    def rango_menor():
            sueldos=0
            for nombres, sueldo_aleatorio  in nom_valores.items():
                if sueldo_aleatorio <800000:
                    print("MENOR A 800000")
                    print("\t\tNOMBRE EMPLEADOR","\t\t SUELDOS")
                    print("\t\t",nombres,"\t\t",sueldo_aleatorio)
                pass


            for nombres, sueldo_aleatorio in nom_valores.items():
                if sueldo_aleatorio >=800000:
                    print("RANGO MAYOR A 8000000 ")
                    print("\t\tNOMBRE EMPLEADOR","\t\t SUELDOS")
                    print("\t\t",nombres,"\t\t",sueldo_aleatorio)
                pass

            for nombres, sueldo_aleatorio in nom_valores.items():
                if sueldo_aleatorio >2000000:
                        print("\t\tNOMBRE EMPLEADOR","\t\t SUELDOS")
                        print("RANGO MAYOR A 2000000")
                        print("\t\t",nombres,"\t\t",sueldo_aleatorio)
                pass
            
        #Estadistcas

    def estadisticas ():
            #PARA SACAR EL PROMEDIO
            promedio=0
            for sueldo_aleatorio in nom_valores.values():
                promedio += sueldo_aleatorio
            print("\t\t\t\tEL PROMEDIO ES DE:", promedio/10)
            print("\t\t\t\tDESVIACIÓN ESTANDAR:", statistics.mean(nom_valores.values()))
except TypeError:
    print("Error tipo de datos")
except SyntaxError:
     print("ERROR DE Syntaxis")
except ValueError:
     print("ERROR VALOR")

try:
    def orden():
            for sueldo_aleatorio in nom_valores.values():
                if sueldo_aleatorio==max(nom_valores.values()):
                    print("\t\t\t\tNUMERO MAXIMO ES DE:", sueldo_aleatorio)
            for sueldo_aleatorio in nom_valores.values():
                if sueldo_aleatorio==min(nom_valores.values()):
                    print("\t\t\t\tNUMERO MINIMO ES DE:", sueldo_aleatorio)
                    print(sueldo_aleatorio)
except TypeError:
    print("Error tipo de datos")
except SyntaxError:
     print("ERROR DE Syntaxis")
except ValueError:
     print("ERROR VALOR")

 
try:   #REPORTE DE SUELDOS
    def descuentos():
            print("\t\tNOMBRE EMPLEADOR","\t\tSUELDO BASE","\t\tAFP", "\tDESCUENTO SALUD","LOQUIDO")
            for nombres, sueldo_aleatorio in nom_valores.items():
                afp= round(sueldo_aleatorio*0.1,2)
                salud=round(sueldo_aleatorio *0.07,2)
                liquido=round(sueldo_aleatorio - afp -salud, 2)
                print("\t\t", nombres,"\t\t\t", sueldo_aleatorio)
                print("\t\t\t\t\t\t\t","\t",afp,"\t\t", "\t",salud,"\t\t", liquido)
except TypeError:
    print("Error tipo de datos")
except SyntaxError:
     print("ERROR DE Syntaxis")
except ValueError:
     print("ERROR VALOR")

        
    
opcion=0

try:

    while True:
            print("1)ASIGNAR NUMERO ALAZAR")
            print("2)CLASIFICAR SUELDOS")
            print("3)VER ESTADISTICAS")
            print("4)REPORTE DE SUELDOS")
            print("5) SALIR")
            opcion=int(input("Ingrese la opcion deseada: "))

            if opcion==1: 
                    print("Ha entrado al menu de asignar sueldos aleatorios")
                    print("\t\tLISTA TRABAJADORES JUNTO CON SU SUELDO")
                    asignacion_aleatoria()

            if opcion==2:
                    print("Ha entrado a la opcion clasificar sueldos")
                    print("\t\t\tSueldos menores a $800.000\t\t\t")
                    rango_menor()

            if opcion==3: 
                print("ingreso a la opcion ver estadisticas")
                orden()
                estadisticas()
            if opcion==4:
                descuentos()

            if opcion==5:       
                print("SALIR")
                pass
            

except TypeError:
    print("Error tipo de datos")
except SyntaxError:
     print("ERROR DE Syntaxis")

except ValueError:
    print("ERROR VALOR")

finally:
     print ("Finalizando programa, Desarrollado por Allison sepulveda")
     print("RUT: 2136768743")
