# Modelos Reológicos Fluidos não Newtonianos
# Lei de Potência (Funções)
# Tensão de Cisalhamento

import matplotlib.pyplot as plt
import numpy as np

# Lei de Potência

def TensaoCisalhamento(m,n):
    Tcis = np.linspace(0,1000,200)
    Tau = m*Tcis**n
    plt.plot(Tcis,Tau)
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.show()
    return Tau


def TensaoCisalhamentolog(m,n):
    Tcis = np.linspace(0.001,1000,200)
    Tau = m*Tcis**n
    plt.loglog(Tcis,Tau)
    plt.title("Tensão de Cisalhamento x Taxa de Cisalhamento")
    plt.xlabel("Taxa de cisalhamento, (1/s)")
    plt.ylabel(" Tensão de Cisalhamento, (Pa)")
    plt.show()
    return Tau

TensaoCisalhamento(0.8,1.2)
TensaoCisalhamentolog(0.8,1.2)