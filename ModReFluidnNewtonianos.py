# Modelos Reológicos Fluidos não Newtonianos
# Lei de Potência (Funções)
# Tensão de Cisalhamento

import matplotlib.pyplot as plt
import numpy as np

# Lei de Potência

# def TensaoCisalhamento(m,n):
    #Tcis = np.linspace(0,1000,200)
    #Tau = m*Tcis**n
    #plt.plot(Tcis,Tau)
    #plt.show()
   # return Tau


# def Viscosidade(m,n):
    #Tcis = np.linspace(0,1000,200)
    #V_isc = m*Tcis**(n-1)
    #plt.plot(Tcis,V_isc)
    #plt.show()
    #return V_isc

# Carreau
def Viscosidadec(u_0,u_inf,Lambda,n):
    Tcis = np.logspace(-5,9,1000)
    V_isc = u_inf+(u_0-u_inf)*(1+(Lambda*Tcis)**2)**(n-1)/2
    plt.loglog(Tcis,V_isc)
    plt.show()
    return V_isc





#TensaoCisalhamento(1,0.5)
Viscosidadec(100,0.001,100,0.5)
