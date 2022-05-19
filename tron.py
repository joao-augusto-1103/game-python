from turtle import *

from freegames import square, vector

p1xy = vector(-200, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(200, 0)
p2aim = vector(-4, 0)
p2body = set()

p3xy = vector(0, 200)
p3aim = vector(0, -4)
p3body = set()


def inside(head):
    """Return True if head inside screen."""
    return -300 < head.x < 300 and -300 < head.y < 300


def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    p3xy.move(p3aim)
    p3head = p3xy.copy()

    if not inside(p1head) or p1head in p2body:
        print('Player blue and green wins!')
        return

    if not inside(p1head) or p1head in p3body:
        print('Player blue and green wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player red and green wins!')
        return

    if not inside(p2head) or p2head in p3body:
        print('Player red and green wins!')
        return

    if not inside(p3head) or p3head in p1body:
        print('Player red and blue wins!')
        return

    if not inside(p3head) or p3head in p2body:
        print('Player red and blue wins!')
        return

    if not inside(p1head) or p1head in p1body:
        print('Player blue and green wins!')
        return

    if not inside(p2head) or p2head in p2body:
        print('Player red and green wins!')
        return

    if not inside(p3head) or p3head in p3body:
        print('Player red and blue wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)
    p3body.add(p3head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    square(p3xy.x, p3xy.y, 3, 'green')
    update()
    ontimer(draw, 20)


setup(600, 600, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 's')
onkey(lambda: p2aim.rotate(90), 'g')
onkey(lambda: p2aim.rotate(-90), 'h')
onkey(lambda: p3aim.rotate(90), '9')
onkey(lambda: p3aim.rotate(-90), '5')
draw()
done()

#criação do Player 3
#Colocou colisão entre todos os players
#Colisão no próprio player
#Ajuste de velocidade

#------------------CODIGO ATULIZADO ABAIXO--------------------#

from turtle import *
from freegames import square, vector
from time import sleep

#Função para definir corpo do player
p1xy = vector(-200, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(200, 0)
p2aim = vector(-4, 0)
p2body = set()

p3xy = vector(0, 200)
p3aim = vector(0, -4)
p3body = set()

#função para definir a area de jogo:
def inside(head):
    """Return True if head inside screen."""
    return -300 < head.x < 300 and -300 < head.y < 300
    
#Timer para começar o jogo:
#Conta um tempo para iniciar o jogo.
print('T R O N')
sleep(2)
print('STARTING GAME...')
sleep(2)
print("3")
sleep(1)  
print("2")
sleep(1)
print("1")
sleep(2)
print("GO!")

#Função para Definir o movimento e para que lados
#os players irão se mexer:
def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    p3xy.move(p3aim)
    p3head = p3xy.copy()


    #Condisões de Colisão:
    #Consilão dos players entre eles (exemplo: player1 bateu em player2):
    if not inside(p1head) or p1head in p2body:
        print('Player blue and green wins!')
        
        return 

    if not inside(p1head) or p1head in p3body:
        print('Player blue and green wins!')
        return 

    if not inside(p2head) or p2head in p1body:
        print('Player red and green wins!')
        return 

    if not inside(p2head) or p2head in p3body:
        print('Player red and green wins!')
        return 

    if not inside(p3head) or p3head in p1body:
        print('Player red and blue wins!')
        return 

    if not inside(p3head) or p3head in p2body:
        print('Player red and blue wins!')
        return 

    #Colisão do player entre ele mesmo (exemplo: player1 bateu em player1):
    if not inside(p1head) or p1head in p1body:
        print('Player blue and green wins!')
        return 

    if not inside(p2head) or p2head in p2body:
        print('Player red and green wins!')
        return 

    if not inside(p3head) or p3head in p3body:
        print('Player red and blue wins!')
        return 

    #Função para adicionar a "cabeça" dos players
    #ao corpo:
    p1body.add(p1head)
    p2body.add(p2head)
    p3body.add(p3head)

    #Função para definir o tamanho, cor, velocidade 
    #de "desenho"(ontimer) dos players:
    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    square(p3xy.x, p3xy.y, 3, 'green')
    update()
    ontimer(draw, 20)

#Função para definir as teclas que serão usadas
#para controlar os players
setup(600, 600, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 's')
onkey(lambda: p2aim.rotate(90), 'g')
onkey(lambda: p2aim.rotate(-90), 'h')
onkey(lambda: p3aim.rotate(90), '5')
onkey(lambda: p3aim.rotate(-90), '6')
draw()
done()

#Criação do Player 3 - dar a opção de escolher a cor do personagem ou quantos jogadores deseja jogar.

#Colocou colisão entre todos os players e no próprio player - falha encontrada.

#Ajuste de velocidade - ajustar para o usuario escolher ou trocar por mudar a cor do player.

#Adicionado um Temporizador para começar o jogo.


