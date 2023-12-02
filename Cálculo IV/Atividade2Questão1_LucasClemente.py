#Atividade 2 - Questão 1
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

#função que representa a equação diferencial do pêndulo
#vetEestado: vetor na forma [θ, ω], sendo θ o ângulo e ω a velocidade angular
#grav: aceleração da gravidade (m/s^2)
#compr: comprimento do pêndulo (m)
def pendulo(vetEstado, grav, compr):
    
    theta, omega = vetEstado
    dtTheta = omega #dθ/dt
    dtOmega = -(grav / compr) * np.sin(theta) #(d^2)θ/dt^2 = - (g/l)*sen(θ) = dω/dt
    return np.array([dtTheta, dtOmega])

#resolve a equação diferencial, para isso usaremos o método de euler
#não que ele seja o mais adequado, mas parecia relativamente simples de implementar
#talvez não seja o método mais preciso, mas deve dar uma boa aproximação
#initTheta: ângulo inicial (rad)
#initOmega: velocidade angular inicial (rad/s)
#tempo: tempo da simulação (s)
#deltaT: tamanho da variação de tempo a ser utilizada no método de Euler (s)
def determinaPendulo(grav, compr, initTheta, initOmega, tempo, deltaT):

    vetTempos = np.arange(0, tempo, deltaT)
    result = []

    #condições iniciais
    estado = np.array([initTheta, initOmega])

    #implementação do método de Euler em si
    for t in vetTempos:
        result.append(estado)
        estado = estado + deltaT * pendulo(estado, grav, compr)

    return np.array(result)

def main(): 
    
    grav = 9.81
    compr = 1.0

    #transforma o angulo em graus para radianos
    #o angulo desejado pode ser alterado livremente
    initTheta = np.radians(60)
    initOmega = 0.0

    tempo = 10.0
    deltaT = 0.01

    resultPendulo = determinaPendulo(grav, compr, initTheta, initOmega, tempo, deltaT)

    #plota o gráfico do ângulo em função do tempo
    #irei anexar na pasta zipada um print de como o gráfico está sendo plotado
    plt.plot(resultPendulo[:, 0], label="Ângulo (θ)")
    plt.title("Movimento do Pêndulo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Ângulo (rad)")
    plt.show()

if __name__ == "__main__":
    main()
