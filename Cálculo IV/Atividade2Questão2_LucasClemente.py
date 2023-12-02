#Atividade 2 - Questão 2
#Lucas Silva Clemente

#para importar esta biblioteca faça os seguintes passos:
#instale o pip do python
#pip install numpy
import numpy as np

#para importar esta biblioteca faça os seguintes passos:
#instale o pip do python
#python -m pip install -U matplotlib
#ou
#py -m pip install -U matplotlib
#só isso deve bastar, mas caso encontre um erro com o Pillow, use o comando:
#pip install --only-binary Pillow Pillow
#tente instalar o matplotlib novamente
import matplotlib.pyplot as plt

#função que representa a equação diferencial de Mathieu: ((d^2)vetY)/dx^2 + (a - 2q*cos(2x))vetY = 0
#vetY: vetor [y, y']
def equacaoMathieu(x, vetY, a, q):

    dy_dx = vetY[1]
    d2y_dx2 = -(a - 2*q*np.cos(2*x))*vetY[0]
    return np.array([dy_dx, d2y_dx2])

#resolve a equação diferencial de Mathieu usando o método de Runge-Kutta de quarta ordem
#deltaX: intervalo de X
#y0: condição inicial para vetY(x)
#y1: condição inicial para vetY'(x)
#deltaP: intervalo entre os pontos do calculo da solução
def determinaMathieu(a, q, deltaX, y0, y1, deltaP):

    valoresX = np.arange(deltaX[0], deltaX[1] + deltaP, deltaP)
    valoresY = []

    y = np.array([y0, y1])

    #método de Runge-Kutta de quarta ordem
    #k1, k2, k3 e k4: coeficientes calculados em cada etapa
    for x in valoresX:
        valoresY.append(y[0])
        k1 = deltaP*equacaoMathieu(x, y, a, q)
        k2 = deltaP*equacaoMathieu(x + 0.5*deltaP, y + 0.5*k1, a, q)
        k3 = deltaP*equacaoMathieu(x + 0.5*deltaP, y + 0.5*k2, a, q)
        k4 = deltaP*equacaoMathieu(x + deltaP, y + k3, a, q)
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6.0

    return valoresX, np.array(valoresY)

def main():

    a = 3.0
    q = 0.5

    y0 = 0.8 #y(x) inicial
    y1 = 0.0 #y'(x) inicial

    deltaX = (0, 10 * np.pi)
    deltaP = 0.05

    valoresX, valoresY = determinaMathieu(a, q, deltaX, y0, y1, deltaP)

    #plota o gráfico das funções de Mathieu
    #irei anexar na pasta zipada um print de como o gráfico está sendo plotado
    #valores teste 1:
    #a = 2.0
    #q = 1.0
    #y0 = 1.0
    #y1 = 0.0
    #valores teste 2:
    #a = 3.0
    #q = 0.5
    #y0 = 0.8
    #y1 = 0.0
    plt.plot(valoresX, valoresY, label="Função de Mathieu")
    plt.title("Funções de Mathieu")
    plt.xlabel("X")
    plt.ylabel("[Y, Y']")
    plt.show()

if __name__ == "__main__":
    main()