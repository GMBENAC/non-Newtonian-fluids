# Modelo Reológico dependente do ph

import numpy as np
import matplotlib.pyplot as plt
import math as m

# Variáveis

u_m1 :float = 23.83 # É o incremento máximo na viscosidade em relação a base. 
u_m2 :float = 18 # É o incremento máximo na viscosidade em relação a base. 
u_m3 :float = 15 # É o incremento máximo na viscosidade em relação a base. 
u_01: float = 1000 # É a viscosidade na base (ph = 0 0u ph = 7).
u_02: float = 1000 # É a viscosidade na base (ph = 0 0u ph = 7).
u_03: float = 1000 # É a viscosidade na base (ph = 0 0u ph = 7).
ph_m: float = 5.47 # é o valor do pH da viscosidade máxima.
a : float = 23.5  # coeficiente que é inversamente proporcional ao range de ph onde ocorre o pico de viscosidade.
ph: float = np.linspace(0.01,6.99, 200) # Potencial Hidrogeniônico.
u_ph1: float = u_01*(1+(u_m1-1)*np.exp((-a*(ph-ph_m)**2)/(ph*(7-ph)))) # Viscosidade em relação ao ph.
u_ph2: float = u_02*(1+(u_m2-1)*np.exp((-a*(ph-ph_m)**2)/(ph*(7-ph)))) # Viscosidade em relação ao ph.
u_ph3: float = u_03*(1+(u_m3-1)*np.exp((-a*(ph-ph_m)**2)/(ph*(7-ph)))) # Viscosidade em relação ao ph.

plt.plot(ph,u_ph1, label='$\dot{\gamma}=$10 $s^{-1}$')
plt.plot(ph,u_ph2, label='$\dot{\gamma}=$20 $s^{-1}$')
plt.plot(ph,u_ph3, label='$\dot{\gamma}=$40 $s^{-1}$')


plt.xlabel("pH")
plt.ylabel("Viscosidade Aparente (Cp)")
plt.title("Viscosidade Aparente x pH")
plt.legend(loc="best")
plt.show()


