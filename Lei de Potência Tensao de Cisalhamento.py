# Lei de Potência

import matplotlib.pyplot as plt
import numpy as np


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

def ViscPspl(Tcis,m1,n1):
    Visc1 = m1*(Tcis)**(n1-1)
    plt.plot(Tcis,Visc1,label="Pseudoplástico")
    plt.title("Vsicosidade x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Vsicosidade, (Pa.s)")
    plt.legend(loc="best")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.show()
    return Visc1

Tcis = np.linspace(0,1000,2000)
Tcisl = np.logspace(-1,6,2000)
n1 = 0.60
n2 = 1 
n3 = 1.2
m1 = 5000
m2 = 370
m3 = 100

TcisPspl(Tcis,m1,n1)
TcisNew(Tcis,m2,n2)
TcisDlt(Tcis,m3,n3)
TensaoCisalhamento3(Tcis,m1,m2,m3,n1,n2,n3)
TcisPspllog(Tcis,m1,n1)
TcisNewlog(Tcis,m2,n2)
TcisDltlog(Tcis,m3,n3)
TensaoCisalhamento3log(Tcisl,m1,m2,m3,n1,n2,n3)
ViscPspl(Tcis,m1,n1)