# Modelos Reológicos Fluidos não Newtonianos
# Lei de Potência (Funções)
# Tensão de Cisalhamento

import matplotlib.pyplot as plt
import numpy as np

# Dados

# 1 Lei de Potência

Tcis = np.linspace(0,1000,2000)
Tcisl = np.logspace(-1,6, 2000)
n1 = 0.6
n2 = 1 
n3 = 1.2
m1 = 5000
m2 = 370
m3 = 100

# 2 Carreau 

l = 100 # parâmetro de ajuste de curva
nc = 0.5  # coeficiente índice de comportamento dp fluxo (< 1)
Tcislc = np.logspace(-5,9, 1000) # Taxa de Cisalhamento
u0c = 100
uinfc = 0.01

# 3 Crossequation

K = 0.01  # parâmetro de ajuste de curva
nce = 0.8  # coeficiente índice de comportamento dp fluxo (< 1)
Tcislce = np.logspace(-5,9, 1000) # Taxa de Cisalhamento
u0ce = 1000
uinfce = 0.1

# 4 Ellis 

a = 3  # coeficiente índice de comportamento dp fluxo (< 1)
Tencislel = np.logspace(-4,6, 1000) # Tensão de Cisalhamento
t12 = 500 # Tensão de Cisalhamento (metade da vscsidade inicial)
u0el= 1000 # Viscosdade Inicial

# 5 Modelo Viscosidade dependente do ph, Tcis e Temperatura 

ph = np.linspace(1,7,1000)
Tcis = [10, 20, 40]
ph1 = [0.01,1,2,3,4,5,6,6.99]
Tcis1 = np.linspace(0,1000,2000)
p_hm = 5.47
u_m = 23.83
u_0 = 1000
a1 = 23.5
T = 300
T_0 = 300
nph = 0.5
alpha = 0.9

# 1 Lei de Potência

# 1.1 Gráfico da Tensão de Cisalhamento

def TcisPspl(Tcis,m1,n1):
    Tau1 = m1*Tcis**n1
    plt.plot(Tcis,Tau1,label="Pseudoplástico")
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Tau1

def TcisNew(Tcis,m2,n2):
    Tau2 = m2*Tcis**n2
    plt.plot(Tcis,Tau2,label="Newtoniano")
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Tau2

def TcisDlt(Tcis,m3,n3):
    Tau3 = m3*Tcis**n3
    plt.plot(Tcis,Tau3,label="Dilatante")
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Tau3

def TcisPspllog(Tcisl,m1,n1):
    Tau1l = m1*Tcisl**n1
    plt.loglog(Tcisl,Tau1l,label="Pseudoplástico")
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento (Log)")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.legend(loc="best")
    plt.xlim(1,)
    plt.ylim(0,)
    plt.show()
    return Tau1l

def TcisNewlog(Tcisl,m2,n2):
    Tau2l = m2*Tcisl**n2
    plt.loglog(Tcisl,Tau2l,label="Newtoniano")
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento (Log)")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Tau2l

def TcisDltlog(Tcisl,m3,n3):
    Tau3l = m3*Tcisl**n3
    plt.loglog(Tcisl,Tau3l,label="Dilatante")
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento (Log)")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Tau3l

TcisPspl(Tcis,m1,n1)
TcisNew(Tcis,m2,n2)
TcisDlt(Tcis,m3,n3)
TcisPspllog(Tcis,m1,n1)
TcisNewlog(Tcis,m2,n2)
TcisDltlog(Tcis,m3,n3)

# 1.2 Gráfico Tensão de Cisalhamento de 3 gráficos (Fluido Dilatante, Newtoniano e Pseudoplástico)

def TensaoCisalhamento3(Tcis,m1,m2,m3,n1,n2,n3):
    Tau1 = m1*Tcis**n1
    Tau2 = m2*Tcis**n2
    Tau3 = m3*Tcis**n3
    plt.plot(Tcis,Tau1,label="Pseudoplástico")
    plt.plot(Tcis,Tau2,label="Newtoniano")
    plt.plot(Tcis,Tau3,label="Dilatante")
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return (Tau1,Tau2,Tau3)

