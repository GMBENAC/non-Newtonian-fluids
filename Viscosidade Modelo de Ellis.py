#Viscosidade Modelo de Ellis


import numpy as np
import matplotlib.pyplot as plt

# Variáveis

alpha: int = 3  # coeficiente índice de comportamento dp fluxo (< 1)
t_yx = np.linspace(0.0001,1000) # Tensão de Cisalhamento
t_12 = 100 # Tensão de Cisalhamento (metade da vscsidade inicial)
u_0 = 1000 # Viscosdade Inicial
u_xy = (u_0)/(1+((t_yx/t_12)**(alpha-1)))# Viscosidade do Fluido 
plt.plot(t_yx,u_xy)
plt.xlabel("Tensão de Cisalhamento, (Pa)")
plt.ylabel("Viscosidade, (Pa.s)")
plt.title("Viscosidade x Tensão de Cisalhamento (Ellis)")
plt.legend(loc="best")
plt.show()


