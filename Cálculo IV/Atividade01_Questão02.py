#Atividade 1 - Questão 2
#Lucas Silva Clemente

#define a série indicada no item A
def serieA(n):
    return 1/(n**3)


#define a série indicada no item B
def serieB(n):
        return 1/(n**2)

#definimos a função "estimador" solicitada, em que temos como entrada a[n] e o máximo de termos
def estimador(funcaoSerie, maxN):
    
    soma = 0
    #formula do erro da aproximação R[n] = 1/2N^2
    erroAprox = 1/(2*(maxN**2))

    #simplesmente vamos somando cada termo da sequencia
    for n in range(1, maxN + 1):
        soma += funcaoSerie(n)

    print("[Item A]Soma estimada[{} termos]: {:.6}".format(maxN, soma))
    print("[Item A]Erro estimado[{} termos]: {}".format(maxN, erroAprox))

def minTermos(funcaoSerie):
     
    soma = 0
    termos = 0
    n = 1
    #aproximação de (pi^2)/6 dada pela questão em 6 casas decimais
    x = 1.644934
    #como estamos trabalhando com uma aproximação, o valor não é exato
    #logo, devemos considerar a margem de erro
    #como estamos trabalhando com aproximações de 6 casas decimais, estou usando essa margem
    margemErro = 1e-6

    while True:
        #simplesmente vamos somando cada termo da sequencia
        soma += funcaoSerie(n)
        n += 1
        termos += 1

        #checamos se o módulo da diferença da soma e x é menor que a margem de erro
        #se sim, paramos o loop
        if(abs(soma - x) < margemErro):
             break

    print("[Item B]Mínimo de termos necessários: {}".format(termos))

def main():

    #chamadas dispostas de acordo com o numero de termos pedido pelo enunciado
    estimador(serieA, 10)
    estimador(serieA, 100)
    estimador(serieA, 1000)

    minTermos(serieB)

if __name__ == "__main__":
    main()
