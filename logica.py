import pytest


def problema1():
    numeros = [x for x in range(1,101)]
    resultado = []
    for i in range(len(numeros)):     
        if numeros[i]%3 == 0 and numeros[i]%5 ==0:
            print(numeros[i],"fizz buzz")
            resultado.append("fizz buzz")
            continue
        if numeros[i]%3 == 0:
            print(numeros[i],"fizz")
            resultado.append("fizz")
            continue
        if numeros[i]%5 == 0:
            print(numeros[i],"buzz")
            resultado.append("buzz")
            continue
        resultado.append(numeros[i])
    return resultado


def problema2(numero):
    if numero > 2:
        resultado = [0,1]
        for i in range(2,numero):
            resultado.append(resultado[i-2]+resultado[i-1])  
    elif numero ==1:
        resultado = [0,1]
    else:
        resultado = [0]
    print(resultado)
    return resultado



def problema3(frase):
    resultado = {}
    frase = frase.split(" ")
    for i in range(len(frase)):
        print(i,frase[i])
        if frase[i] in resultado:
            resultado[frase[i]] +=1
        else:
            resultado[frase[i]] = 1

    print(resultado)
    return resultado

#problema3("Hi how are things? How are you? Are you a developer? I am also a developer")
