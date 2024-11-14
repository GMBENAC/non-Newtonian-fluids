# Viscosidade Lei de Carreau

# Modelo Reológico Lei de Potência Vicosidade

import numpy as np
import matplotlib.pyplot as plt

# Variáveis

l :float = 100 # parâmetro de ajuste de curva
n: int = 0.5  # coeficiente índice de comportamento dp fluxo (< 1)
Tcis = np.logspace(-5,9, 1000) # Taxa de Cisalhamento
u_0 = 100
u_inf = 0.01

def Visc(u_0,u_inf,Tcis,n,l):
    Visc = u_inf+(u_0-u_inf)*(((1+(l*Tcis)**2))**((n-1)/2)) # Viscosidade do Fluido 
    plt.loglog(Tcis,Visc)
    plt.xlabel("Log Taxa de Cisalhamento, ($s^{-1}$)")
    plt.ylabel("Log Viscosidade, (Pa.s)")
    plt.title("Viscosidade x Taxa de Cisalhamento (Lei de Carreau)")
    plt.legend(loc="best")
    plt.show()

    return Visc


Visc(u_0,u_inf,Tcis,n,l)