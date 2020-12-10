from __future__ import division 
import math
from tabulate import tabulate # https://pypi.org/project/tabulate/

# ** Desenvolvido por: Thiago Gabriel Souza Oliveira
# ** Matrícula: 17105760072

PI = 3.1416 # constante π
TOL = math.pow(10,-4) # tolerância (critério de parada)
# cos(x) e sin(x) são medidos em radianos

# f1(x) = cos(x) + 1 ; [a , b] = [? , ?] ; NÃO FUNCIONA COM O MÉTODO DA BISSEÇÃO
def f1(x):
    return (math.cos(x) + 1) 

# f2(x) = 10+(x-2)^2-10cos(2πx) ; [a , b] = [? , ?] ; NÃO FUNCIONA COM O MÉTODO DA BISSEÇÃO
def f2(x):
    return  (10 + math.pow(x-2, 2) - 10 * math.cos(2*PI*x)) 

# f3(x) = x^3-3x^2(2^-x)+3x(4^-x)-8^-x ; [a , b] = [0.5 , 1] ; FUNCIONA COM O MÉTODO DA BISSEÇÃO
def f3(x):
    return x**3 - 3*x**2 * 2**(-x) + 3*x*4**(-x) - 8**(-x)

# f4(x) = sin(x)sin(x^2/π) ; [a , b] = [4 , 4.5] ; FUNCIONA COM O MÉTODO DA BISSEÇÃO
def f4(x):
    return (math.sin(x)*math.sin(math.pow(x,2)/PI))

# f5(x) = (x-1.44)^5 ; [a , b] = [1 , 1.5] ; FUNCIONA COM O MÉTODO DA BISSEÇÃO
def f5(x):
    return (math.pow(x-1.44,5)) 


#Teste
#monta uma tabela no intervalo [a,b]
def achar_intervalo(f, a, b, i):
    cabecalho = ['x','f(x)']
    tabela = []

    print("a = ", a,"\n", "b = ", b, "\n")

    while (a <= b+i ):
        linha =[a , f(a)]
        tabela.append(linha)
        a += i
    
    print( 
        tabulate(
            tabela,
            headers=cabecalho,
            showindex=False,
            tablefmt="github",
            numalign="center"
        )
    )


#calcula o erro
def erro(a,b):
    return abs(b - a)

# Calcula o número máximo de iterações
def iteracoes(a,b):
    return int(math.ceil(math.log(abs(b-a)/TOL)/math.log(2)))


# Caulcula e montar a tabela em um arquivo .md (formato github)
# Obs.: o arquivo.md pode ser aberto com o bloco de notas, ou outro editor de texto
def bissecao(f, a, b, nome_arquivo="resultado.md"):

    if f(a)*f(b) > 0.0:
        print("Intervalo inválido!\n"
                +"Os valores da função nos pontos-finais iniciais devem ser de sinais opostos\n")
        return

    #cria a tabela/arquivo
    arquivo = open(nome_arquivo,'w')#arquivo de resultado
    cabecalho = ['Iteracao','a','x','b','f(x)', 'erro absoluto (b - a)'] #cabeçalho da tabela
    tabela = [] #tabela do método da bisseção
    p = (a+b)/2 #ponto médio # a + (b-a)/2
    linha = [
        round(a,5),
        round(p,5),
        round(b,5),
        round(f(p),5),
        round(erro(a,b),5)
    ] 
    tabela.append(linha) #adiciona a primeria linha da tabela, valores iniciais

    i = 1  
    fa = f(a)  
    N = iteracoes(a,b) #número máximo de iterações
    while (i <= N):  
        #iteracao da bissecao  
        fp = f(p)

        #condicao de parada  
        if ((fp == 0) or ((b-a)/2 < TOL)):
            #adiciona última linha da tabela/arquivo
            linha = [
                round(a,5),
                round(p,5),
                round(b,5),
                round(fp,5),
                round((erro(a,b)/2),5)
            ]
            tabela.append(linha)
            arquivo.write(
                tabulate(
                    tabela,
                    headers=cabecalho,
                    showindex="always", #"always"
                    tablefmt="github",
                    numalign="center"
                )
            )
            arquivo.write("\n\n#### Raiz aproximada = " + str(round(p,5)))
            arquivo.close()
            
            #imprime a tabela
            print()
            print(
                tabulate(
                    tabela,
                    headers=cabecalho,
                    showindex="always", #"always"
                    tablefmt="github",
                    numalign="center"
                )
            )
            print("\n#### Raiz aproximada = ", round(p,5), "\n")
 
            return  

        #bissecta o intervalo  
        i += 1  
        if (fa * fp > 0):  
            a = p  
            fa = fp  
        else:  
            b = p
        
        p = (a+b)/2

        #adiciona as linhas da tabela/arquivo
        linha = [
           round(a,5),
           round(p,5),
           round(b,5),
           round(fp,5),
           round(erro(a,b),5)
        ] 
        tabela.append(linha)
            
    raise NameError('Num. max. de iter. excedido!')


if __name__ == "__main__":

    #Ferramenta usada para comparação de resultados
        #https://pt.planetcalc.com/3718/

    #Funcões: f1, f2, f3, f4, f5
    '''
    >> bissecao(f, a, b, nome_arquivo)
    Obs.: o nome do arquivo é opcional caso não seja
          passado por parâmetro, o nome padrão será
          resultado.md
    '''
    
    #bissecao(f1, -5, 5, "resultado_f1.md") #não funcionou no método
    #bissecao(f2, -3, 3, "resultado_f2.md") #não funcionou no método

    #bissecao(f3, 0.5, 1, "resultado_f3.md") #funcionou
    #bissecao(f4, 4, 4.5, "resultado_f4.md") #funcionou
    bissecao(f5, 1, 1.5, "resultado_f5.md") #funcionou