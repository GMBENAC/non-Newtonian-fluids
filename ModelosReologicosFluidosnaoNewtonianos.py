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

#def Carreau(Tcis,u_0,u_inf,Lambda,n):
    #V_isc = u_inf+(u_0-u_inf)*np.power(1+np.power(Lambda*Tcis,2),(n-1)/2)
    #plt.title("Viscosidade x Taxa de Cisalhamento (Ph Constante)")
    #plt.xlabel("Taxa de cisalhamento, (1/s)")
    #plt.ylabel(" Viscosidade, (Pa.s)") 
    #return V_isc

# Cross Equation
#def Crossequation(Tcis,u_0,u_inf,K,n):
    #V_isc = u_inf+((u_0-u_inf)*(1/(1+K*np.power(Tcis,n))))
    #plt.title("Viscosidade x Taxa de Cisalhamento")
    #plt.xlabel("Taxa de cisalhamento, (1/s)")
    #plt.ylabel(" Viscosidade, (Pa.s)") 
    #return V_isc


# Modelo Viscosidade dependente do ph, Tcis e Temperatura (ph Constante)
#def Visc_Ph(ph,p_hm,u_m,u_0,a,T,T_0,Tcis,n,alpha):
 #ph, Tcis = np.meshgrid(ph, Tcis)
 #V_isc = (u_0*((Tcis)**(n-1)))*((1-alpha)*((T-T_0)/T_0))*(1+(u_m-1)*np.exp((-a*(ph-p_hm)**2)/(ph*(7-ph)))) 
 #plt.title("Viscosidade x Taxa de Cisalhamento (Ph Constante)")
 #plt.xlabel("Taxa de cisalhamento, (1/s)")
 #plt.ylabel(" Viscosidade, (Pa.s)")    
 #return V_isc

# Modelo Viscosidade dependente do ph, Tcis e Temperatura (Tcis Constante)
def Visc_Ph(ph,p_hm,u_m,u_0,a,T,T_0,Tcis,n,alpha):
 Tcis, ph = np.meshgrid(Tcis, ph)
 V_isc = (u_0*((Tcis)**(n-1)))*((1-alpha)*((T-T_0)/T_0))*(1+(u_m-1)*np.exp((-a*(ph-p_hm)**2)/(ph*(7-ph)))) 
 plt.title("Viscosidade x ph (Taxa de Cisalhamento Constante)")
 plt.xlabel("Taxa de cisalhamento, (1/s)")
 plt.ylabel(" Viscosidade, (Pa.s)")
 return V_isc

ph = np.linspace(1,7,1000)
Tcis = [10, 20, 40]

#TensaoCisalhamento(1,0.5)
V_isc=Visc_Ph(ph,5.47,23.83,1000,23.5,300,150,Tcis,1.2,0.9)
plt.plot(ph,V_isc)
plt.show()