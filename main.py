def criar_pasta(nome):
    return{ 
        'nome': nome,
        'tipo': 'pasta',
        'filhos': []
    }
    
def criar_arquivo(nome, tamanho):
    return{
        'nome': nome,
        'tipo': 'arquivo',
        'tamanho': tamanho
    }
    
def adicionar_item(pasta_destino, item):
    pasta_destino['filhos'].update(item)
    
def imprimir_estrutura(pasta_raiz, nivel=0):
    
    prefixo = " " * nivel
    if pasta_raiz['tipo'] == "pasta":
        if nivel == 0:
            print("└─ {}/".format(pasta_raiz['nome']))
        else:
            print("{}├─ {}/".format(prefixo, pasta_raiz['nome']))
        for filho in pasta_raiz['filhos']:
            imprimir_estrutura(filho, nivel + 1)
    else:
        print("{}├─ {} ({} KB)".format(prefixo, pasta_raiz['nome'], pasta_raiz['tamanho']))
            
def calcular_tamanho(pasta):
    contador = 0
    for item in pasta['filhos']:
        if item["tipo"] == "pasta":
            contador += calcular_tamanho(item)
        else:
            contador += item["tamanho"]
    return contador
    
def imprimir_pre_ordem(self):

    for chave, valor in self.items():
       
        if chave == 'filhos':
            for filho in self['filhos']:
                imprimir_pre_ordem(filho)
            
        else:
            print(f"{chave}: {valor}")
        
    print('')
       


def imprimir_pos_ordem(self):
    return

diretorio = []
diretorio.append(criar_pasta('root'))

while(True):
    
    print('---menu---')
    print('')
    print('1 - criar uma pasta')    #feito
    print('2 - criar um arquivo')   #feito  
    print('3 - adiciona item')      #problema   
    print('4 - imprimir em pré-ordem')  #feito  
    print('5 - imprimir em pós-ordem')  #nao sei fazer o inverso
    print('6 - buscar arquivo')     #falta fazer
    print('7 - buscar pasta')   #falta fazer    
    print('8 - imprimir árvore')    #feito
    print('9 - calcular o tamanho de uma pasta')    #deu errado
    print('0 - sair')   #feito
    print('')
    
    escolha = input()
    
    if escolha == '0':
        print('ate logo')
        break
    
    if escolha == '1':
        print('')
        pasta = criar_pasta(input('digite o nome para a nova pasta: '))
        print(pasta)
        diretorio.append(pasta)
        print(diretorio)
        print('')
        print('pasta criada com sucesso')
        print('')
        
    elif escolha == '2':
        print('')
        diretorio.append(criar_arquivo(input('digite o nome do arquivo a ser criado: '), input('digite o tamanho do arquivo a ser criado:')))
        print('')
        print('arquivo criado com sucesso')
        print('')
        
    elif escolha == '3':
        print('')
        pasta = input('digite a pasta de destino: ')
        item = {'sdafsdf': 'dseafasdg'}#input('digite o item a ser adicionado')
        adicionar_item(pasta, item)
        print('')
        
    elif escolha == '4':
        for x in diretorio:
            imprimir_pre_ordem(x)
    
    elif escolha == '5':
        for x in diretorio:
            imprimir_pos_ordem(x)
            
    elif escolha == '6':
        arquivo = input('digite o arquivo a ser procurado: ')
        
        if diretorio.get('root'):
            print('arquivo encontrado')
        else:
            print('arquivo nao encontrado')
            
    
    #elif escolha == '7':
        
    elif escolha == '8':
        for x in diretorio:
            imprimir_estrutura(x)
        
    elif escolha == '9':
        print('')
        calcular_tamanho(input('insira a pasta que vc deseja que calculo o tamanho'))
    
    else:
        print('')
        print('escolha errada')
        print('')
        
#raiz = criar_pasta("root")

#docs = criar_pasta("documentos")
#img = criar_arquivo("foto.png", 150)
#txt = criar_arquivo("texto.txt", 50)

#adicionar_item(docs, txt)
#adicionar_item(raiz, docs)
#adicionar_item(raiz, img)

#imprimir_estrutura(raiz)
#print(calcular_tamanho(raiz)) 