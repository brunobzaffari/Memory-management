# PUCRS - Disciplinba de Sistemas Operacionais
# T2: Gerenciador de Memória
# Versão 1.3 - 2023 11 14
# Componentes do Grupo: Bruno Bavaresco Zaffari, Tomás Bringhenti Onofrio,  Eduardo Felber Eichner e  Leonardo Lersch Forner
#
# Para executar o programa siga os passos abaixo. É necessário Python 3.9+ instalado na máquina
#   1. Abra o CMD
#   2. Navegue até o diretório do projeto
#   3. Execute o programa usando o comando abaixo
#           python .\src\germem.py
#
# Os arquivos de comandos devem ser salvos numa pasta com o nome "data", e estar junto ao diretorio do programa.
# Os comandos dever ser escritos em letras maiúsculas ("IN", "OUT") e sem espaços em branco.
#
# Referência
# https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/listas-encadeadas/

import os
import copy

class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, proc, tamanho, proximo_nodo=None):
        self.proc = proc
        self.tamanho = tamanho
        self.proximo = proximo_nodo

    def __repr__(self):
        if self.proximo is None or self.proximo.tamanho == 0:
            return '|%s,%s|' % (self.proc, self.tamanho)
        else:
            return '|%s,%s|->%s' % (self.proc, self.tamanho, self.proximo)


class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[ " + str(self.cabeca) + " ]"


def insere_no_inicio(lista, novo_proc, novo_tamanho):
    # 1) Cria um novo nodo com o dado a ser armazenado.
    novo_nodo = NodoLista(novo_proc, novo_tamanho)

    # 2) Faz com que o novo nodo seja a cabeça da lista.
    novo_nodo.proximo = lista.cabeca

    # 3) Faz com que a cabeça da lista referencie o novo nodo.
    lista.cabeca = novo_nodo


def insere_depois(lista, nodo_anterior, novo_proc, novo_tamanho):
    assert nodo_anterior, "Nodo anterior precisa existir na lista."

    # Cria um novo nodo com o dado desejado.
    novo_nodo = NodoLista(novo_proc, novo_tamanho)

    # Faz o próximo do novo nodo ser o próximo do nodo anterior.
    novo_nodo.proximo = nodo_anterior.proximo

    # Faz com que o novo nodo seja o próximo do nodo anterior.
    nodo_anterior.proximo = novo_nodo


def busca(lista, proc, tamanho):
    corrente = lista.cabeca
    while corrente and ( corrente.proc != proc or corrente.tamanho != tamanho):
        corrente = corrente.proximo
    return corrente


def busca_proc(lista, proc):
    corrente = lista.cabeca
    while corrente and corrente.proc != proc:
        corrente = corrente.proximo
    return corrente


def remove_proc(self, proc):
    assert self.cabeca, "Impossível remover dado de lista vazia."

    # Nodo a ser removido é a cabeça da lista.
    if self.cabeca.proc == proc:
        self.cabeca.proc = "VAZIO"
    else:
        # Encontra a posição do elemento a ser removido.
        anterior = None
        corrente = self.cabeca
        while corrente and corrente.proc != proc:
            anterior = corrente
            corrente = corrente.proximo
        # O nodo corrente é o nodo a ser removido.
        if corrente:
            corrente.proc = "VAZIO"
            corrente.tamanho = corrente.tamanho
        else:
            # O nodo corrente é a cauda da lista.
            anterior.proximo = None


def altera(self, proc, tamanho, novo_proc, novo_tamanho):
    assert self.cabeca, "Impossível alterar dado de lista vazia."

    # Nodo a ser alterado é a cabeça da lista.
    if self.cabeca.proc == proc and self.cabeca.tamanho == tamanho:
        self.cabeca.proc = novo_proc
        self.cabeca.tamanho = novo_tamanho
    else:
        # Encontra a posição do elemento a ser alterado.
        anterior = None
        corrente = self.cabeca
        while corrente and ( corrente.proc != proc or corrente.tamanho != tamanho):
            anterior = corrente
            corrente = corrente.proximo
        # O nodo corrente é o nodo a ser alterado.
        if corrente:
            corrente.proc = novo_proc
            corrente.tamanho = novo_tamanho
        else:
            # O nodo corrente é a cauda da lista.
            anterior.proximo = None


