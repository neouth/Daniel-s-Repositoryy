import pygame
import math
import winsound
import random
import os
import datetime
import time
from tkinter import simpledialog
import tkinter as tk
from tkinter import messagebox
pygame.init()

tamanho = (900,520)
tela =  pygame.display.set_mode( tamanho )
pygame.display.set_caption("Space Marker")
clock = pygame.time.Clock()
space = pygame.image.load("space.png")
pygame.display.set_icon(space)

estrelas = []

def abrir_caixa_de_pergunta(posicao):
    root = tk.Tk()
    root.withdraw()
    resposta = simpledialog.askstring("Pergunta", "Qual é o nome da estrela? \nCaso não saiba clique em OK ou em Cancel")
    if resposta is None or resposta.strip() == "":
        resposta = "desconhecido"
    resposta += f" ({posicao[0]}, {posicao[1]})"
    estrelas.append((posicao, resposta))

def desenhar_estrelas():
    for posicao, nome in estrelas:
        pygame.draw.circle(tela, (255, 255, 255), posicao, 5)
        fonte = pygame.font.Font(None, 20)
        texto = fonte.render(nome, True, (255, 255, 255))
        tela.blit(texto, (posicao[0] + 10, posicao[1] - 10))

def salvar_pontos_arquivo():
    with open("pontos.txt", "w") as arquivo:
        for posicao, nome in estrelas:
            arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")


def desenhar_linhas():
    if len(estrelas) >= 2:
        for i in range(len(estrelas) - 1):
            ponto1, nome1 = estrelas[i]
            ponto2, nome2 = estrelas[i+1]
            pygame.draw.line(tela, (255, 255, 255), ponto1, ponto2, 2)
            distancia = calcular_distancia(ponto1, ponto2)
            texto_distancia = f"Distância: {distancia:.2f}"
            fonte_distancia = pygame.font.Font(None, 20)
            texto_renderizado_distancia = fonte_distancia.render(texto_distancia, True, (255, 255, 255))
            posicao_texto_distancia = ((ponto1[0] + ponto2[0]) // 2, (ponto1[1] + ponto2[1]) // 2 - 10)
            tela.blit(texto_renderizado_distancia, posicao_texto_distancia)

def carregar_pontos_arquivo():
    try:
        with open("pontos.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",")
                x = int(partes[0])
                y = int(partes[1])
                nome = ",".join(partes[2:])
                estrelas.append(((x, y), nome))
    except FileNotFoundError:
        pass

def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def excluir_marcacoes():
    estrelas.clear()
    


def jogo():
    branco = (255,255,255)
    preto = (0,0,0)
    fundo = pygame.image.load("fundospace.jpg")
    running = True
    pygame.mixer.music.load("Space_Machine_Power.mp3")
    pygame.mixer.music.play(-1)
    fonte = pygame.font.Font(None, 20)
    texto1 = "Pressione F10 para Salvar os pontos"
    texto2 = "Pressione F11 para Carregar os pontos"
    texto3 = "Pressione F12 para Deletar os pontos"
    texto_renderizado1 = fonte.render(texto1, True, branco)
    texto_renderizado2 = fonte.render(texto2, True, branco)
    texto_renderizado3 = fonte.render(texto3, True, branco)
    posicao_texto1 = (260 // 2 - texto_renderizado1.get_width() // 2, 15 // 2 - texto_renderizado1.get_height() // 2)
    posicao_texto2 = (275 // 2 - texto_renderizado2.get_width() // 2, 45 // 2 - texto_renderizado2.get_height() // 2)
    posicao_texto3 = (265 // 2 - texto_renderizado3.get_width() // 2, 75 // 2 - texto_renderizado3.get_height() // 2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    abrir_caixa_de_pergunta(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    salvar_pontos_arquivo()
                elif event.key == pygame.K_F11:
                    carregar_pontos_arquivo()
                elif event.key == pygame.K_F12:
                    excluir_marcacoes()
                elif event.key== pygame.K_ESCAPE:
                    running = False
        


        tela.blit(fundo, (0,0))
        desenhar_linhas()
        desenhar_estrelas()
        tela.blit(texto_renderizado1, posicao_texto1)
        tela.blit(texto_renderizado2, posicao_texto2)
        tela.blit(texto_renderizado3, posicao_texto3)
        pygame.display.update()
        clock.tick(60)

jogo()