nota = int(input("decime tu nota del examen"))

while (nota > 10 and nota <= 0):
    print("Como?")
    nota = int(input("ingrese su nota"))

if (nota >= 7 and nota <= 10):
    print("estas aprovado, mira vos che")
elif(nota >= 1 and nota <7):
    print("estas promocionado!")
else:
    print("ta desaprovado pe causa")