def TensaoCisalhamento3log(Tcisl,m1,m2,m3,n1,n2,n3):
    Tau1l = m1*Tcisl**n1
    Tau2l = m2*Tcisl**n2
    Tau3l = m3*Tcisl**n3
    plt.loglog(Tcisl,Tau1l,label="Pseudoplástico")
    plt.loglog(Tcisl,Tau2l,label="Newtoniano")
    plt.loglog(Tcisl,Tau3l,label="Dilatante")
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento (Log)")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return (Tau1l,Tau2l,Tau3l)

TensaoCisalhamento3(Tcis,m1,m2,m3,n1,n2,n3)
TensaoCisalhamento3log(Tcisl,m1,m2,m3,n1,n2,n3)

# 1.3 Gráfico Vicosidade 

def ViscPspl(Tcis,m1,n1):
    Visc1 = m1*(Tcis)**(n1-1)
    plt.plot(Tcis,Visc1,label="Pseudoplástico")
    plt.title("Viscodidade x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Visc1

ViscPspl(Tcis,m1,n1)

def ViscNew(Tcis,m2,n2):
    Visc2 = m2*(Tcis)**(n2-1)
    plt.plot(Tcis,Visc2,label="Newtoniano")
    plt.title("Viscodidade x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Visc2

ViscNew(Tcis,m2,n2)

def ViscDlt(Tcis,m3,n3):
    Visc3 = m3*(Tcis)**(n3-1)
    plt.plot(Tcis,Visc3,label="Dilatante")
    plt.title("Viscodidade x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Visc3

ViscDlt(Tcis,m3,n3)

def ViscPspl(Tcisl,m1,n1):
    Viscl1 = m1*(Tcisl)**(n1-1)
    plt.plot(Tcisl,Viscl1,label="Pseudoplástico")
    plt.title("Viscosidade x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Viscl1

ViscPspl(Tcisl,m1,n1)

def ViscNew(Tcisl,m2,n2):
    Viscl2 = m2*(Tcisl)**(n2-1)
    plt.plot(Tcisl,Viscl2,label="Newtoniano")
    plt.title("Viscosidade x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Viscl2

ViscNew(Tcisl,m2,n2)

def ViscDltlog(Tcisl,m3,n3):
    Viscl3 = m3*(Tcisl)**(n3-1)
    plt.loglog(Tcisl,Viscl3,label="Dilatante")
    plt.title("Viscosidade x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(1,)
    plt.ylim(0,)
    plt.show()
    return Viscl3

ViscDltlog(Tcisl,m3,n3)

# 1.4 Gráfico Viscosidade de 3 gráficos (Fluido Dilatante, Newtoniano e Pseudoplástico)

def Viscosidade3(Tcis,m1,m2,m3,n1,n2,n3):
    Visc1 = m1*Tcis**(n1-1)
    Visc2 = m2*Tcis**(n2-1)
    Visc3 = m3*Tcis**(n3-1)
    plt.plot(Tcis,Visc1,label="Pseudoplástico")
    plt.plot(Tcis,Visc2,label="Newtoniano")
    plt.plot(Tcis,Visc3,label="Dilatante")
    plt.title("Viscosidade x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return (Visc1,Visc2,Visc3)

def Viscosidade3log(Tcisl,m1,m2,m3,n1,n2,n3):
    Visc1l = m1*Tcisl**(n1-1)
    Visc2l = m2*Tcisl**(n2-1)
    Visc3l = m3*Tcisl**(n3-1)
    plt.loglog(Tcisl,Visc1l,label="Pseudoplástico")
    plt.loglog(Tcisl,Visc2l,label="Newtoniano")
    plt.loglog(Tcisl,Visc3l,label="Dilatante")
    plt.title("Viscosidade x Taxa de Cisalhamento (Log)")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(1,)
    plt.show()
    return (Visc1l,Visc2l,Visc3l)

Viscosidade3(Tcis,m1,m2,m3,n1,n2,n3)
Viscosidade3log(Tcisl,m1,m2,m3,n1,n2,n3)


# 2 Gráfico de Viscosidade x Taxa de Cisalhamento (Carreau)

def Carreau(Tcislc,u0c,uinfc,l,nc):
    Visc = uinfc+(u0c-uinfc)*(((1+(l*Tcislc)**2))**((nc-1)/2))
    plt.title("Viscosidade x Taxa de Cisalhamento (Log)")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)") 
    plt.loglog(Tcislc,Visc,label="Carreau")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Visc

Carreau(Tcislc,u0c,uinfc,l,nc)

# 3 Cross Equation
def Crossequation(Tcislce,u0ce,uinfce,K,n):
    Visc = uinfce+((u0ce-uinfce)*(1/(1+K*np.power(Tcislce,n))))
    plt.title("Viscosidade x Taxa de Cisalhamento (Log)")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Viscosidade, (Pa.s)") 
    plt.loglog(Tcislce,Visc,label="Crossequation")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Visc

Crossequation(Tcislce,u0ce,uinfce,K,nce)

# 4 Ellis 

def Ellis(a,Tencislel,t12,u0el):
    Visc = (u0el)/(1+((Tencislel/t12)**(a-1)))
    plt.title("Viscosidade x Tensão de Cisalhamento (Log)")
    plt.xlabel("Tensão de cisalhamento, (Pa)")
    plt.ylabel(" Viscosidade, (Pa.s)") 
    plt.loglog(Tencislel,Visc,label="Ellis")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Visc

Ellis(a,Tencislel,t12,u0el)

# 5 Modelo Viscosidade dependente do ph, Tcis e Temperatura 

# 5.1 Modelo Viscosidade dependente do ph, Tcis e Temperatura (ph Constante)

def Visc_Ph(ph,p_hm,u_m,u_0,a1,T,T_0,Tcis,nph,alpha):
 Tcis, ph = np.meshgrid(Tcis, ph)
 V_isc = (u_0*((Tcis)**(nph-1)))*(1-alpha*((T-T_0)/T_0))*(1+(u_m-1)*np.exp((-a1*(ph-p_hm)**2)/(ph*(7-ph)))) 
 plt.title("Viscosidade x ph (Taxa de Cisalhamento Constante)")
 plt.xlabel("Taxa de cisalhamento, (1/s)")
 plt.ylabel(" Viscosidade, (Pa.s)")
 label = ([10],[20],[40])
 plt.plot(ph,V_isc,label= label)
 plt.legend()
 plt.show()
 return V_isc

Visc_Ph(ph,p_hm,u_m,u_0,a1,T,T_0,Tcis,nph,alpha)

# 5.2 Modelo Viscosidade dependente do ph, Tcis e Temperatura (Tcis Constante)
def Visc_Ph1(ph1,p_hm,u_m,u_0,a1,T,T_0,Tcis1,nph,alpha):
 ph1, Tcis1 = np.meshgrid(ph1, Tcis1)
 V_isc1 = (u_0*((Tcis1)**(nph-1)))*(1-alpha*((T-T_0)/T_0))*(1+(u_m-1)*np.exp((-a1*(ph1-p_hm)**2)/(ph1*(7-ph1)))) 
 plt.title("Viscosidade x ph (ph Constante)")
 plt.xlabel("Taxa de cisalhamento, (1/s)")
 plt.ylabel(" Viscosidade, (Pa.s)")
 label1 = ([0.01],[1],[2],[3],[4],[5],[6],[6.99])
 plt.plot(Tcis1,V_isc1,label = label1)
 plt.legend()
 plt.show()
 return V_isc1

Visc_Ph1(ph1,p_hm,u_m,u_0,a1,T,T_0,Tcis1,nph,alpha)






