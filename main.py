import pygame
import winsound
import sys
from tkinter import Tk, simpledialog
import json
pygame.init()
tamanho = 800, 600
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("bg.jpg")
pontos = []
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
fonte = pygame.font.Font(None, 24)

def abrirDialogo():
    root = Tk()
    root.withdraw()
    try:
        nome = simpledialog.askstring("Estrela", "Digite o nome da estrela:")
    except:
        nome = None
    root.destroy()
    return nome


pygame.display.flip()
