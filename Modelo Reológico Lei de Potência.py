# Modelo Reológico Lei de Potência ou modelo Ostwald de Waele

import numpy as np
import matplotlib.pyplot as plt

# Variáveis

m_1 :float = 3800  # coeficiente de consistência do fluido
m_2: float = 1000 # coeficiente de consistência do fluido
m_3: float = 15000 # coeficiente de consistência do fluido
n_1: int = 1  # coeficiente índice de comportamento dp fluxo
n_2: float = 1.2  # coeficiente índice de comportamento dp fluxo
n_3: int = 0.6 # coeficiente índice de comportamento dp fluxo
Y_xy = np.linspace(0, 10000, 50) # Taxa de Cisalhamento
t_xy1 = m_1*(Y_xy)**n_1 # Tensão de Cisalhamento Fluido Newtoniano
t_xy2 = m_2*(Y_xy)**n_2 # Tensão de Cisalhamento Fluido Não-Newtoniano Dilatante
t_xy3 = m_3*(Y_xy)**n_3 # Tensão de Cisalhamento Fluido Não-Newtoniano Pseudoplástico

plt.plot(Y_xy,t_xy1, label="Newtoniano")
plt.plot(Y_xy,t_xy2, label="Dilatante")
plt.plot(Y_xy,t_xy3, label="Pseudoplástico")
plt.xlabel("Taxa de Cisalhamento,"r'$\gamma$')
plt.ylabel("Tensão de Cisalhamento,"r'$\tau$')
plt.title("Tensão x Taxa de Cisalhamento (Lei de Potência)")
plt.legend(loc="best")
plt.show()

plt.loglog(Y_xy,t_xy1, label="Newtoniano")
plt.loglog(Y_xy,t_xy2, label="Dilatante")
plt.loglog(Y_xy,t_xy3, label="Pseudoplástico")
plt.xlabel("Taxa de Cisalhamento,"r'$\gamma$')
plt.ylabel("Tensão de Cisalhamento,"r'$\tau$')
plt.title("Tensão x Taxa de Cisalhamento (Lei de Potência)")
plt.legend(loc="best")
plt.show()


