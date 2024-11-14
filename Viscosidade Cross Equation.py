# Viscosidade Cross Equation

# Modelo Reológico Lei de Potência Vicosidade

import numpy as np
import matplotlib.pyplot as plt

# Variáveis

K :float = 0.01  # parâmetro de ajuste de curva
n: int = 0.8  # coeficiente índice de comportamento dp fluxo (< 1)
Y_xy = np.linspace(-1000,1000) # Taxa de Cisalhamento
u_0 = 1000
u_inf = 0.1
u_xy = u_inf+((u_0-u_inf)*(1/(1+K*(Y_xy)**n)))# Viscosidade do Fluido 
plt.plot(Y_xy,u_xy)
plt.xscale('log')
plt.xlabel("Log Taxa de Cisalhamento, ($s^{-1}$)")
plt.ylabel("Log Viscosidade, (Pa.s)")
plt.title("Viscosidade x Taxa de Cisalhamento (Cross Equation)")
plt.legend(loc="best")
plt.show()


