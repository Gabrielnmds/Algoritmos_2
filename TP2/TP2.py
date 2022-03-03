from timeit import default_timer as timer
import os
import csv


# Classe mochila que armazena todos os itens, valores e pesos do arquivo de entrada
class Mochila:
    qtd_itens = 0  # quantidade total de itens
    capacidade = 0  # capacidade maxima da mochila
    # valor maximo capaz de ser colocado na mochila (atualiza ao longo da execucao do algoritmo)
    valorMaximo = 0
    valor = []  # lista dos valores de cada item
    peso = []  # lista dos pesos de cada item
    valorPorPeso = []  # lista do relacao valor/peso de cada item
    itensOrdenados = []  # lista ordenada com base no valor da relacao valor/peso de cada item

    def __init__(self, n, wmax):  # metodo construtor
        self.qtd_itens = n
        self.capacidade = wmax

    def montaMochila(self, v, w):  # metodo de montagem da mochila
        self.valor = v
        self.peso = w
        self.valorPorPeso = [self.valor[i]/self.peso[i]
                             for i in range(self.qtd_itens)]
        self.itensOrdenados = [i[0] for i in sorted(
            enumerate(self.valorPorPeso), reverse=True, key=lambda item: item[1])]


# Funcao que recebe o arquivo de entrada e monta a mochila com todas os valores
def abrirArquivo(arquivo):
    with open(arquivo) as file:  # abre o arquivo de entrada
        linha = file.readlines()
        # pega a quantidade de itens
        n = int(linha[0].strip("\n").split(" ")[0])
        # pega a capacidade maxima da mochila
        wmax = float(linha[0].strip("\n").split(" ")[1])
        mochila = Mochila(n, wmax)  # cria a mochila
        v = []
        w = []
        for i in range(n):
            # monta a lista de valores dos itens
            v.append(float(linha[i-1].strip("\n").split(" ")[0]))
            # monta a lista de pesos dos itens
            w.append(float(linha[i-1].strip("\n").split(" ")[1]))
        mochila.montaMochila(v, w)  # monta a mochila
        file.close()
        return mochila


# Funcao que calcula o upper bound
def upperBound(valor, pesoMaximo, pesoAtual, ratio):
    return valor + (pesoMaximo + pesoAtual)*ratio


# Algoritmo pra solucao do problema da mochila utilizando backtracking
def KS_Backtracking(mochila, temp_valor, temp_capacidade, i, visitado):
    if i >= mochila.qtd_itens:
        return mochila.valorMaximo
    else:
        wmax = mochila.capacidade
        index = mochila.itensOrdenados[i]
        if temp_capacidade+mochila.peso[index] == wmax:
            visitado[i] = 1
            temp_capacidade += mochila.peso[index]
            temp_valor += mochila.valor[index]
            mochila.valorMaximo = max(temp_valor, mochila.valorMaximo)
            return mochila.valorMaximo
        elif temp_capacidade+mochila.peso[index] < wmax:
            visitado[i] = 1
            temp_capacidade += mochila.peso[index]
            temp_valor += mochila.valor[index]
            mochila.valorMaximo = max(temp_valor, mochila.valorMaximo)
            i += 1
            return KS_Backtracking(mochila, temp_valor, temp_capacidade, i, visitado)
        elif temp_capacidade+mochila.peso[index] > wmax:
            if i+1 <= mochila.qtd_itens:
                i += 1
                return KS_Backtracking(mochila, temp_valor, temp_capacidade, i, visitado)
            else:
                while visitado[i] == 0 and i == 0:
                    i -= 1
                index = mochila.itensOrdenados[i]
                visitado[i] = 0
                temp_valor -= mochila.valor[index]
                temp_capacidade -= mochila.peso[index]
                return KS_Backtracking(mochila, temp_valor, temp_capacidade, i, visitado)


# Algoritmo pra solucao do problema da mochila ultilizando branch and bound
def KS_BranchAndBound(mochila, temp_valor, temp_capacidade, i):
    if i+1 == mochila.qtd_itens:
        index = mochila.itensOrdenados[i]
        if temp_capacidade+mochila.peso[index] <= mochila.capacidade:
            temp_capacidade += mochila.peso[index]
            temp_valor += mochila.valor[index]
            mochila.valorMaximo = max(temp_valor, mochila.valorMaximo)
            return mochila.valorMaximo
        else:
            return mochila.valorMaximo
    else:
        wmax = mochila.capacidade
        index = mochila.itensOrdenados[i]
        if temp_capacidade+mochila.peso[index] <= mochila.capacidade:
            index_1 = mochila.itensOrdenados[i+1]
            v_1 = temp_valor + mochila.valor[index]
            w_1 = temp_capacidade + mochila.peso[index]
            v_2 = temp_valor
            w_2 = temp_capacidade
            r = mochila.valorPorPeso[index_1]
            if upperBound(v_1, wmax, w_1, r) >= upperBound(v_2, wmax, w_2, r):
                mochila.valorMaximo = max(mochila.valorMaximo, w_1)
                return KS_BranchAndBound(mochila, v_1, w_1, i+1)
            else:
                mochila.valorMaximo = max(mochila.valorMaximo, w_2)
                return KS_BranchAndBound(mochila, v_2, w_2, i+1)
        else:
            return KS_BranchAndBound(mochila, temp_valor, temp_capacidade, i+1)


# Preencher aquivo csv com o resultado da execucao de cada paradigma para cada arquivo teste
path = "C:/Users/Gabriel Nunes/Desktop/Matcomp_shit/7° Periodo/ALG2/Trabalhos praticos/TP2/TP2"
files = os.listdir(path)  # vetor com os nomes dos arquivos de teste

with open('TP2.csv', 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo, delimiter=';')  # cria o objeto de escrita
    writer.writerow(['Gabriel Nunes Mendes'])  # escreve o cabeçalho
    for file in files:
        M = abrirArquivo(file)  # monta a mochila para o backtracking
        N = abrirArquivo(file)  # monta a mochila para o branch and bound
        visitado = [0 for j in range(M.qtd_itens)]
        start = timer()
        # executa backtracking sobre a entrada
        result_BT = KS_Backtracking(M, 0, 0, 0, visitado)
        end = timer()
        time_BT = end - start  # calcula o tempo de execucao do backtracking
        start = timer()
        # executa branch and bound sobre a entrada
        result_BB = KS_BranchAndBound(N, 0, 0, 0)
        end = timer()
        time_BB = end - start  # calcula o tempo de execucao do branch and bound
        writer.writerow([file,
                        result_BB,
                        time_BT,
                        time_BB])
    arquivo.close()