def status_memoria(lista):

    status = ""
    copy_list = copy.deepcopy(lista)
    concatena_memoria(copy_list)
    corrente = copy_list.cabeca

    while corrente is not None:
        if corrente.proc == "VAZIO" and corrente.tamanho != 0:
            status+= "|" + str(corrente.tamanho) + "|"
        corrente = corrente.proximo 
    
    return status
    
    
# def status_memoria(lista):
#     status = ""
#     corrente = lista.cabeca
#     tam = 0
#     while corrente != None:
#         if corrente.proc == "VAZIO":
#             tam = corrente.tamanho
#             while corrente.proximo == "VAZIO":
#                 tam += corrente.proximo.tamanho
#                 corrente = corrente.proximo
#             status+= "|" + str(tam) + "|"
#     return status

def concatena_memoria(lista):

    corrente = lista.cabeca
    encontrou = False

    while corrente is not None:
        encontrou = False
        if corrente.proc == "VAZIO":
            if corrente.proximo is not None:
                if corrente.proximo.proc == "VAZIO":
                    corrente.tamanho = corrente.tamanho + corrente.proximo.tamanho
                    corrente.proximo = corrente.proximo.proximo 
                    encontrou = True
        if not encontrou:
            corrente = corrente.proximo
            
def concatena_vazio(lista, start, end):
    corrente = start
    encontrou = False
    while corrente != end:
        encontrou = False
        if corrente.proc == "VAZIO":
            if corrente.proximo is not None:
                if corrente.proximo.proc == "VAZIO":
                    corrente.tamanho = corrente.tamanho + corrente.proximo.tamanho
                    corrente.proximo = corrente.proximo.proximo 
                    encontrou = True
        if not encontrou:
            corrente = corrente.proximo

def first_fit(lista, proc, tamanho):
    
    corrente = lista.cabeca
    while corrente and not (corrente.proc == "VAZIO" and corrente.tamanho >= tamanho):        
        corrente = corrente.proximo
    
    if corrente is None:
        print("Espaço insuficiente de memória")
    else:
        
        # Se sobrar espaço vazio, insere novo node
        if corrente.tamanho > tamanho:
            # Insere a sobre depois
            insere_depois(lista, corrente, corrente.proc, corrente.tamanho - tamanho)
        
        # Aloca o processo no espaço vazio
        altera(lista, corrente.proc, corrente.tamanho, proc, tamanho)


def best_fit(lista, proc, tamanho):
    melhorpos = None
    corrente = lista.cabeca

    while corrente :
        if corrente.proc == "VAZIO" and corrente.tamanho >= tamanho:
            if melhorpos is not None:
                melhorpos = corrente
            else:
                if melhorpos.tamanho > corrente.tamanho:
                    melhorpos = corrente        
        corrente = corrente.proximo
    
    if melhorpos is None:
        print("Espaço insuficiente de memória")
    else:
        
        # Se sobrar espaço vazio, insere novo node
        if melhorpos.tamanho > tamanho:
            # Insere a sobre depois
            insere_depois(lista, melhorpos, melhorpos.proc, melhorpos.tamanho - tamanho)
        
        # Aloca o processo no espaço vazio
        altera(lista, melhorpos.proc, melhorpos.tamanho, proc, tamanho)


def worst_fit(lista, proc, tamanho):
    piorpos = None
    corrente = lista.cabeca

    while corrente :
        if corrente.proc == "VAZIO" and corrente.tamanho >= tamanho:
            if piorpos is None:
                piorpos = corrente
            else:
                if piorpos.tamanho < corrente.tamanho:
                    piorpos = corrente        
        corrente = corrente.proximo
    
    if piorpos is None:
        print("Espaço insuficiente de memória")
    else:
        
        # Se sobrar espaço vazio, insere novo node
        if piorpos.tamanho > tamanho:
            # Insere a sobre depois
            insere_depois(lista, piorpos, piorpos.proc, piorpos.tamanho - tamanho)
        
        # Aloca o processo no espaço vazio
        altera(lista, piorpos.proc, piorpos.tamanho, proc, tamanho)


