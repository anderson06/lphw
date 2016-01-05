# -*- coding: utf-8 -*-

from sys import exit

honey = False
somniferous = False
bronze_key = False
silver_key = False
gold_key = False
final_key = False
score = False
what_now_question = "O que você quer fazer agora?"

def dead(why):
    print why, "Tente mais uma vez!"
    exit(0)

def final_room(coming_from):
    global final_key

    print "Você está em uma sala com apenas duas portas."
    print "A porta por onde você entrou está atrás de você."
    print "Uma outra porta com uma placa onde está escrito 'saída' está a sua frente."

    print what_now_question

    while True:

        choice = raw_input("> ")

        if choice == "frente":
            if (final_key):
                print "Você terminou o jogo!! Parabéns!!"
                exit(0)
            else:
                print "A porta está trancada."
        elif choice == "voltar":
            piano_room("direita")
        elif choice == "sair":
            print "Jogue de novo quando quiser :) Tchau tchau"
            exit(0)
        else:
            print "Não entendi."

def try_get_key_from_bear():
    global somniferous
    global honey
    global silver_key

    if (somniferous and honey):
        print "Você misturou sonífero no mel e deu para o urso que apagou."
        print "Você pegou a chave de prata!"
        silver_key = True
    else:
        dead("O ursos ficou puto com a sua ousadia e arrancou seu braço.")

def bear_room(coming_from):
    global silver_key

    print "Você está em uma grande sala com um urso selvagem."
    print "Não entre em pânico! O urso está preso com uma coleira para ursos."
    print "Nesta sala há apenas a porta por onde você entrou."
    print "Você veio da porta", coming_from

    if (silver_key):
        print "Você pegou a chave de prata que estava no pescoço do urso."
    else:
        print "Há uma chave de prata pendurada no pescoço do urso."

    print what_now_question

    while True:

        choice = raw_input("> ")

        if choice == "pegar chave":
            try_get_key_from_bear()
        elif choice == "voltar":
            first_room("de trás")
        elif choice == "sair":
            print "Jogue de novo quando quiser :) Tchau tchau"
            exit(0)
        else:
            print "Não entendi."

def kitchen_room(coming_from):
    global honey

    print "Você está uma cozinha."
    print "Nesta sala há 2 portas, uma a frente e uma atrás."
    print "Você veio da porta", coming_from

    if (honey):
        print "Você já pegou o pote de mel que estava aqui."
    else:
        print "Não há muita coisa aqui além de um pote de mel."

    print what_now_question

    while True:

        choice = raw_input("> ")

        if choice == "pegar pote de mel":
            print "Você pegou o pote de mel."
            honey = True
            print what_now_question
        elif choice == "frente":
            lab_room("direita")
        elif choice == "atrás":
            first_room("esquerda")
        elif choice == "sair":
            print "Jogue de novo quando quiser :) Tchau tchau"
            exit(0)
        else:
            print "Não entendi."

def lab_room(coming_from):
    global somniferous

    print "Esta sala parece ser um antigo laboratório."
    print "Nesta sala há 2 portas, uma a esquerda e uma a direita."
    print "Você veio da porta", coming_from

    if (somniferous):
        print "Você já pegou o snífero que estava aqui."
    else:
        print "Há um pote de sonífero aqui."

    print what_now_question

    while True:

        choice = raw_input("> ")

        if choice == "pegar sonífero":
            print "Você pegou o sonífero."
            somniferous = True
            print what_now_question
        elif choice == "esquerda":
            kitchen_room("direita")
        elif choice == "direita":
            piano_room("esquerda")
        elif choice == "sair":
            print "Jogue de novo quando quiser :) Tchau tchau"
            exit(0)
        else:
            print "Não entendi."

def try_play_piano():
    global score
    global bronze_key

    if (score):
        print "Você tocou a música que estava na partitura."
        print "Uma chave de bronze caiu de dentro do piano."
        print "Você pegou a chave."

        bronze_key = True
    else:
        print "Você precisa de uma partitura pra tocar esse piano."

