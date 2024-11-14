# Modelo Reológico Lei de Potência Vicosidade

import numpy as np
import matplotlib.pyplot as plt

# Variáveis

m_1 :float = 500  # coeficiente de consistência do fluido
m_2: float = 500 # coeficiente de consistência do fluido
m_3: float = 500 # coeficiente de consistência do fluido
n_1: int = 1  # coeficiente índice de comportamento dp fluxo
n_2: int = 1.1  # coeficiente índice de comportamento dp fluxo
n_3: int = 0.9 # coeficiente índice de comportamento dp fluxo
Y_xy = np.linspace(0.001,500,1000) # Taxa de Cisalhamento
u_xy1 = m_1*(Y_xy)**(n_1-1) # Viscosidade Fluido Newtoniano
u_xy2 = m_2*(Y_xy)**(n_2-1) # Viscosidade Fluido Não-Newtoniano Dilatante
u_xy3 = m_3*(Y_xy)**(n_3-1) # Viscosidade Fluido Não-Newtoniano Pseudoplástico

plt.plot(Y_xy,u_xy1, label="Newtoniano")
plt.plot(Y_xy,u_xy2, label="Dilatante")
plt.plot(Y_xy,u_xy3, label="Pseudoplástico")
plt.xlabel("Taxa de Cisalhamento, ($s^{-1}$)")
plt.ylabel("Viscosidade, (Pa.s)")
plt.title("Viscosidade x Taxa de Cisalhamento (Lei de Potência)")
plt.legend(loc="best")
plt.show()