def next_fit(lista, proc, tamanho, pos_in):

    melhorpos = None
    corrente = pos_in
    proximo_node = None
    tam = 0
    pos_vazio_start = None
    pos_vazio_end = None
    # 1st loop to search from the initial position to the end of the list
    while corrente or melhorpos is not None:
        if corrente.proc == "VAZIO" and corrente.tamanho >= tamanho:
            melhorpos = corrente
            break
        elif corrente.proc == "VAZIO" and  corrente.tamanho < tamanho:
            tam = tam + corrente.tamanho
            pos_vazio_start = corrente
        while corrente.proximo == "VAZIO":
            corrente = corrente.proximo
            tam = tam + corrente.tamanho
            if  tam >= tamanho:
                melhorpos = pos_vazio_start
                pos_vazio_end = corrente
                break
        tam = 0
        corrente = corrente.proximo
       
    if melhorpos is not None:
        concatena_vazio(lista, pos_vazio_start, pos_vazio_end)
        insere_depois(lista, melhorpos, melhorpos.proc, melhorpos.tamanho - tamanho)
        altera(lista, melhorpos.proc, melhorpos.tamanho, proc, tamanho)
        proximo_node = melhorpos.proximo
        print(f"Ponteiro Next-Fit: [{proximo_node.proc},{proximo_node.tamanho}]")
        return proximo_node
        
    else: # If no free space was found to the right of the list, search from the beginning
        corrente = lista.cabeca
        # 2nd loop to search from the beginning (head) to the initial position
        while corrente or melhorpos is not None:
            if corrente.proc == "VAZIO" and corrente.tamanho >= tamanho:
                melhorpos = corrente
                break
            elif corrente.proc == "VAZIO" and  corrente.tamanho < tamanho:
                tam = tam + corrente.tamanho
                pos_vazio_start = corrente
            while corrente.proximo == "VAZIO":
                corrente = corrente.proximo
                tam = tam + corrente.tamanho
                if  tam >= tamanho:
                    melhorpos = pos_vazio_start
                    pos_vazio_end = corrente
                    break
            tam = 0
            corrente = corrente.proximo

        if melhorpos is not None:
             # If there is free space left, insert a new node
            if melhorpos.tamanho >= tamanho:
                # Insert the remainder afterwards
                concatena_vazio(lista, pos_vazio_start, pos_vazio_end)
                insere_depois(lista, melhorpos, melhorpos.proc, melhorpos.tamanho - tamanho)
                altera(lista, melhorpos.proc, melhorpos.tamanho, proc, tamanho)
                proximo_node = melhorpos.proximo
                print(f"Ponteiro Next-Fit: [{proximo_node.proc},{proximo_node.tamanho}]")
                return proximo_node
            else:
                print("Ponteiro Next-Fit: None")
                return None   
           
        else:
            print("Espaço insuficiente de memória")
           


def get_input(message, example_value, default_value, allow_null, onlydigit):

    aux = ""

    while aux == "":
        if default_value == "":
            aux = input("{}[{}]: ".format(message, example_value)).strip()
        else:
            aux = input("{}[tecle ENTER para {}]: ".format(message, default_value)).strip() or default_value
        if ( aux == "" and not allow_null):
            print("Informação Invalida. Por favor informe novamente.\n")
        else:
            if onlydigit == True and aux.isdigit() == False:
                aux = ""
                print("Informação Invalida. Por favor informe novamente.\n")
            else:
                break

    return aux


