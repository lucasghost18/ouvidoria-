

#TRABALHO ABELLA - OUVIDORIA DA UNIVERSIDADE ABC:
#1) Listar todas as manifestações
#2) Listar todas as sugestões
#3) Listar todas as reclamações
#4) Listar todos os elogios
#5) Enviar uma manifestação( criar uma nova )
#6) Pesquisar protocolo por número (ID)
#7) Sair

from csv import list_dialects
from tkinter.tix import AUTO


print (' Bem vindo a Ouvidoria da Universidade ABC') #Mensagem inicial
print() #Pula linha

#Variáveis Base: 
opçao= [] #input do usuário no Menu Principal
lista_manifestações= [] #Lista de manifestações
tipo_Manifestaçao= ['Sugestões', 'Reclamações','Elogios']# Tipo da Manifestação
#indice da lista : [     0             1            2   ]
lista_Sugestões=[]
lista_Reclamações=[]
lista_Elogios=[]

# EXIBIÇÃO DO MENU PRINCIPAL :
while opçao != 7 : #Enquanto o usuário não selecionar "Sair", continuar exibindo o Menu Principal
  print()
  print('1)Listar todas as manifestações')
  print('2) Listar todas as sugestões')
  print('3) Listar todas as reclamações')
  print('4)Listar todos os elogios')
  print('5) Enviar uma manifestação( criar uma nova )')
  print('6) Pesquisar manifestação por número de protocolo por número (ID)')
  print('7) Sair')
  print() #Pula linha

  #INPUT DO USUÁRIO NO MENU PRINCIPAL
  opçao= int(input('Digite a sua opção:')) #Selecionar opção do Menu Principal
  print()
  #CASO O USUÁRIO DIGITE UMA OPÇÃO INVÁLIDA NO MENU PRINCIPAL:
  if opçao < 1 or opçao > 7:
      print('Opção inválida.Por favor verifique a opção escolhida e digite novamente')
      print() #Pula linha
  #CONTABILIZA AS MAIFESTAÇÕES:
  quant_manifestações= len(lista_manifestações)

  #OPÇÃO 1: LISTAR TODAS AS MANIFESTAÇÕES:
  if opçao == 1:
      if lista_manifestações == []:  #Caso a lista de manifestações esteja vazia:
           print('Caixa de Manifestações vazia. Por favor selecione a opção 5) p/ adicionar uma nova Manifestação')
      else:
          print('Exibindo Lista de Manifestações')# Exibiçaõ da lista de Manifestações
          for manifestaçao in lista_manifestações :
              mani_quebrado= manifestaçao.split('#') #Fragmentando a Manifestação em #
              print('protocolo:{} -- tipo de Manifestação:{} -- Requisitante:{}-- Descrição:{}'.format(mani_quebrado[0],mani_quebrado[1],mani_quebrado[2],mani_quebrado[3]))
              #Fim da lista de manifestações

  #OPÇÃO 2: LISTAR TODAS AS SUGESTÕES:
  elif opçao == 2:
      if lista_Sugestões==[]:
            print('Caixa de Sugestões Vazia no momento')
      else:
           print('Exibindo Lista de Sugestões: ')
           for manifestaçao in lista_Sugestões:
                mani_quebrado = manifestaçao.split('#')
                print('protocolo:{}-- requisitante {}--descriçao: {}'.format(mani_quebrado[0],mani_quebrado[2],mani_quebrado[3]))
                # fim das sugestoes

    #OPÇÃO 3: LISTAR TODAS AS RECLAMAÇÕES:
  elif opçao == 3:
      if lista_Reclamações==[]:
            print('Caixa de Reclamações vazia no momento')
      else:
          print('Exibindo Lista de Reclamaçoes:')
          for manifestaçoes in lista_Reclamações:
                mani_quebrado = manifestaçoes.split('#')
                print('protocolo:{} , requisitante:{} , descriçao{}: ' .format(mani_quebrado[0],mani_quebrado[2],mani_quebrado[3]))
                #fim de reclamaçoes
    
    #OPÇÃO 4: LISTAR TODOS OS ELOGIOS:
  elif opçao == 4:
      if lista_Elogios ==[] : #Caso a lista de Elogios esteja Vazia 
          print('Caixa de Elogios vazia no momento')
      else :# Exibição da Lista de Elogios:
          print('Exibindo Lista de Elogios: ')
          for manifestaçao in lista_Elogios:
              mani_quebrado = manifestaçao.split('#') # Quebra a string em #
              print('protocolo:{} , requisitante:{} , descriçao{}: ' .format(mani_quebrado[0],mani_quebrado[2],mani_quebrado[3])) #Sring Manifestação- 'Tipo da Manifestação'

  #OPÇÃO 5: CRIAR UMA NOVA MANIFESTAÇÃO:
  elif opçao == 5:
      tipo= 0
      print('Criando Nova Manifestação...')
      nome= input('Insira o nome do Requisitante:') #Pede o nome do Requisitante
      while tipo <1 or tipo >3:
          tipo = int(input('Digite o tipo de Manifestação : [1) para Reclamações , 2) para Sugestões,3) para Elogios]:')) #Pede do usuário o tipo de manifestação
          if tipo <1 or tipo> 3:
              print('A opção selecionada é inválida ou inexistente.')
              print()
      descriçao = input ('digite a descriçao da manifestaçao:')
      protocolo =str(len(lista_manifestações)+ 1)
         #Verificação de possíveis erros no input do usuário:
          
      if tipo==1:
            manifestaçao=protocolo + '#' + 'Reclamaçao' + '#' + nome + '#' +descriçao
            lista_manifestações.append(manifestaçao)
            lista_Reclamações.append(manifestaçao)

      elif tipo==2:
            manifestaçao=protocolo + '#' + 'Sugestao' + '#' + nome + '#' +descriçao
            lista_manifestações.append(manifestaçao)
            lista_Sugestões.append(manifestaçao)

      elif tipo==3:
            manifestaçao=protocolo + '#' + 'Elogios'+ '#' + nome + '#' +descriçao
            lista_manifestações.append(manifestaçao)
            lista_Elogios.append(manifestaçao)         

 #OPÇÃO 6: PESQUISAR PROTOCOLO POR NÚMERO (ID)
  elif opçao  == 6:
    if lista_manifestações == [] : # Caso a lista de manifestações esteja vazia 
        print('No momento ainda não há nenhum protocolo disponível. Clique na opção 5) p/ add uma nova Manifestação')
    else : #Caso o protocolo de fato exista na Lista de Manifestações
        quantidade= len(lista_manifestações) #Contabiliza a quantidade de Manifestações existentes
        print('Número de protocolos disponíveis:[{}]'. format(quantidade)) #Printa a quantidade de protocolos disponíveis
        input_protocolo = int(input('Digite o número do  seu protocolo (ID): ')) #Input do usuário do número do protocolo
        if input_protocolo < 1 or input_protocolo > quantidade :# Verificar caso o protocolo digitado seja inválido
         print(' Protocolo inválido ou inexistente')
        else:
            for manifestaçaot in lista_manifestações:
                input_proto= input_protocolo #Conversão do número do protocolo em string
                mani_quebrado= manifestaçaot.split('#') # Quebra a sting da Manifestação em "#"
                if input_proto == int(mani_quebrado[0]):
                    print('-Código-')
                    for i in mani_quebrado:
                      print( i ) #Printa a manifestação
                  
    
    #OPÇÃO 7 : SAIR
print ('Progama encerrado')





    







