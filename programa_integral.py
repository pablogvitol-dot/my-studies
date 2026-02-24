# programa para o cálculo de integrais

# OTIMIZAÇÕES POSSÍVEIS:
# 1. aumentar  n
# 2. trabalhar com decimal, ao invés de float
# 3. fazer sum += f(ci + delta/2), ou seja, pegar o ponto médio do retângulo
#              += (f(ci) + f(ci+delta))/2

from math import *

def gera_f(f_str):
    def f(x):
        return eval(f_str)
    return f
def integral_riemann(a, b, f, n = 1000):
    soma = 0
    delta = (b - a)/n
    for i in range(n):
        m = 100
        lista = [a + i*delta + k*delta/m for k in range(m)]
        soma += (sum(map(f,lista)))/m
    return soma * delta
def der(x, f, n = 10):
    h = pow(10, -n)
    delta_f = f(x + h) - f(x)
    return delta_f/h

f = gera_f(input('qual a funcao, em x? '))
match input('qual a operação, derivada ou integral? '):
    case 'integral':
        b = float(input('qual o limite superior? '))
        a = float(input('e o inferior? '))
        
        res = integral_riemann(a, b, f)
        print(f"o resultado da integral é: {res}")
    case 'derivada':
        x0 = float(input('vai derivar f em qual x? '))
        res = der(x0, f)
        print(f'o resultado é: {res}')

