import os
import sys,time
import sqlite3

def nuevo():
    os.system("cls")
    nombre=input("digite el nombre del alumno")
    edad=input("digire la edad del alumno")
    dni=input("digite el dni del alumno")
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("insert into instituto (nombre,edad,dni) values ('"+nombre+"','"+edad+"','"+dni+"')")
    con.commit()
    con.close()

def menu():
    os.system("cls")
    print("Base de datos del Instituto del Sur")
    print("")
    print("1.- agregar articulo")
    print("2.- ver alumno")
    print("3.- modificar articulo")
    print("4.- iliminar articulo")
    print("5.- salir")
    while(1):
        try:
            print("ingrese una opcion")
            entrada=input()
            entrada=int(entrada)
            while(entrada<0 or entrada>5):
                print("ingrese correctamente la opcion")
                entrada=input()
                entrada=int(entrada)
            break
        except ValueError:
            print("ingrese correctamente una opcion valida")
    if (entrada==1):
        nuevo()
    elif(entrada==2):
        reporte()
    elif(entrada==3):
        modificar()
    elif(entrada==4):
        iliminar()
    elif(entrada==5):
        sys.exit()

def reporte():
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from instituto ")
    for instituto in cursor:
        print("")
        print("\t alumnos agregados")
        print("\t------------------------")
        print("\t nombre:"'\t'+str(instituto[1]))
        print("\t edad:"'\t'+str(instituto[2]))
        print("\t dni:"'\t'+str(instituto[3]))
        print("\t codigo:"'\t'+str(instituto[0]))
    con.commit()
    con.close()
    input()
    menu()
def modificar():
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from instituto ")
    for instituto in cursor:
        print("")
        print("\t alumnos agregados")
        print("\t------------------------")
        print("\t nombre:"'\t'+str(instituto[1]))
        print("\t edad:"'\t'+str(instituto[2]))
        print("\t dni:"'\t'+str(instituto[3]))
        print("\t codigo:"'\t'+str(instituto[0]))
    cod=input("digite el codigo del articulo que desea modificar")
    for intituto in cursor:
        if int(instituto[0])==int(cod):
            nombre=instituto[1]
            edad=instituto[2]
            dni=instituto[3]
            break
    nombre= input("Digite nuevo nombre o corrija" )
    edad=input("Digite nueva edad o corrija")
    dni= input("Digite nuevo dni o corrija" )
    sql = "UPDATE instituto set nombre ='"+nombre+"', edad='"+edad+"',dni='"+dni+"' where codigo = "+cod
    cursor.execute(sql)

    con.commit()
    con.close()
    print("")
    print("el archivo fue modificado exitoxamente-.......")
    input()
    menu()
def iliminar():
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from instituto ")
    for instituto in cursor:
        print("")
        print("\t alumnos agregados")
        print("\t------------------------")
        print("\t nombre:"'\t'+str(instituto[1]))
        print("\t edad:"'\t'+str(instituto[2]))
        print("\t dni:"'\t'+str(instituto[3]))
        print("\t codigo:"'\t'+str(instituto[0]))
    cod=input("digite el codigo del articulo que desea iliminar")
    sql="delete from instituto where codigo="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    print("")
    print("el archivo fue iliminado exitoxamente-.......")
    input()
    menu()

menu()
