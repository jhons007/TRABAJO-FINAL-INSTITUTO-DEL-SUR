# TRABAJO-FINAL-INSTITUTO-DEL-SUR
TRABAJO FINAL INSTITUTO DEL SUR
import sqlite3
import os
import sys
def nuevo():
    nombre = input("ingrese su nombre ")
    edad = input("ingrese su edad ")
    dni = input("ingrese su DNI ")
    con = sqlite3.connect('tienda.s3db')
    cursor = con.cursor()
    cursor.execute("insert into cursos (nombre,edad,dni) values ('"+nombre+"','"+edad+"','"+dni+"')")
    con.commit()
    input("operacion completada")
    con.close()
def modificar():
    persona=[]
    con = sqlite3.connect('tienda.s3db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM cursos')
    print("personas agregados")
    print("\t <codigo> \t <nombre> \t <edad> \ <dni> ")
    print("---------------------------------------------------------")
    for persona in cursor:
        cursos.append(persona)
        nom =    '\t '+str(persona[0])+ '\t     '+persona[1]+'\t      '+persona[2]+ '\t     '+persona[3]
        print(nom)
    cod=input("digite el codigo")
    encontrado =False
    for persona in cursos:
        if int(persona[0]) ==int(cod):
            nombre=persona[1]
            edad=persona[2]
            dni=persona[3]
            encontrado == True
            break
        else:
            input("digite un opcion porfavor..")
            os.system("clear")
            modificar()
    nombre=input("digite el nuevo nombre de "+nombre+":")
    edad=input("digite el nuevo nombre de "+edad+":")
    dni=input("digite el nuevo nombre de "+dni+":")

    sql="update cursos set nombre-'"+nombre+"',edad-'"+edad+"',dni-'"+dni+"' where cod-"+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    print("modificado......<->")
    input()

def iliminar():
    con = sqlite3.connect('tienda.s3db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM cursos')
    print("personas agregados")
    print("\t <codigo> \t <nombre> \t <edad> \ <dni> ")
    print("-------------------------------------------------")
    for persona in cursor:
        cursos.append(persona)
        nom =    '\t '+str(persona[0])+ '\t     '+persona[1]+'\t      '+persona[2]+ '\t     '+persona[3]
        print(nom)
    cod=input("digite el codigo")
    if cod==True:
        return True
    else:
        input("codigo incorrecto")
        iliminar()
    sql="delete persona where cod-"+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    print("iliminado......<->")
    input()




def indice():
    print("1.-agregar nombre del alumno ")
    print("2.-modificar nombre del alumno")
    print("3.-iliminar nombre")
    print("4.-salir")
    print("")
    rvl=input("Digite una opcion")
    if rvl=="1":
        nuevo()
    elif rvl=="2":
        modificar()
    elif rvl=="3":
        iliminar()
    elif rvl=="4":
        input("este program se esta cerrndo ...")
        sys.exit()
    else:
        input("ingrese una opcion valida")
        indice()
indice()
