from random import randint
ganhou1= 0
ganhou2= 0

while ganhou1< 3 and ganhou2< 3 :
    jogador1= randint(1,5)
    print("estou pronto")
    jogador2= input("escolha sua jogada entre tesoura, papel, pedra, lagarto e spock: ")
    if jogador2=="tesoura":
        jogador2= 1
    if jogador2=="papel":
        jogador2= 2
    if jogador2=="pedra":
        jogador2= 3
    if jogador2=="lagarto":
        jogador2= 4
    if jogador2=="spock":
       jogador2= 5
    if (jogador1==jogador2):
        print("empate")
        ganhou1=0
        ganhou2=0
    if jogador1==1:
        if jogador2==3 or jogador2==5:
            print("ponto seu")
            ganhou2 +=1
            ganhou1=0
        if jogador2==2 or jogador2==4:
            print("ponto meu")
            ganhou1 +=1
            ganhou2=0
    if jogador1==2:
        if jogador2==1 or jogador2==4:
            print("ponto seu")
            ganhou2 +=1
            ganhou1=0
        if jogador2==3 or jogador2==5:
            print("ponto meu")
            ganhou1 +=1
            ganhou2=0
    if jogador1==3:
        if jogador2==2 or jogador2==5:
            print("ponto seu")
            ganhou2 +=1
            ganhou1=0
        if jogador2==1 or jogador2==4:
            print("ponto meu")
            ganhou1 +=1
            ganhou2=0
    if jogador1==4:
        if jogador2==3 or jogador2==1:
            print("ponto seu")
            ganhou2 +=1
            ganhou1=0
        if jogador2==2 or jogador2==5:
            print("ponto meu")
            ganhou1 +=1
            ganhou2=0
    if jogador1==5:
        if jogador2==4 or jogador2==2:
            print("ponto seu")
            ganhou2 +=1
            ganhou1=0
        if jogador2==1 or jogador2==3:
            print("ponto meu")
            ganhou1 +=1
            ganhou2=0
    if jogador1==1:
        jogador1= "tesoura"
    if jogador1==2:
        jogador1= "papel"
    if jogador1==3:
        jogador1= "pedra"
    if jogador1==4:
        jogador1= "lagarto"
    if jogador1==5:
        jogador1= "spock"
    print("eu joguei %s" %jogador1)
if (ganhou1>=3) :
    print("EU GANHEI!!!")
else:
    print("voce ganhou")
    
