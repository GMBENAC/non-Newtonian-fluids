# Viscosidade Cross Equation

# Modelo Reológico Lei de Potência Vicosidade

import numpy as np
import matplotlib.pyplot as plt

# Variáveis

K :float = 0.01  # parâmetro de ajuste de curva
n: int = 0.8  # coeficiente índice de comportamento dp fluxo (< 1)
Tcis = np.logspace(-5,5,1000) # Taxa de Cisalhamento
u_0 = 1000
u_inf = 0.1


def Crossequation(Tcis,u_0,u_inf,K,n):
    Visc = u_inf+((u_0-u_inf)/(1+K*(Tcis)**n))
    plt.xscale('log')
    plt.xlabel("Log Taxa de Cisalhamento, ($s^{-1}$)")
    plt.ylabel("Log Viscosidade, (Pa.s)")
    plt.title("Viscosidade x Taxa de Cisalhamento (Cross Equation)")
    plt.loglog(Tcis,Visc)
    plt.show()

    return Visc

Crossequation(Tcis,u_0,u_inf,K,n)
