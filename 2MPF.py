# Método do Ponto Fixo (MPF) #

import math
e = 2.71828

E = float(input("E = ").replace(",",".")) # O resultado da aproximação será o mais perto de "E"

def f(x): # Coloque a função f(x) depois de return
    ####################################

    return 
    # Exemplo: return x**7-x**4+2*(x**3)-4

    ####################################

def P(x): # Coloque a função iteração (isola o x) depois de return
    ####################################

    return 
    # Exemplo: return (x**4-2*x**3+4)**(1/7)

    ####################################

x = float(input("x0 = ").replace(",","."))
lista_x, lista_fx = [],[]

print(f"  ||   x   ||   f(x)  ||\n"," ||-------||---------||")
print(f"0 || {x:.8f} || {f(x):.8f} ||")

i=0
while abs(f(x))>E: #and (x >= a and x <= b)
    x=P(x)
    lista_x.append(x)
    f(x)
    lista_fx.append(f(x))

    i=i+1

for i in range(len(lista_x)):
    if i!=len(lista_x)-1:
        print(f"{i+1} || {lista_x[i]:.8f} || {lista_fx[i]:.8f} ||") 
    else:
        print(f"{i+1} || ({lista_x[i]:.8f}) || {lista_fx[i]:.8f} ||") 
print(f"solução aproximada = {lista_x[-1]} | (f(x) = {lista_fx[-1]})")
print()