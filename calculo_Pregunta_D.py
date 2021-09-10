
dominio_bajo=3.36
dominio_alto=10
usuario=int(input("Ingrese un numero de particiones: "))

distancia=dominio_alto-dominio_bajo
particiones=distancia/usuario
print("Numero de particiones")
print(particiones)

q=0
for i in range(usuario):
    if i!=usuario-1:
        x=particiones+dominio_bajo
        print("Intervalo")
        print(x)
        dominio_bajo=dominio_bajo+particiones
        print("SUma intervalo")
        print(dominio_bajo)

        funcion_grande=(-0.18*(x**2))+(2.42*x)-3.04
        print(funcion_grande)
        print("Esta es la funcion grande")
        funcion_chica=(0.15*(x**2))-(1.99*x)+8.06
        print(funcion_chica)
        print("Esta es la funcion chica")
        resta=funcion_grande-funcion_chica
        print(resta)
        print("Esta es la resta")
        y=resta*particiones
        print(y)
        print("area rectangulo")
        q=y+q
    else:
        x
        x_1=dominio_bajo
        print(x_1)
        print("Valor de dominio bajo")
        funcion_grande=(-0.18*(x**2))+(2.32*x)-3.04
        print("Funcion grande final")
        funcion_chica=(0.15*(x_1**2))-(1.99*x_1)+8.06
        print("Funcion chica final")
        resta=funcion_grande-funcion_chica
        y=resta*particiones
        q=y+q

print(q)
