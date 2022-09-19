from datetime import datetime

from Classes import *

roles = ['Maestro', 'Estudiante']
dniTypes = ['cedula de ciudadania', 'tarjeta de identidad', 'cedula de extranjeria', 'pasaporte']
places = ['Coliseo', 'Salon', 'Biblioteca']
things = ['balon','libro', 'computador']

def validarFecha(dateAsString:str):
    format = "%Y-%m-%d"
    res = True
    try:
        res = bool(datetime.strptime(dateAsString, format))
    except ValueError:
        res = False
    return res

while (True):
    name = input("Hola, me gustaria saber ¿cual es tu nombre? \n")
    confirm = input("Su nombre es: " + name + ". Es correcto? \n 1. Si \n 2. No \n" )
    if (confirm == '1'):
        break
    else:
        print("Intente de nuevo.\n")

while (True):
    rolId = input("¿Que rol tienes? \n 1. Maestro \n 2. Estudiante \n")
    if (rolId in ["1","2"]):
        rol = roles[int(rolId)-1]
        confirm = input("Usted seleccionó: " + rol + ". Es correcto? \n 1. Si \n 2. No \n" )
        if (confirm == '1'):
            break
        else:
            print("Intente de nuevo.\n")
    else:
        print("Esta opción no existe, intente de nuevo.\n")

while(True):
    dniType = input("¿cual es tu tipo de documento? \n 1.cédula de ciudadanía. \n 2.tarejeta de identidad \n 3.cédula de extranjeria \n 4.pasaporte \n")
    if (dniType in ["1","2","3","4"]):
        dniType = dniTypes[int(dniType)-1]
        confirm = input("Usted seleccionó: " + dniType + ". Es correcto? \n 1. Si \n 2. No \n" )
        if (confirm == '1'):
            break
        else:
            print("Intente de nuevo.\n")
        break
    else:
        print("Esta opción no existe, intente de nuevo.\n")

while (True):
    dni = input("Ingrese su número de documento \n")
    confirm = input("Su documento es: " + dni + ". Es correcto? \n 1. Si \n 2. No \n" )
    if (confirm == '1'):
        break
    else:
        print("Intente de nuevo.\n")

while(True):
    doReservation = input("¿en que te puedo servir? ¿Deseas hacer una reserva? \n \n 1. Si \n 2. No \n" )
    if (doReservation == '1'):
        break
    elif (doReservation == '2'):
        input("Esta bien, muchas gracias por comunicarse con nosotros." )
        break
    else:
        print("Esta opción no existe, intente de nuevo.\n")

if (doReservation == "1"):
    while(True):
        placeId = input("Que lugar quieres reservar \n 1. coliseo \n 2.salon \n 3.biblioteca \n")
        if (placeId  in ["1","2","3"]):
            placeName = places[int(placeId)-1]
            confirm = input("Usted seleccionó: " + placeName + ". Es correcto? \n 1. Si \n 2. No \n" )
            if (confirm == '1'):
                break
            else:
                print("Intente de nuevo.\n")
        else:
            print("Esta opción no existe, intente de nuevo.\n")

    while (True):
        date = input("fecha de la reserva (YYYY-MM-DD) : \n")
        dateValidated = validarFecha(date)
        if (dateValidated == True):
            confirm = input("La fecha es: " + date + ". Es correcto? \n 1. Si \n 2. No \n" )
            if (confirm == '1'):
                break
            else:
                print("Intente de nuevo.\n")
        else:
            print("Fecha incorrecta, intente de nuevo.\n")

    while (True):
        needThing =input('¿Necesitas algun objeto? \n 1. Si \n 2. No \n ')
        if (needThing in ["1" ,"2"]):
            break
        else:
            print("Esta opción no existe, intente de nuevo.\n")        

    thingName = ""
    if (needThing == "1"):
        while (True):
            thingId = input("¿Qué objeto? \n 1. Balón \n 2. Libro \n 3. Computador\n ")
            if (thingId in ["1","2","3"]):
                thingName = things[int(thingId)-1]
                confirm = input("Usted seleccionó: " + thingName + ". Es correcto? \n 1. Si \n 2. No \n" )
                if (confirm == '1'):
                    break
                else: 
                    print("Intente de nuevo.\n")
            else:
                print("Esta opción no existe, intente de nuevo.\n")

user1 = User(dniType, dni, name, rol)
print(f"Usuario Creado: \nName: {name}\nRol: {rol}\ndni: {dniType} - {dni}\n")

if (doReservation == "1"):
    place = Place(placeName)
    thing = Thing(thingName)
    reservation = user1.bookReservation(place, date, thing)
    print(f"Reserva Creada: \nUsuario: {name}\nLugar: {placeName}\nFecha: {date}\nObjeto: {thingName}")

exit()