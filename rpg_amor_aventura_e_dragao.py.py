import random

nome = str(input('Escolha o nome do seu personagem: '))
poder = str(input('Qual especialidade  do seu personagem: '))
raça = str(input('Coloque a raça do seu personagem: '))
resumo = str(input('Faça um pequeno resumo do seu personagem: '))

print('')

print('>>>>>>>>>>>>>')
print('Começo da Aventura')
print('seu aventureiro planeja sair; jogue os dados para ver se ele sai: ')
dadosi=random.randint(1,6)
print(dadosi)
match dadosi:

    case 1:
        print("volta para casa e fim")
    case 2|3:
        print("sai em aventura sem mais nem menos")
    case 4 | 5: 
        print("recebe 10 moedas de  ouro")
    case 6: 
        print("Recebe uma armadura de batalha sagrada")
print('>>>>>>>>>>>>>')    
print(' ')
if dadosi!=1:
  escolha= int(input('''Logo após sair da cidade vc da de cara com bandidos o que fazer
  (1)Atacar
  (2)Fugir
  (3)Persoadir'''))

  if escolha ==1:
      dadosc=random.randint(1,6)
      print(dadosc)
    
      match dadosc:
          case 1:
            print("Voce morre")
          case 2|3|4:
            print("vc mal sobrevive, mas acha um mapa de tesouro")
          case 5:
            print("Sobrevive com 2 de vida e encontra um mapa") 
          case 6:
            print("Sobrevive sem nenhum arranhão e encontra um mapa do tesouro")  
  elif escolha ==2:
    dadosc=random.randint(1,6)
    print(dadosc)
    
    match dadosc:
              case 1|2:
                print("Voce da de cara com um leão e morre por estar fraco")
              case 3|4:
                print("Decide voltar a vida comum")
              case 5:
                print("sobrevive  e encontra uma entrada  de uma caverna com tesouros, mas se machuca no caminho ficando com 1 de vida") 
              case 6:
                print("Sobrevive sem nenhum arranhão e encontra uma entrada  de uma caverna com tesouros")
  elif escolha == 3:
    dadosc=random.randint(1,6)
    print(dadosc)
    
    match dadosc:
              case 1:
                print("Voce falha e é morto")
              case 2|3|4:
                print("Voce falha, se tiver dinheiro fica vivo e se junta a eles, se não morre")
                tem = str(input('Tem dinheiro?[S/N]')).upper()
                if tem =='S':
                    print( 'Se junta a eles em uma caça ao tesouro, mas depois eles te matam')
                else:
                      print('Voce morre na hora')#

              case 5:
                print("sobrevive, e pode sair sem nenhum problema ") 
              case 6:
                print("Vc é tão gente boa que eles te entregam um mapa do tesouro")
 
  if dadosc == 5 or 6:   
      print('>>>>>>>>>>>>>')
      print(' ')
      print('Ao seguir o mapa é encontrado uma caverna ' )
      pessoas = str(input('Tinha pessoas com vc? [S/N] ')).upper()
      if pessoas == 'S':
          print( 'Antes mesmo de entrar um Dragão vermelho escarlate aparece e mata todos ao seu redor com um sopro sopro de fogo ')
      else: 
          print( 'Antes mesmo de entrar um Dragão vermelho escarlate aparece e solta um poderoso sopro de fogo em vc')
      print('vc sobreviveria? ')
      dadosd=random.randint(1,6)
      print(dadosd)
      match dadosd:
        case 1|2|3:
                  print("Voce é morto")
                  print('Bom jogo pra vc')
        case 4|5:
                  sobre=int(input('''Sobrevive e tenta dialogar com o Dragão vc tenta
      (1)Convencer
      (2)Intimidar
      (3)Conquistar'''))
                  if sobre == 1:
                          print('Voce e o Dragão se tornam amigos e fim da aventura')
                  elif sobre ==2:
                          print('Voce morre, afinal dragões são criaturas orgulhosas')
                  elif sobre ==3:
                          print('Voce descobre que o dragão é femea e decide criar uma familia com ela')

        case 6:
                print(" Voce chuta a bola sagrada e derrota o dragão")
  else:
    print('Bom jogo')
else:
  print('Bom jogo')
      