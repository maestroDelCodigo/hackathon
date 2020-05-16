edad =input("Introduce tu edad: ")
edad= int(edad)

if edad < 4:
    print ("El precio de la entrada es 0 euros")
elif edad >= 4 and edad <= 18:
    print("El precio son 5 euros")
else:
    print("El precio son 10 euros")
    