def carrega_processo():
    directory = os.getcwd() + '\\' + "data" + '\\'
    input_file_name = ""
    processos = []
    processo = []
     
    while input_file_name == "":
        input_file_name = input("Informe o nome do arquivo a ser carregado\n[sequencia1.txt]:")
        if input_file_name == "":
            print("Informação Inválida. Por favor informe novamente ou digite 'CANCELA' para terminar.\n")

    if input_file_name != "CANCELA":

        if os.path.isfile(fr"" + directory + input_file_name):
            with open(fr"" + directory + input_file_name) as file:
                for linha in file:
                    processo = []
                    if linha[0:2] == "IN":
                        #print(linha[0:2])
                        abre_parentese = linha.rfind("(")
                        fecha_parentese = linha.rfind(")")
                        virgula = linha.rfind(",")
                        #print(linha[abre_parentese+1:virgula])
                        #print(linha[virgula+1:fecha_parentese])
                        processo.append("IN")
                        processo.append(linha[abre_parentese+1:virgula])
                        processo.append(linha[virgula+1:fecha_parentese])
                        processos.append(processo)
                    elif linha[0:3] == "OUT":
                        #print(linha[0:3])
                        abre_parentese = linha.rfind("(")
                        fecha_parentese = linha.rfind(")")
                        #print(linha[abre_parentese+1:fecha_parentese])
                        processo.append("OUT")
                        processo.append(linha[abre_parentese+1:fecha_parentese])
                        processos.append(processo)
                    
            print("Instruções carregadas do arquivo {}.\n".format(directory + input_file_name))
                
        else:
            print("Arquivo {} não encontrado. Por favor verifique o nome do arquivo.\n".format(directory + input_file_name))   
    else:
        print("Operação Encerrada.\n")
    
    return processos

def main():
    
    tam_Mem = 0
    while tam_Mem < 4:
        tam_Mem = int(get_input("Informe o tamanho da memória 2^n (deve ser maior ou igual a 4):\n", "4", "4", False, True))

    while True:
        algo = int(get_input("\nInforme o tipo de alocação de memória \n1=first-fit\n2=best-fit\n3=worst-fit\n4=next-fit\n", "1", "1", False, True))
        if algo == 1 or algo == 2 or algo == 3 or algo == 4:
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2, 3 ou 4.\n")
            
    lista_memoria = ListaEncadeada()
    #print("Lista vazia:", lista_memoria)
    print("")
    print("Inicializa memória")
    insere_no_inicio(lista_memoria, "VAZIO", pow(2,tam_Mem))
    
    posIn = lista_memoria.cabeca

    instrucoes = carrega_processo()
    
    print("[{}]".format("]\n[".join([", ".join(i) for i in instrucoes])))
    print("Instruções\n")
    
    for p in range (0, len(instrucoes)):
        print("Lista: ", lista_memoria)
        print("Status: {}".format(status_memoria(lista_memoria)))
        if instrucoes[p][0] == "IN":
            print("IN({},{}) -------------------------------------------------------".format(instrucoes[p][1], instrucoes[p][2]))
            if algo == 1: 
                first_fit(lista_memoria, instrucoes[p][1],int(instrucoes[p][2]))
            elif algo == 2:
                best_fit(lista_memoria, instrucoes[p][1],int(instrucoes[p][2]))
            elif algo == 3:
                worst_fit(lista_memoria, instrucoes[p][1],int(instrucoes[p][2]))
            elif algo == 4:
                posIn = next_fit(lista_memoria, instrucoes[p][1],int(instrucoes[p][2]),posIn)        
        elif instrucoes[p][0] == "OUT":
            print("OUT({}) --------------------------------------------------------".format(instrucoes[p][1]))
            if algo == 4:
                if posIn != None:
                    if posIn.proc == instrucoes[p][1]:
                        # Encontra o elemento anterior aquele que será removido.
                        e_anterior = None
                        e_corrente = lista_memoria.cabeca
                        while e_corrente and e_corrente.proc != instrucoes[p][1]:
                            e_anterior = e_corrente
                            e_corrente = e_corrente.proximo
                        # Se o elemento anterior aquele que será removido é um VAZIO, então ajusta o PosIn que será posteiormente concatenado
                        if e_anterior.proc == "VAZIO":
                            posIn = e_anterior
                
                remove_proc(lista_memoria, instrucoes[p][1])
            else:
                remove_proc(lista_memoria, instrucoes[p][1])
                concatena_memoria(lista_memoria)

            

    print("Lista : ", lista_memoria)
    print("Status: {}".format(status_memoria(lista_memoria)))
    while True:
        opcao = input("\nDigite 'sai' para sair ou 'restart' para recomeçar:\n")
        if opcao == 'sai':
            break
        elif opcao == 'restart':
            print("")
            main()
        else:
            print("Opção inválida. Por favor, digite 'sai' ou 'restart'.")

if __name__ == "__main__":
    main()
