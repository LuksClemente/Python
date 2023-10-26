#Atividade 1 - Questão 1
#Lucas Silva Clemente

#embora neste código nenhum método desta biblioteca esteja sendo usado diretamente
#pode ser que o usuário queria usar na expressão de entrada. Ex: sqrt(), sin(), etc.
import math

#método que define a função do termo a[n] que será utilizada
def termo(n, funcao):
    try:
        #avalia a expressão de entrada, quer será executada como uma instrução de Python
        return eval(funcao) 

    # Tratamento para divisão por zero
    except ZeroDivisionError:
        return float("inf")  

#método que calcula o limite
def limiteSeq(maxN):

    funcao = input("Digite aqui o termo a[n]: ")

    oldLim = termo(0, funcao)
    newLim = oldLim

    for n in range(1, maxN + 1):

        termoSeq = termo(n, funcao)
        
        #caso o termo seja infinito, retorna "infinito"
        if termoSeq == float("inf"):
            return "Infinito"  
        
        #caso o termo seja None, retorna "inexistente"
        if termoSeq is None:
            return "Inexistente"
        
        newLim = termoSeq
        
        #comparamos aproximadamente o limite atual com o limite anterior
        #se ambos os limites forem suficientemente próximos, retornamos o limite atual
        #o número de casas decimais a serem aproximadas pode ser alterado ao seu critério
        #quanto maior o numero de casas decimais a serem aproximadas, mais preciso o resultado é
        if round(newLim, 8) == round(oldLim, 8):
            return "O limite é: {:.2f}".format(newLim)
    
        oldLim = newLim

    #se chegarmos ao limite de iterações, iremos supor que o limite tende a infinito
    return "Infinito" 

def main(): 
    
    #define um limite máximo arbitrário
    #não utilizei o loop infinito "while True" pois caso o limite seja de fato infinito ele nunca chegaria ao fim da iteração
    #é preferivel que seja escolhido um limite alto para maior confiabilidade dos resultados
    #um limite muito baixo pode significar atingir o fim da iteração com uma conclusão incorreta
    #pode ser alterado ao seu critério
    maxN = 1000000000

    print(limiteSeq(maxN))

if __name__ == "__main__":
    main()

#RESULTADOS DE ALGUNS TESTES (pode copiar e colar no prompt de entrada, se desejar)
#-------------------------------------------------------------------------------------------------------
# ENTRADA                           |   RESULTADO
#-------------------------------------------------------------------------------------------------------
# None                              |   Inexistente
# float("inf")                      |   Infinito
# n                                 |   Infinito (após ficar um bom tempo rodando até dar o resultado)
# 1/(n**2)                          |   0.00
# 1/(n + 1)                         |   0.00
# (n + 1)/(3*n - 1)                 |   0.33
# math.sqrt(n)/(1 + math.sqrt(n))   |   1.00       