def piano_room(coming_from):
    print "Nesta sala há 3 portas, uma a esquerda, uma atrás e uma a direita."

    if (coming_from != "nenhuma"):
        print "Você veio da porta", coming_from

    print "Há um piano nesta sala."

    print what_now_question

    while True:

        choice = raw_input("> ")

        if choice == "tocar piano":
            try_play_piano()
            print what_now_question
        elif choice == "esquerda":
            lab_room("direita")
        elif choice == "direita":
            final_room("esquerda")
        elif choice == "atrás":
            score_room("frente")
        elif choice == "sair":
            print "Jogue de novo quando quiser :) Tchau tchau"
            exit(0)
        else:
            print "Não entendi."

def try_open_chest():
    global bronze_key
    global silver_key
    global gold_key
    global final_key

    if (bronze_key and silver_key and gold_key):
        print "Dentro do baú há mais uma chave. Inception!"
        print "Você pegou a chave, o que será que ela abre?"

        final_key = True
    else:
        print "Você não tem todas as chaves, tente procurar mais um pouco."


def chest_room(coming_from):
    print "Nesta sala há apenas a porta por onde você entrou e um baú."
    print "Este baú está trancado e possui 3 fechaduras."
    print "Uma fechadura de bronze, uma de prata e uma de ouro."

    print what_now_question

    while True:

        choice = raw_input("> ")

        if choice == "abrir baú":
            try_open_chest()
            print what_now_question
        elif choice == "voltar":
            score_room("direita")
        elif choice == "sair":
            print "Jogue de novo quando quiser :) Tchau tchau"
            exit(0)
        else:
            print "Não entendi."


def score_room(coming_from):
    global score

    print "Há 3 portas nesta sala."
    print "Há uma porta esquerda, uma a direita e uma frente."
    print "Você veio pela porta da", coming_from

    if (score):
        print "Você pegou a partitura que estava aqui."
    else:
        print "Há uma partitura de piano aqui."

    while True:

        print what_now_question
        choice = raw_input("> ")

        if choice == "esquerda":
            first_room("direita")
        elif choice == "direita":
            chest_room("esquerda")
        elif choice == "frente":
            piano_room("de trás")
        elif choice == "pegar partitura":
            print "Você pegou a partitura."
            score = True
        elif choice == "sair":
            print "Jogue de novo quando quiser :) Tchau tchau"
            exit(0)
        else:
            print "Não entendi."

def first_room(coming_from):
    global gold_key

    print "Você está em uma sala grande com alguns móveis antigos."
    print "Há um quadro na parede com a pintura de uma chave dourada."
    print "Há uma porta a sua esquerda, outra a sua direita e mais uma atrás de você."

    if (coming_from != "nenhuma"):
        print "Você veio da porta", coming_from
    else:
        print what_now_question

    while True:

        choice = raw_input("> ")

        if choice == "pegar quadro":
            gold_key = True
            print "Ao pegar o quadro você notou um compartimento secreto com uma chave dourada."
            print "Você pegou a chave."
            print what_now_question
        elif choice == "direita":
            score_room("esquerda")
        elif choice == "esquerda":
            kitchen_room("de trás")
        elif choice == "atrás":
            bear_room("de trás")
        elif choice == "sair":
            print "Jogue de novo quando quiser :) Tchau tchau"
            exit(0)
        else:
            print "Não entendi."

def start():
    print "Bem vindo ao maravilhoso jogo do Anderson."
    print 'Escreva apenas "direita" ou "esquerda" ou "frente" ou "atrás" para entrar nas portas nestas direções.'
    print "Tente interagir com o cenário e descubra como escapar deste estranho local."
    print "--------------------------------------------------------------------------------\n"

    first_room("nenhuma")


start()
